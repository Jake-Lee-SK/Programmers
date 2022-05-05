record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = []
hash = {}
for re in record:
    re = re.split()
    # enter 혹은 change
    if len(re)==3 and re[0] == "Enter":
        hash[re[1]] = re[2]
    elif len(re)==3 and re[0] == "Change":
        hash[re[1]] = re[2]

for re in record:
    re = re.split()
    # leave
    if len(re) == 2:
        answer.append(f'{hash.get(re[1])}님이 나갔습니다.')
    # enter 혹은 change
    else:
        if re[0] == "Enter":
            answer.append(f'{hash.get(re[1])}님이 들어왔습니다.')
print(answer)