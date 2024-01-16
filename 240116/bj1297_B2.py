d, h, w = map(int, input().split())

k = d / ((w**2 + h**2)**(1/2))
print(int((k*h) // 1) , int((k*w) //1))
print(int(k*h) , int(k*w))
