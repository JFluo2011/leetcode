from data_structures.helper import EmptyError


class HeapMin:
    def __init__(self):
        self._data = [None]

    def size(self):
        return len(self._data) - 1

    def empty(self):
        return self.size() == 0

    def heapify(self, lst):
        self._data[1:] = lst[:]
        n = self.size() // 2
        while n > 0:
            self._shift_down(n)
            n -= 1

    def insert(self, item):
        self._data.append(item)
        self._shift_up(self.size())

    def pop(self):
        if self.size() == 0:
            raise EmptyError('heap is empty')
        self._data[1], self._data[-1] = self._data[-1], self._data[1]
        item = self._data.pop()
        self._shift_down(1)
        return item

    def _shift_down(self, i):
        while 2*i <= self.size():
            j = 2*i
            if ((j + 1) <= self.size()) and (self._data[j+1] < self._data[j]):
                j += 1

            if self._data[i] > self._data[j]:
                self._data[i], self._data[j] = self._data[j], self._data[i]
                i = j
            else:
                break

    def _shift_up(self, i):
        while (i > 1) and (self._data[i//2] > self._data[i]):
            self._data[i // 2], self._data[i] = self._data[i], self._data[i // 2]

            i //= 2


class HeapMax:
    def __init__(self):
        self._data = [None]

    def size(self):
        return len(self._data) - 1

    def empty(self):
        return self.size() == 0

    def heapify(self, lst):
        self._data[1:] = lst[:]
        n = self.size() // 2
        while n > 0:
            self._shift_down(n)
            n -= 1

    def insert(self, item):
        self._data.append(item)
        self._shift_up(self.size())

    def pop(self):
        if self.size() == 0:
            raise EmptyError('heap is empty')
        self._data[1], self._data[-1] = self._data[-1], self._data[1]
        item = self._data.pop()
        self._shift_down(1)
        return item

    def _shift_down(self, i):
        while 2*i <= self.size():
            j = 2*i
            if ((j + 1) <= self.size()) and (self._data[j+1] > self._data[j]):
                j += 1

            if self._data[i] < self._data[j]:
                self._data[i], self._data[j] = self._data[j], self._data[i]
                i = j
            else:
                break

    def _shift_up(self, i):
        while (i > 1) and (self._data[i//2] < self._data[i]):
            self._data[i // 2], self._data[i] = self._data[i], self._data[i // 2]

            i //= 2


def main():
    lst = [41, 30, 28, 22, 16, 13, 19, 15, 52, 17, 62]
    h = HeapMax()
    for item in lst:
        h.insert(item)

    print(lst)
    while not h.empty():
        print(h.pop(), end=' ')
    print('')

    h = HeapMax()
    h.heapify(lst)

    print(lst)
    while not h.empty():
        print(h.pop(), end=' ')


if __name__ == '__main__':
    main()
