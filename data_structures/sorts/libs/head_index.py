import abc


class IndexHeap(metaclass=abc.ABCMeta):
    def __init__(self):
        self._data = [-1]
        self._indexes = [-1]
        # reverse[i]表示索引i在indexes中的位置
        # reverse[i] = j ==>  indexes[j] = i ==>  (reverse[indexes[i]] = i, indexes[reverse[i]] = i)
        self._reverse = [-1]
        self.count = 0

    def size(self):
        return self.count

    def empty(self):
        return self.count == 0

    def heapify(self, lst):
        self._data[1:] = lst[:]
        self.count = len(lst)
        self._indexes.extend([i for i in range(1, self.count+1)])
        self._reverse.extend([i for i in range(1, self.count+1)])
        n = self.count // 2
        while n > 0:
            self._shift_down(n)
            n -= 1

    def insert(self, item):
        self._data.append(item)
        self.count += 1
        self._indexes.append(self.count)
        self._reverse.append(self.count)
        self._shift_up(self.count)

    def pop(self):
        assert self.count > 0
        self._indexes[1], self._indexes[self.count] = self._indexes[self.count], self._indexes[1]
        # reverse[indexes[i]] = i
        self._reverse[self._indexes[1]] = 1
        self._reverse[self._indexes[self.count]] = self.count
        item = self._data[self._indexes[self.count]]
        self.count -= 1
        self._shift_down(1)
        return item

    def pop_index(self):
        assert self.count > 0
        self._indexes[1], self._indexes[self.count] = self._indexes[self.count], self._indexes[1]
        # reverse[indexes[i]] = i
        self._reverse[self._indexes[1]] = 1
        self._reverse[self._indexes[self.count]] = self.count
        index = self._indexes[self.count] - 1
        self.count -= 1
        self._shift_down(1)
        return index

    def get_item(self, i):
        return self._data[i+1]

    def update(self, i, item):
        assert (0 <= i <= self.count)
        i += 1
        self._data[i] = item
        # k为item在索引数组中的位置
        k = self._reverse[i]
        self._shift_up(k)
        self._shift_down(k)

    @staticmethod
    @abc.abstractmethod
    def _compare(a, b):
        pass

    def _shift_down(self, i):
        while 2*i <= self.count:
            j = 2*i
            if ((j + 1) <= self.count) and self._compare(self._data[self._indexes[j+1]], self._data[self._indexes[j]]):
                j += 1

            if self._compare(self._data[self._indexes[j]], self._data[self._indexes[i]]):
                self._indexes[i], self._indexes[j] = self._indexes[j], self._indexes[i]
                # reverse[indexes[i]] = i
                self._reverse[self._indexes[i]] = i
                self._reverse[self._indexes[j]] = j
                i = j
            else:
                break

    def _shift_up(self, i):
        while (i > 1) and self._compare(self._data[self._indexes[i]], self._data[self._indexes[i//2]]):
            self._indexes[i // 2], self._indexes[i] = self._indexes[i], self._indexes[i // 2]
            # reverse[indexes[i]] = i
            self._reverse[self._indexes[i // 2]] = i // 2
            self._reverse[self._indexes[i]] = i

            i //= 2


class IndexMinHeap(IndexHeap):
    @staticmethod
    def _compare(a, b):
        return a < b


class IndexMaxHeap(IndexHeap):
    @staticmethod
    def _compare(a, b):
        return a > b


def main():
    lst = [41, 30, 28, 22, 16, 13, 19, 15, 52, 17, 62]
    h = IndexMaxHeap()
    for item in lst:
        h.insert(item)
    print(lst)
    print(h.get_item(5))
    h.update(4, 53)
    while not h.empty():
        print(h.pop(), end=' ')
    print('')

    h = IndexMaxHeap()
    h.heapify(lst)
    print(lst)
    print(h.get_item(9))
    h.update(9, 70)
    while not h.empty():
        print(h.pop(), end=' ')


if __name__ == '__main__':
    main()
