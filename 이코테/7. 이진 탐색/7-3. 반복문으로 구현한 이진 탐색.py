array = [1,2,3,2,5,3,3,4,5,6,6,7,8]

def binary_search(array, target, start, end):
    while start < end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

idx = binary_search(array, 4, 0, len(array)-1)
print('idx =',idx)