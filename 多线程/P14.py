import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def func_1():
    print('func_1 starting............')
    lock_1.acquire()
    print('func_1 apply lock_1........')
    time.sleep(2)
    print('func_1 waiting lock_2.....')

    lock_2.acquire()
    print('func_1 apply lock_2')

    lock_2.release()
    print('func_1 release lock_2')
    lock_1.release()
    print('func_1 release lock_1')

    print('func_1 done........')


def func_2():
    print('func_2 starting............')
    lock_2.acquire()
    print('func_2 apply lock_1........')
    time.sleep(2)
    print('func_2 waiting lock_2.....')

    lock_1.acquire()
    print('func_2 apply lock_2')

    lock_1.release()
    print('func_2 release lock_1')
    lock_2.release()
    print('func_2 release lock_2')

    print('func_2 done........')


if __name__ == '__main__':

    print('main process start .......')
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('main process start..........')