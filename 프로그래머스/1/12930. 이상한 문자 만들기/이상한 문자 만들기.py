def solution(s):
    s_lst = list(s)
    idx = 0

    print(s_lst)
    for i in range(len(s_lst)):
        if s_lst[i] == ' ':
            idx = i-1
            continue
        if (i - idx) % 2 == 0:
            s_lst[i] = s_lst[i].upper()
        else:
            s_lst[i] = s_lst[i].lower()
    return ''.join(s_lst)