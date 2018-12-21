from data_structures.helper import time_cal


@time_cal
def insert_sort(nums):
    for i in range(1, len(nums)):
        k, tmp = i, nums[i]
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                k, nums[k] = j - 1, nums[j]
            else:
                break
        nums[k] = tmp

    return nums


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
