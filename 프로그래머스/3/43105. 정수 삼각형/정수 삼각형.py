def solution(triangle):
    sum_list = []
    for i in range(len(triangle)):
        temp = []
        for j in range(len(triangle[i])):
            if i == 0:
                prev_num = 0
            else:
                if j == 0:
                    prev_num = sum_list[i-1][j]
                elif j == i:
                    prev_num = sum_list[i-1][j-1]
                else:
                    prev_num = max(sum_list[i-1][j-1], sum_list[i-1][j])
            temp.append(triangle[i][j] + prev_num)
        sum_list.append(temp)
    return max(temp)