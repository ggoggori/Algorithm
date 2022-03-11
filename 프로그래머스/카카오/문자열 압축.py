def convert_str(context, num):
    prev_char, answer_list, count = None, [], 1

    for idx in range(0, len(context),num):
        char = context[idx:idx+num]
        try:
            next_char = context[idx+num:idx+num*2]
        except:
            next_char = None
            
        if char == prev_char:
            count += 1
            if char != next_char:
                answer_list.append(str(count) + prev_char)
                count = 1
        else:
            if char != next_char:
                answer_list.append(char)
                
        prev_char = char
            
    return ''.join(answer_list)

def solution(context):
    answer = []
    if len(context)==1:
        return 1
    
    for length in range(1,int(len(context)/2)+1):
        answer.append(len(convert_str(context, length)))
        
    return min(answer)