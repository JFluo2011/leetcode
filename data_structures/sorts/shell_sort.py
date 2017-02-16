def insert_sort(nums):
    print('*'*30)
    print(nums)
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            index, temp = i, nums[i]
            for j in range(i-gap, -1, -gap):
                if temp < nums[j]:
                    nums[j+gap], index = nums[j], j
            nums[index] = temp
        print(nums)
        gap //= 2
    print('*'*30)


def main():
    args = [
        [1, 5, 3, 2, 7, 4, 9, 0],
        [3, 1, 5, 2, 6],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    for arg in args:
        insert_sort(arg)
        print(arg)


if __name__ == '__main__':
    main()
