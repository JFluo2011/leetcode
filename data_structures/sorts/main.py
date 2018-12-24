from copy import deepcopy

from data_structures.helper import gen_random_numbers, gen_nearly_order_numbers, sort_nums, gen_reverse_order_numbers
from data_structures.sorts.merge_sort import merge_sort, merge_sort_with_iterative
from data_structures.sorts.selection_sort import selection_sort
from data_structures.sorts.insert_sort import insert_sort
from data_structures.sorts.heap_sort import heap_sort1, heap_sort2


def main():
    n = 50000
    swap_times = 10
    # sort_func_lst = [selection_sort, insert_sort, merge_sort]
    # sort_func_lst = [insert_sort, merge_sort]
    sort_func_lst = [merge_sort_with_iterative, merge_sort, heap_sort1, heap_sort2]
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
