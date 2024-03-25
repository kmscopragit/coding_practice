def solution(num):
    answer = 0
    while num != 1:
        if answer == 501:
            answer = -1
            break
        
        if num%2 == 0:
            num = int(num/2)
            
        else:
            num = 3*num + 1
            
        answer += 1
        
    return answer