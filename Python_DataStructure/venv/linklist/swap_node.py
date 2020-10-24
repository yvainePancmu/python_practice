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
        prevD1 = d1
        prevD2 = d2
        #假设这两个
        if d1 == d2:
            return
        else:
            D1 =




