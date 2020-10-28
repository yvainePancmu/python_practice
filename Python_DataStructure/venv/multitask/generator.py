import inspect
from functools import wraps

#添加一个装饰器
def coroutine(func): #预激协程装饰器
    @wraps(func)
    def wrapper(*args,**kw):
        g = func(*args,**kw)
        next(g)
        return g
    return wrapper

#和装饰器名字同名
# @coroutine
# def generator():
#     i = '激活生成器'
#     while True:
#         try:
#             value = yield i
#         except ValueError:
#             print('OVER')
#         i = value
#         print(i)
@coroutine
def generator():
    l = []
    while True:
        value = yield
        if value == 'CLOSE':
            break
        l.append(value)
    return l


if __name__ == '__main__':
    g = generator()
    #state = inspect.getgeneratorstate(g)
    # next(g)
    # state = inspect.getgeneratorstate(g)
    #
    # print(state)
    g = generator()
    g.send('hello')
    g.send('shiyanlou')
    g.send('CLOSE')

    # g.send('Hello shiyanlou')
    # state = inspect.getgeneratorstate(g)
    # print(state)
    # g.throw(ValueError)
    # state = inspect.getgeneratorstate(g)
    # print(state)
    # g.close()
    # state = inspect.getgeneratorstate(g)
    # print(state)

