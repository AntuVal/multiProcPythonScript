import os
import multiprocessing
import itertools

PATH = "instances/"
NAME = "CP_slack_dist_ordering-rnd-softmax-restart"

NUMPROC = 32

OPTION = "--timelimit 3600 --boolmodelpos --restart --randomSoftMax"
CMD = "java -cp jarfile/choco-solver-4.10.2.jar:jarfile/myjar.jar Main"

SEEDS =[32322, 563569, 490768, 98772, 884361, 564737, 295649, 470526, 907938, 470087]

def func(data):
    filename, seed, num = data
    outfile = NAME + "_" + str(num) + ".out"
    errorfile = NAME + "_" + str(num) + ".error"
    cmd = CMD+" {} {} --seed {} > results/{} 2> errors/{}".format(PATH + filename, OPTION, seed, outfile, errorfile)
    os.system(cmd)



if __name__ == '__main__':
    files = os.listdir(PATH)

    data = [a for a in itertools.product(*[files, SEEDS])]
    data = [(b[0], b[1], a) for a, b in enumerate(data)]

    pool = multiprocessing.Pool(processes=NUMPROC)
    pool.map(func, data)
    pool.close()
    pool.join()
