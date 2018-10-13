# encoding=utf-8
import threading
import time
import queue


class Produce(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = 'product' + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # get是从queue中取出一个值
                    msg= self.name + 'consume' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(5000):
        queue.put('new product'+str(i))
    for i in range(2):
        p =  Produce()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()