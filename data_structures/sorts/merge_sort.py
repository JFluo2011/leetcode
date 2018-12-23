from data_structures.helper import time_cal, gen_random_numbers, gen_nearly_order_numbers, is_sorted


# 自顶向下
@time_cal
def merge_sort(nums):
    return _merge_sort(nums)


def _merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    l = _merge_sort(nums[:mid])
    r = _merge_sort(nums[mid:])
    if l[-1] < r[0]:
        return l + r
    return _merge(l, r)


def _merge(l, r):
    nums = []
    i, j = 0, 0
    while (i < len(l)) and (j < len(r)):
        if l[i] < r[j]:
            nums.append(l[i])
            i += 1
        else:
            nums.append(r[j])
            j += 1
    nums += l[i:]
    nums += r[j:]
    return nums


@time_cal
def merge_sort_with_iterative(nums):
    i, length = 1, len(nums)
    while i < length:
        j = 0
        while j < length:
            nums[j:min(length, j+2*i)] = _merge(nums[j:j+i], nums[j+i: min(length, j+2*i)])
            j += 2*i
        i += i

    return nums


def main():
    nums = gen_random_numbers(10000, 1, 10001)
    nums = merge_sort(nums)
    assert is_sorted(nums)

    nums = gen_nearly_order_numbers(10000, 10)
    nums = merge_sort(nums)
    assert is_sorted(nums)


if __name__ == '__main__':
    main()
