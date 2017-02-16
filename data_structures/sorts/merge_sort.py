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


if __name__ == '__main__':
    main()
