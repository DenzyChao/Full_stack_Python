import time
import _thread as thread

def loop1():
    print('Start loop 1 at:', time.ctime())
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2():
    print('Start loop 2 at:', time.ctime())
    time.sleep(2)
    print('End loop 2 at:', time.ctime())

def main():
    print('Starting at:', time.ctime())
    thread.start_new_thread(loop1, ())

    thread.start_new_thread(loop2, ())

    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)