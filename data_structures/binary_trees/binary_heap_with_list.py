class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def pear_up(self, i):
        while i // 2:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, k):
        self.heap_list.append(k)
        self.size += 1
        self.pear_up(self.size)

    def del_root(self):
        root_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.pear_down(1)
        return root_val

    def pear_down(self, i):
        # 还有子节点
        while 2*i <= self.size:
            index = self.min_child(i)
            if self.heap_list[i] > self.heap_list[index]:
                self.heap_list[i], self.heap_list[index] = self.heap_list[index], self.heap_list[i]
            i = index

    def min_child(self, i):
        if (2*i + 1) > self.size:
            return 2*i
        return 2*i if self.heap_list[2*i] < self.heap_list[2*i+1] else (2*i + 1)

    def build_heap(self, src_list):
        i = len(src_list) // 2
        self.size = len(src_list)
        self.heap_list = [0] + src_list
        while i > 0:
            self.pear_down(i)
            i -= 1


def main():
    # l = [9, 6, 5, 2, 3]
    # b = BinaryHeap()
    # b.build_heap(l)
    # print(b.heap_list)
    lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
    count = 0
    print(len(lst))
    for item in lst:
        count += 1
        if item == 0:
            lst.remove(item)
    print(count, lst)


if __name__ == '__main__':
    main()
