"""
이진 탐색으로 해결
global 변수인 result를 선언하고, M만큼의 떡길이를 얻을 때마다, result를 갱신해줌.
이진탐색이 종료되면, result에는 M만큼의 길이를 얻기 위해 최대한으로 자를 수 있는 떡의 길이가 담긴다.
"""

n, m = list(map(int, input().split(" ")))
array = list(map(int, input().split()))

result = None


def binary_search(array, start, end, target):
    global result
    if start > end:
        return None
    mid = (start + end) // 2
    sums = sum([i - mid for i in array if i - mid > 0])
    if target >= sums:
        result = mid
        return binary_search(array, start, mid - 1, target)

    elif target < sums:
        return binary_search(array, mid + 1, end, target)


binary_search(array, 0, max(array), m)

###########################################################################################
# 처음풀이
# 문제에서 1억까지 높이가 주어진다고 했기 때문에 순차탐색과 같이 이딴 식으로 풀면 시간초과임.

# n, m = 4, 6
# array = [19,15,10,17]

# for i in range(max(array),0,-1):
#     if m == sum([0 if j<=i else j-i for j in array]):
#         print(i)
