from itertools import combinations
from collections import Counter

def solution(orders, courses):
    answer = []
    
    for course in courses:
        tar = []
        for order in orders:
            tar.extend(list(combinations(''.join(sorted(order)), course)))
        cnt = Counter(tar)
        if len(cnt.values()) !=0: max_val=max(cnt.values())
        answer.extend([''.join(key) for key, value in cnt.items() if value >= 2 and value == max_val])
    answer = sorted(answer)
    
    return answer