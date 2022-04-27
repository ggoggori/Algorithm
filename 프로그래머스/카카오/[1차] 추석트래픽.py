def solution(lines):
    times = []
    total_times = []
    for item in lines: # sec으로 단위를 바꿔주고, total_times에 요청시간, 요청 마감시간을 넣음.
        time = item.split(' ')[1]
        hour, minute, second = time.split(':')
        time = int(hour) * 3600 + int(minute) * 60 + float(second)

        using_sec = float(item.split(' ')[2].split('s')[0])
        start = time - using_sec + 0.001
        times.append([start, time])
        total_times.append(start)
        total_times.append(time)
        
    max_count = 0
    for i in range(len(total_times)):
        count = 0
        time = total_times[i]
        time_plus = round(time + 0.999, 3)

        for j in range(len(times)):
            start, end = times[j]

            if (time <= start <= time_plus) or (time <= end <= time_plus) or (start <= time and time <= end):
                # 기준 시간 + 1초 안에 요청이 겹치는 경우는 요청시간 또는 요청 마감시간이 t 범위 안에 있을 때
                # 요청시간과 요청 마감시간이  t범위를 감싸고 있을 때 총 3가지임.
                count += 1

        max_count = max(max_count, count)
    
    return max_count