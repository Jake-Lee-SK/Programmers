clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]


# hash는 말이 hash지 dict 형식을 가리킨다.

hash_map = {}
for cloth, type in clothes:
    hash_map[type] = hash_map.get(type, 0) + 1

# 2. 입지 않는 경우를 추가하여 모든 조합 계산

answer = 1
for type in hash_map:
    answer *= (hash_map[type] + 1)

# 3. 아무 종류의 옷도 입지 않는 경우 제외하기

print(answer - 1)