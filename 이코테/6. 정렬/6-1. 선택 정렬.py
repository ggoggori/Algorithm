array = [7, 6, 2, 3, 1, 0, 5, 9, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):  # i+1 부터 마지막까지 중 가장 작은 index를 찾음.
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # i번째 요소와의 스와핑
