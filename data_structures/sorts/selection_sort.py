from data_structures.helper import time_cal


@time_cal
def selection_sort(nums):
    for i in range(len(nums)):
        k = i
        for j in range(i+1, len(nums)):
            if nums[k] > nums[j]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
    return nums


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
