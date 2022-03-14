new_id = 'b'
    new_id_one = new_id.lower() # 1단계
    new_id_list = []
    for i in new_id_one: # 2단계
        if i.isalpha() == True or i.isdecimal() == True or i == '-' or i == '_' or i == '.' :
            new_id_list.append(i)
        else:
            continue
    new_id_two = ''.join(new_id_list)
    new_id_list_two = []
    if len(new_id_two) > 1:
        for i in range(len(new_id_two)-1): # 3단계
            if new_id_two[i] == '.' and new_id_two[i+1] == '.':
                continue
            else:
                new_id_list_two.append(new_id_two[i])
        if len(new_id_two)>1:
            if new_id_two[-2] == '.' and new_id_two[-1] == '.':
                pass
            else:
                new_id_list_two.append(new_id_two[-1])
    elif len(new_id_two) == 1:
        new_id_list_two.append(new_id_two[0])

    new_id_three = ''.join(new_id_list_two)
    # 4단계
    new_id_four = new_id_three.strip('.')
    # 5단계
    if len(new_id_four) == 0:
        new_id_five = 'a'
    else:
        new_id_five = new_id_four
    # 6단계
    new_id_six = []
    if len(new_id_five) > 15:
        for i in range(15):
            new_id_six.append(new_id_five[i])
        if new_id_six[len(new_id_six)-1] == '.':
            new_id_seven = []
            for i in range(len(new_id_six)-1):
                new_id_seven.append(new_id_six[i])
            new_id_six = new_id_seven
    # 7단계
    elif len(new_id_five) <= 2:
        if len(new_id_five) == 1:
            new_id_six.append(new_id_five[0])
            new_id_six.append(new_id_five[0])
            new_id_six.append(new_id_five[0])
        else:
            new_id_six.append(new_id_five[0])
            new_id_six.append(new_id_five[1])
            new_id_six.append(new_id_five[1])

    else:
        for i in range(len(new_id_five)):
            new_id_six.append(new_id_five[i])
    print(''.join(new_id_six))