while True :
  a, b = map(int, input().split())
  
  if a == 0 and a == b:
    break  
  elif a > b:
    print('Yes')
  else :
    print('No')