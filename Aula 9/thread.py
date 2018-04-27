import threading
import random


def list_apppend(count, id, out_list):
    for i in range(count):
        out_list.append(random.randint(0,1000))


def th():
    size = 1000000
    threads = 2

    jobs = []

    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=list_apppend(size, i, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("Process with multithreading terminate")