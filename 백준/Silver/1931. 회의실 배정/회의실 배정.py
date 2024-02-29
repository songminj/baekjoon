
# 회의실배정
import sys

n = int(sys.stdin.readline())

conv = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

conv.sort(key= lambda x : (x[1], x[0]))
# print(conv)
cnt, e = 1, conv[0][1]
for i in range(1, n):
    if conv[i][0] >= e:
        e = conv[i][1]
        cnt += 1
print(cnt)