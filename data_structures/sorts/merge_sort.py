def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    left = merge_sort(nums[:len(nums) // 2])
    right = merge_sort(nums[len(nums) // 2:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_start, right_start = 0, 0
    while (left_start < len(left)) and (right_start < len(right)):
        if left[left_start] < right[right_start]:
            result.append(left[left_start])
            left_start += 1
        else:
            result.append(right[right_start])
            right_start += 1
    result += left[left_start:]
    result += right[right_start:]
    return result


def merge_sort_with_iterative(nums):
    import collections
    result, deque = [], collections.deque((nums[len(nums)//2:], nums[:len(nums)//2]))
    while deque:
        left, right = deque.popleft()
        if len(left) <= 1:
            result += merge(left, right)
        else:
            deque.append((left[len(left)//2:], left[:len(right)//2]))
            deque.append((right[len(right)//2:], right[:len(right)//2]))

    return result


def main():
    args = [
        [1, 5, 3, 2, 7, 4, 9, 0],
        [3, 1, 5, 2, 6],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    for arg in args:
        print(arg)
        result = merge_sort(arg)
        print(result)
        result1 = merge_sort_with_iterative(arg)
        print(result1)


if __name__ == '__main__':
    main()
