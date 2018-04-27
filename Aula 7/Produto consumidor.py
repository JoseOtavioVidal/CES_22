from threading import Thread, RLock
import time
import random


class producer(Thread):
    def __init__(self, elements, lock):
        Thread.__init__(self)
        self.elements = elements
        self.lock = lock


    def run(self):
        for i in range(10):
            element = random.randint(0, 256)
            self.lock.acquire()
            self.elements.append(element)
            self.lock.release()
            print("Producer Notify: item {} appended to list by {}".format(element, self.name))
            time.sleep(1)

class consumer(Thread):
    def __init__(self, elements, lock):
        Thread.__init__(self)
        self.elements = elements
        self.lock = lock


    def run(self):
        while True:
            self.lock.acquire()
            if len(self.elements) == 0:
                self.lock.release()
                time.sleep(2.5)
            else:
                element = self.elements.pop()
                self.lock.release()
                print("Consumer Notify: item {} popped from list by {}".format(element, self.name))



if __name__ == "__main__":
    items = 10
    print("Putting {} elements in the box".format(items))
    lock = RLock()
    elements = []
    t1 = producer(elements, lock)
    t2 = consumer(elements, lock)
    t3 = consumer(elements, lock)
    t4 = consumer(elements, lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()