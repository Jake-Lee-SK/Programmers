import itertools

numbers = [1,2,3, 0]

num_list = []
for i in numbers:
    num_list.append(i)

tmp = list(itertools.permutations(num_list, len(numbers)))

tmp2 = []
for i in tmp:
    if i[0] != 0:
        tmp2.append(i)

for i in tmp2:
    
print(tmp2)