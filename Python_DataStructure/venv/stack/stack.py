class Stack(object):
    def __init__(self,limit=10):
        #实际的存放方式是list
        self.stack = [] #存放元素
        self.limit = limit #栈容量极限

    def push(self,data):
        if len(self.stack) >= self.limit:
            raise IndexError('超出容量极限·')
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack
        else:
            raise IndexError('pop from empty stack')

    #查看顶栈上的元素
    def peek(self):
        if self.stack:
            return self.stack[-1]

    #查看是否为空
    def is_empty(self):
        return bool(self.stack)

    #查看栈的长度
    def size(self):
        return len(self.stack)

    if __name__== 'main':
        peek()

