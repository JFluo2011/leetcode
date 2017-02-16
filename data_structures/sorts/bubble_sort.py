def bubble_sort(nums):
    print('*'*30)
    print(nums)
    for i in range(len(nums)):
        flag = True
        for j in range(1, len(nums)-i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                flag = False
        if flag:
            print('i:', i)
            break
        print(nums)
    print('*'*30)


def main():
    args = [
        [1, 5, 3, 2, 7, 4, 9, 0],
        [3, 1, 5, 2, 6],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    for arg in args:
        bubble_sort(arg)
        print(arg)


if __name__ == '__main__':
    main()
