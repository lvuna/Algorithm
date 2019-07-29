"""randomized quick sort"""
import random
import time


def randomized_quick_sort(arr: list)-> list:
    if len(arr) == 0:
        return
    new_arr = split(arr)
    arr = new_arr
    return arr


def split(arr: list) -> list:
    if len(arr) == 0 or len(arr) == 1:
        return arr

    index = choose_pivot(arr)
    pivot = arr[index]
    left = []
    right = []
    for i in range(len(arr)):
        if i == index:
            pass
        elif arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left_result = split(left)
    right_result = split(right)
    result = left_result + [pivot] + right_result
    return result


def choose_pivot(arr: list) -> int:
    return random.randint(0, len(arr) - 1)


if __name__ == "__main__":
    lst = []
    for i in range(1000000):
        lst.append(i)
    random.shuffle(lst)

    start = time.time()
    new_lst = randomized_quick_sort(lst)
    end = time.time()
    result_time = end - start
    print(result_time)

    start = time.time()
    lst.sort()
    end = time.time()
    result_time = end - start
    print(result_time)
