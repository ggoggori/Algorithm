import re
from itertools import permutations

def solution(exp):
    operator_list = list(permutations(['+','-','*'],3)) # 가능한 우선순위 조합
    result = []
    for operators in operator_list: # 연산자 조합들에서 하나씩 꺼냄
        exp_list = re.split('([+\-*])', exp) #문자열로 구성된 계산 식을 List 형태로 바꿔줌.
        for operator in operators:
            for idx, element in enumerate(exp_list):
                if element == operator: #현재 요소가 연산자라면, 앞뒤 인덱스의 수에 eval을 취해서 연산한다.
                    exp_list[idx-1:idx+2] = [str(eval(exp_list[idx-1] + element + exp_list[idx+1]))]
                    exp_list.insert(0,'') # 연산 후 list에서 요소값이 2개 줄어들기 때문에 index를 맞춰주기 위해 빈요소를 2개 추가
                    exp_list.insert(0,'')
            exp_list = [i for i in exp_list if i != ''] # 빈요소 없애주기

        result.append(abs(int(exp_list[0])))
    return max(result)