from copy import deepcopy
from random import choice

from data_structures.helper import time_cal, gen_random_numbers, gen_reverse_order_numbers, gen_nearly_order_numbers
from data_structures.sorts.merge_sort import merge_sort
from data_structures.sorts.insert_sort import insert_sort
from data_structures.sorts.main import sort_nums


@time_cal
def quick_sort(nums):
    return _quick_sort(nums)


def _quick_sort(nums):
    if not nums:
        return nums

    p = choice(nums)
    l = [e for e in nums if e < p]
    r = [e for e in nums if e > p]
    return _quick_sort(l) + [p]*(len(nums) - len(l) - len(r)) + _quick_sort(r)


def main():
    n = 100000
    swap_times = 10
    sort_func_lst = [quick_sort, merge_sort]
    random_nums_lst = [
        ('random numbers', gen_random_numbers(n, 1, n+1)),
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
