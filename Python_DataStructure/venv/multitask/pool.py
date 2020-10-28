#实现线程池
from multiprocessing.dummy import Pool

def proc_some(args):
    pass

if __name__ == '__main__':
    pool = Pool(2)
    str_list = list()
    results = pool.map(proc_some,str_list)
    print(results)

