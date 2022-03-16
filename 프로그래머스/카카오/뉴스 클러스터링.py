import re

def get_bigram(string):
    bigram_list = []
    for idx, _ in enumerate(string):
        if idx+1 == len(string):
            break
        bigram = string[idx]+string[idx+1]
        if len(re.findall('[a-zA-Z]', bigram))==2:
            bigram_list.append(bigram.upper())
    return bigram_list

def get_intersect(set1, set2):
    intersect = []
    for element in set1:
        if element in set2:
            set2.remove(element)
            intersect.append(element)
    return intersect

def get_union(set1, set2, intersect):
    set1.extend(set2)
    for element in intersect:
        if set1.count(element)!=0:
            del set1[set1.index(element)]

    return set1

def solution(str1, str2):
    set1 = get_bigram(str1)
    set2 = get_bigram(str2)
    if len(set1)==0 and len(set2)==0:
        return 65536
    intersect = get_intersect(set1.copy(), set2.copy())
    union = get_union(set1.copy(), set2.copy(), intersect)

    answer = int((len(intersect) / len(union)) * 65536)

    return answer

# 다른사람 풀이 보니까 합집합, 교집합 연산을 간단하게 했음.
# 문제를 보고 해당 기능을 구현하려고 노력한 것은 좋은 시도였으나, 그 안에서도 더 간단하고 효율적인 방법을 고민할 필요가 있을 것 같다.