from bisect import bisect_left, bisect_right

array1 = [1, 1, 2, 2, 2, 2, 3]
array2 = [1, 1, 2, 2, 2, 2, 3]

target1, target2 = 2, 4


def solution(array, target):
    if len(array) != bisect_left(array, target):
        return bisect_right(array1, target1) - bisect_left(array1, target1)
    else:
        return -1


solution(array1, target1)
solution(array2, target2)
