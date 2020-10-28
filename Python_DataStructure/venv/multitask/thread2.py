import threading
import time

#threading.Thread类有一个run方法，用于定义线程的功能函数
#多线程
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I am"+self.name+'@'+str(i)
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()
