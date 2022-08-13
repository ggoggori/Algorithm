array = [1, 2, 3, 4, 5, 6, 6, 7, 8]


def binary_search(array, target, start, end):
    if (
        start > end
    ):  # start == end인 조건에서는 binary search가 더 진행될 여지가 있음. start==end 라면 start==end==mid이기 때문에!!
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)


idx = binary_search(array, 4, 0, len(array) - 1)
print("idx =", idx)

