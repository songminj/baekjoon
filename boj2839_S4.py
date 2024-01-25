# 2839 설탕 

sugar = int(input())
sugar_3 = 0
sugar_5, remain = divmod(sugar)


if remain % 3 == 0 :
    sugar_3 = remain // 3
else :
    while remain % 3 != 0:
        remain += 5
        sugar_3 = remain // 3
        sugar_5 -= 1

        if 
    pass

print(sugar_3+sugar_5)