from copy import deepcopy

from data_structures.helper import time_cal, gen_random_numbers, gen_reverse_order_numbers, gen_nearly_order_numbers, sort_nums
from data_structures.sorts.heap import HeapMin


@time_cal
def heap_sort1(nums):
    heap = HeapMin()
    for item in nums:
        heap.insert(item)

    return [heap.pop() for _ in range(len(nums))]


@time_cal
def heap_sort2(nums):
    heap = HeapMin()
    heap.heapify(nums)

    return [heap.pop() for _ in range(len(nums))]


def main():
    n = 50000
    swap_times = 10
    sort_func_lst = [heap_sort1, heap_sort2]
    random_nums_lst = [
        ('random numbers', gen_random_numbers(n, 1, n + 1)),
        ('reverse order numbers', gen_reverse_order_numbers(n)),
        ('nearly order numbers', gen_nearly_order_numbers(n, swap_times)),
        ('repeat numbers', gen_random_numbers(n, 1, 11)),
    ]
    for name, nums in random_nums_lst:
        print(f'nums from {name}')
        print('*' * 40)
        args_lst = [(func, deepcopy(nums)) for func in sort_func_lst]
        sort_nums(args_lst, n)
        print('\n', end='')


if __name__ == '__main__':
    main()
