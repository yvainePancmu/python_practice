class Node(object):

    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)


class Tree(object):
    def __init__(self):
        self.root = Node('root')

    #把节点加进树里面
    def add(self,item):
        #先把item构成节点
        node = Node(item)
        #判断二叉树是否为空
        if self.root is None:
            self.root = item
        else:
            #在列表里添加二叉树的根节点
            q = [self.root]
            while True:
                #表示根节点
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    #找到item的父节点
    def get_parent(self,item):
        if self.root.item == item:
            return None
        temp = [self.root]
        while temp:
            #从上到下
            pop_node = temp.pop(0)
            #如果点的左子树是要找的点的话
            if pop_node.left and pop_node.left.item == item:
                return pop_node
            if pop_node.right and pop_node.right.item == item:
                return pop_node
            if pop_node.left is not None:
                temp.append(pop_node,left)
            if pop_node.right is not None:
                temp.append(pop_node,right)
        return None

    def delete(self,item):
        #如果根为空，就什么都不做
        if self.root is None:
            return False
        parent = self.get_parent(item)
        if parent:
            #确定待删除节点
            del_node = parent.left if parent.left.item == item else parent.right
            #待删除节点的左子树为空
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:
                temp_pre = del_node
                temp_next = del_node.right
                if temp_next.left is None:
                    temp_pre.right = temp_next.right
                    temp_next.left = del_node.left
                    temp_next.right = del_node.right
                else:
                    while temp_next.left:
                        temp_pre = temp_next
                        temp_next = temp_next.left
                    temp_pre.left = temp_next.right
                    temp_next.left = del_node.left
                    temp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = temp_next
                else:
                    parent.right = temp_next
                del del_node
                return True

        else:
            return False



    def inorder(self,node):
        if node is None:
            return []
        result = [node.item]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item+result+right_item

    def postorder(self,node):
        if node is None:
            return []
        result = [node.item]
        left_item = self.postorder(node.left)
        right_item = self.postorder(node.right)
        return left_item+right_item+result

    def preorder(self,node):
        if node is None:
            return []
        result = [node.item]
        left_item = self.preorder(node.left)
        right_item = self.preorder(node.right)
        return result+left_item+right_item


if __name__ == '__main__':
    t = Tree()
    for i in range(1,11):
        t.add(i)
    print('中序遍历',t.inorder(t.root))
    print('前序遍历',t.preorder(t.root))
    print('后序遍历',t.postorder(t.root))





