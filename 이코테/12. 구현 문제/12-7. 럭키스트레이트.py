# 푼 횟수 : v
inputs = '7755'
middle_idx = len(inputs)//2

if sum(map(int,list(inputs[:middle_idx]))) == sum(map(int,list(inputs[middle_idx:]))):
    print("LUCKY")
else:
    print("READY")