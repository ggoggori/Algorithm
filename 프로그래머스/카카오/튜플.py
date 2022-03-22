def solution(s):
    target = s[2:-2].split('},{')
    target = sorted(target, key=lambda x:len(x))
    answer, ana_set = list(), set()
    for nums in target:
        for num in nums.split(','):
            if int(num) not in ana_set:
                answer.append(int(num))
                ana_set.add(int(num))
    return answer