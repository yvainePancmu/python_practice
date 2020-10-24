class Node(object):

    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def get_length(self):
        cur = self._head
        count = 0
        while cur != None:
            count = count+1
            cur = cur.next
        return cur

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    #表明在头部插入元素
    def add(self,item):
        #注意这是一个双向链表，因此指针也是双向的
        #在头部插入元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    #表明在尾部插入元素
    def append(self):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    #查找元素是否存在
    def search(self,item):
        cur = self._head
        while cur.next != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self,item,pos):
        if pos <= 0:
            self.add(item)
        elif pos > (self.get_length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    #删除要删除的节点
    def remove(self,item):
        if self.is_empty():
            return
        else:
            cur = self._head
            #如果首节点就是要删除的节点的话
            if cur.item == item:
                #分情况讨论，如果链表只有这一个节点
                if cur.next == None:
                    self._head = None
                #如果链表还有别的节点
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            #如果要删除的节点在别的位置
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next




