def selection_sort(nums):
    print('*'*30)
    print(nums)
    for i in range(len(nums)):
        index = i
        for j in range(i+1, len(nums)):
            if nums[index] > nums[j]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
        print(nums)
    print('*'*30)


def main():
    args = [
        [1, 5, 3, 2, 7, 4, 9, 0],
        [3, 1, 5, 2, 6],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    for arg in args:
        selection_sort(arg)
        print(arg)


if __name__ == '__main__':
    main()
