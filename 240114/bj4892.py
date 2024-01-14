num = 1

while True :
  n0 = int(input())

  if n0 == 0:
    break
  elif n0 % 2 == 1 :
    print(f'{num}. odd {int(3*(3*n0+1)/2) // 9}')
  else :
    print(f'{num}. even {int(9*n0/2) // 9}')
  num = num + 1