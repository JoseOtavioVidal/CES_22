import time
import thread
import multiprocess

if __name__ == "__main__":
    t1 = time.process_time()
    thread.th()
    t2 = time.process_time()
    print("{}".format(t2-t1))
    t1 = time.process_time()
    multiprocess.multi()
    t2 = time.process_time()
    print("{}".format(t2 - t1))


