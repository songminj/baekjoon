num = int(input())

def factorial(n):
  if n <= 1 :
    return 1
  return n * factorial(n-1)

for i in range(num):
  a, b = map(int, input().split())
  bHa = factorial(b) // (factorial(a)*factorial(b-a))
  print(bHa)