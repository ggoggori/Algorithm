def solution(sample):
    answer, id_dict = [], {}

    for msg in sample[::-1]:
        if 'Leave' in msg:
            continue
        msg = msg.split(' ')
        if id_dict.get(msg[1]) is None:
            id_dict[msg[1]] = msg[2]

    for msg in sample:
        msg = msg.split(' ')
        if msg[0] == 'Enter':
            answer.append(f"{id_dict[msg[1]]}님이 들어왔습니다.")
        elif msg[0] == 'Leave':
            answer.append(f"{id_dict[msg[1]]}님이 나갔습니다.")

    return answer