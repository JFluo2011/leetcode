def insert_sort(nums):
    print('*'*30)
    print(nums)
    for i in range(1, len(nums)):
        index, temp = i, nums[i]
        for j in range(i - 1, -1, -1):
            if temp < nums[j]:
                nums[j+1], index = nums[j], j
            else:
                break
        nums[index] = temp
        print(nums)
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
