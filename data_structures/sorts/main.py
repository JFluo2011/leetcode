from copy import deepcopy

from data_structures.helper import gen_random_numbers, gen_nearly_order_numbers, is_sorted, gen_reverse_order_numbers
from data_structures.sorts.merge_sort import merge_sort
from data_structures.sorts.selection_sort import selection_sort
from data_structures.sorts.insert_sort import insert_sort


def sort_nums(args_lst):
    for func, nums in args_lst:
        nums = func(nums)
        assert is_sorted(nums)


def main():
    n = 10000
    swap_times = 10
    sort_func_lst = [selection_sort, insert_sort, merge_sort]
    # sort_func_lst = [merge_sort]
    random_nums_lst = [
        ('random numbers', gen_random_numbers(n)),
        ('reverse order numbers', gen_reverse_order_numbers(n)),
        ('nearly order numbers', gen_nearly_order_numbers(n, swap_times)),
    ]
    for name, nums in random_nums_lst:
        print(f'nums from {name}')
        print('*' * 40)
        args_lst = [(func, deepcopy(nums)) for func in sort_func_lst]
        sort_nums(args_lst)
        print('\n', end='')


if __name__ == '__main__':
    main()
