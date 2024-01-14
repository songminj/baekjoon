from sys import stdin

test_num = int(stdin.readline())
for i in range(test_num):
  a, b = map(int, stdin.readline().strip().split())
  print(a+b)