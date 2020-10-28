import time 
import threading 


def test1(def_name):
    for i in range(2):
        print('这是一个线程测试:%s，编号为 %d' % (def_name,i))
        time.sleep(1)

def test2(def_name):
    for i in range(2):
        print('这是一个线程测试:%s，编号为 %d' % (def_name,i))
        time.sleep(1)


def main():
    
    print('开始  {}'.format(time.ctime()))
    # 通过threading模块的Thread类创建一个线程对象
    # 这个对象接收两个参数,target=目标函数名,args为元组，包含传入函数的所有参数
    t1 = threading.Thread(target=test1,args=('test1',))
    t2 = threading.Thread(target=test2,args=('test2',))
    # 当调用start()时，才会真正的创建线程，并且开始执行
    t1.start()
    t2.start()

    # 查看线程数
    while True:
        length = len(threading.enumerate())
        # print('线程名：{}'.format(threading.enumerate()))
        print('当前运行的线程数为：{}'.format(length))
        if length<=1:
            break

    time.sleep(5)
    # 主线程会等待所有的子线程结束后才结束
    print('结束  {}'.format(time.ctime()))

if __name__=='__main__':
    main()
