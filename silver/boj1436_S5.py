# 1436

"""
브루트포스 알고리즘
: 완전탐색 알고리즘의 유형으로 가능한 모든 경우의 수를 조합하는 알고리즘이다
이 문제의 경우에는 666부터 하나싹 숫자를 올려가면서 666이 숫자 안에 있는지 확인하고
만약에 있으면 count를 해주고, 아니면 그냥 넘겨준다. 

"""
num = int(input())

name = 666
cnt = 0

while True:
  if '666' in str(name):
    cnt += 1
  
  if cnt == num :
    break

  name += 1

print(name)