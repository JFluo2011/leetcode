from random import randint
import time


class EmptyError(Exception):
    pass


def gen_random_numbers(count, s, e):
    return [randint(s, e) for _ in range(count)]


def gen_reverse_order_numbers(count):
    return [_ for _ in range(count, 0, -1)]


def gen_nearly_order_numbers(count, swap_times):
    nums = [_ for _ in range(1, count+1)]
    for _ in range(swap_times):
        i = randint(0, count-1)
        j = randint(0, count-1)
        nums[i], nums[j] = nums[j], nums[i]

    return nums


def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True


def time_cal(func):
    def decorator(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} time cost: {time.time() - start}')
        return result
    return decorator


def sort_nums(args_lst, length):
    for func, nums in args_lst:
        nums = func(nums)
        assert len(nums) == length
        assert is_sorted(nums)