def solution(N, stages):
    count, answer, result = len(stages) ,[], []
    temp = [0 for _ in range(N+2)] # stage 별로 남아있는 사람의 수를 담기 위한 리스트
                                   # 인덱스를 맞추기 위해 +1, 마지막 스테이지를 달성한 사람을 담기 위해 +1 총 +2
    for stage in stages:
        temp[stage] += 1 # stage별로 남아있는 사람을 센다.

    for idx, t in enumerate(temp[1:-1], 1): #0번째 스테이지와 마지막 스테이지를 제외한 for문
        if count > 0: # 남아있는 사람의 수와 현재 스테이지의 실패자 수로 실패율을 구해준다.
            result.append([t/count,idx])
        else: #마지막 스테이지가 아님에도 모두가 도달하지 못했을 경우
            result.append([0, idx])
        count -= t

    for i in sorted(result, key=lambda x:(x[0],-x[1]), reverse=True): 
        # 리스트에 담아져있는 인덱싱을 이용하여 argsort
        answer.append(i[1])
    
    return answer