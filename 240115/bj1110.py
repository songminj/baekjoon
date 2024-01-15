n = int(input())
num = n
cycle_num, total = 0, 0

while True:
    il = (num // 10 + num % 10) % 10 
    sib = num % 10 
    num = sib*10 +il
    total += 1

    if num == n :
        break

print(total)