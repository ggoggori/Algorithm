# 푼 횟수 : v
# 그리디 문제인디 DP 느낌으로 푼듯..?
input = "02984"
# input = '567'

input = list(map(int, list(input)))

for i in range(len(input) - 1):
    input[i + 1] = max(input[i] + input[i + 1], input[i] * input[i + 1])

print(input[-1])
