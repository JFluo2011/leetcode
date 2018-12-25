import abc


class Heap(metaclass=abc.ABCMeta):
    def __init__(self):
        self._data = [-1]
        self.count = 0

    def size(self):
        return self.count

    def empty(self):
        return self.count == 0

    def heapify(self, lst):
        self._data[1:] = lst[:]
        self.count = len(lst)
        n = self.count // 2
        while n > 0:
            self._shift_down(n)
            n -= 1

    def insert(self, item):
        self._data.append(item)
        self.count += 1
        self._shift_up(self.count)

    def pop(self):
        assert self.count > 0
        self._data[1], self._data[-1] = self._data[-1], self._data[1]
        item = self._data.pop()
        self.count -= 1
        self._shift_down(1)
        return item

    @staticmethod
    @abc.abstractmethod
    def _compare(a, b):
        pass

    def _shift_down(self, i):
        while 2*i <= self.count:
            j = 2*i
            if ((j + 1) <= self.count) and self._compare(self._data[j+1], self._data[j]):
                j += 1

            if self._compare(self._data[j], self._data[i]):
                self._data[i], self._data[j] = self._data[j], self._data[i]
                i = j
            else:
                break

    def _shift_up(self, i):
        while (i > 1) and self._compare(self._data[i], self._data[i//2]):
            self._data[i // 2], self._data[i] = self._data[i], self._data[i // 2]

            i //= 2


class MinHeap(Heap):
    @staticmethod
    def _compare(a, b):
        return a < b


class MaxHeap(Heap):
    @staticmethod
    def _compare(a, b):
        return a > b


def main():
    lst = [41, 30, 28, 22, 16, 13, 19, 15, 52, 17, 62]
    h = MaxHeap()
    for item in lst:
        h.insert(item)

    print(lst)
    while not h.empty():
        print(h.pop(), end=' ')
    print('')

    h = MaxHeap()
    h.heapify(lst)

    print(lst)
    while not h.empty():
        print(h.pop(), end=' ')


if __name__ == '__main__':
    main()
