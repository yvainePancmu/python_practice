class HashTable:
    def __init__(self, size):
        # 使用list数据结构作为哈希表元素保存方法
        self.elem = [None for i in range(size)]
        self.count = size  # 最大表长

    def hash(self, key):
        # 散列函数采用除留余数法
        return key % self.count

    def insert_hash(self, key):
        # 插入关键字到哈希表内
        address = self.hash(key)  # 求散列地址
        # 当前位置已经有数据了，发生冲突。
        while self.elem[address]:
            # 线性探测下一地址是否可用
            address = (address+1) % self.count
        # 没有冲突则直接保存。
        self.elem[address] = key

    def search_hash(self, key):
        # 查找关键字，返回布尔值
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            # 说明没找到或者循环到了开始的位置
            if not self.elem[address] or address == star:
                return False
        return True, address  # 返回索引值


if __name__ == '__main__':
    list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(12)
    for i in list_a:
        hash_table.insert_hash(i)
    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)), end=" ")
    print("\n")
    print(hash_table.search_hash(15))
    print(hash_table.search_hash(33))
