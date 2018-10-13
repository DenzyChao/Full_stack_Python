import multiprocessing
from time import ctime


def consumer(input_q):
    print('Into consumer: ', ctime())
    while True:
        item = input_q.get()
        print('pull', item, 'out of q')
        input_q.task_done() # 发出信号通知任务完成
    print('Out of consumer:', ctime())


def producer(sequence, output_q):
    print('into producer: ', ctime())
    for item in sequence:
        output_q.put(item)
        print('put', item, 'into q')
    print('Out of producer: ', ctime())


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()

    # 生产多个产品，sequence代表发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.join()