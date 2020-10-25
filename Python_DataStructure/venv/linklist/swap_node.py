class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        print("print linkedlist")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def insert(self,item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def swapNodes(self,d1,d2):
        prevD1 = None
        prevD2 = None
        #假设这两个
        if d1 == d2:
            return
        else:
            D1 = self.head
            while D1 is not None and D1.data != d1:
                prevD1 = D1
                D1 = D1.next
            D2 = self.head
            while D2 is not None and D2.data != d2:
                prevD2 = D2
                D2 = D2.next
            if D1 is None and D2 is None:
                return
            if prevD1 is not None:
                prevD1.next = D2
            else:
                self.head = D2
            if prevD2 is not None:
                prevD2.next = D1
            else:
                self.head = D1
            temp = D1.next
            D1.next = D2.next
            D2.next = temp

if __name__ == '__main__':
    list = LinkedList()
    list.insert(5)
    list.insert(4)
    list.insert(3)
    list.insert(2)
    list.insert(1)
    list.print_list()
    list.swapNodes(1,4)
    print("after swapping")
    list.print_list()





