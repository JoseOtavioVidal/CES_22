import multiprocessing
import random

def list_apppend(count, id, out_list):
    for i in range(count):
        out_list.append(random.randint(0,1000))

def multi():
    size = 1000000
    procs = 2
    jobs = []

    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(target=list_apppend, args=(size, i, out_list))
        jobs.append(process)

    for p in jobs:
        p.start()

    for p in jobs:
        p.join()

    print("Process with multiprocess terminate")