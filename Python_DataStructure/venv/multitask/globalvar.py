from threading import Thread
import time

#多线程共享全局变量，可以允许在多个线程之间共享数据

def work1(nums):
    nums.append(44)
    print("---in work1---",nums)

def work2(nums):
    time.sleep(1)
    print("---in work2---",nums)

g_nums = [11,22,33]

t1 = Thread(target=work1,args=(g_nums,))
t1.start()

t2 = Thres zad(target=work2,args=(g_nums,))
t2.start()
