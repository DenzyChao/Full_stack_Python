'''
利用time函数，生成连个函数
顺序调用
计算运行时间
'''

import time

def loop1():
    print('start loop 1 at:', time.ctime())
    time.sleep(4)
    print('end loop 1 at:', time.ctime())

def loop2():
    print('start loop 2 at:', time.ctime())
    time.sleep(2)
    print('end loop 2 at:', time.ctime())

def main():
    print('Starting at:', time.ctime())
    loop1()
    loop2()
    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()