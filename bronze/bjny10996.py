num = int(input())

if num == 1 :
    print('*')
else :
    for i in range(1, 2*num+1):
        if num % 2 == 0:
            if i % 2 == 0:
              print(' *'*(int(num/2)))
            else :
              print('* '*(int(num/2)))
        else :
            if i % 2 == 0:
                print(' *'*(round(num/2)-1))
            else :
                print('* '*(round(num/2)))
  