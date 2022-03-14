import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    id_list = input().split(sep='"')
    report = input().split(sep='"')
    k = int(input())
    report_case = [0]*(len(id_list)//2)
    do_not_twice = [[None]*(len(id_list)//2) for _ in range(len(id_list)//2)]
    numbering = {}
    for i in range(len(id_list)//2):
        numbering[id_list[2*i+1]] = i
    for i in range(len(report)//2):
        a = report[2*i+1].split()
        if do_not_twice[numbering.get(a[0])][numbering.get(a[1])] != True: # 한번 신고하면 신고 횟수가 안 늘어남.
            do_not_twice[numbering.get(a[0])][numbering.get(a[1])] = True
            report_case[numbering.get(a[1])] += 1
        else:
            continue
    get_mail = [0]*(len(id_list)//2)
    for i in range(len(id_list)//2):
        if report_case[i] >= k: # i번째 사람이 report 횟수가 일정 횟수를 넘었다면
            for j in range(len(id_list)//2):
                if do_not_twice[numbering.get(id_list[2*j+1])][numbering.get(id_list[2*i+1])] == True:
                    get_mail[j] += 1
    print(get_mail)