# array에서 n번째부터 m번째까지 숫자를 뽑은 후에
# sort 하고
# sort한 숫자 중 k번째 숫자를 뽑음

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        new_array = array[commands[i][0] - 1:commands[i][1]]
        new_array = sorted(new_array)
        answer.append(new_array[commands[i][2] - 1])
    return answer