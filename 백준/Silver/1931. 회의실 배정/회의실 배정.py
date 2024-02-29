
# 회의실배정
import sys

n = int(sys.stdin.readline())

conv = [[] for _ in range(n)]
for i in range(n):
    start, end = map(int, input().split())
    conv[i] = (start, end)
conv.sort(key= lambda x : (x[1], x[0]))
# print(conv)
cnt, e = 0, 0
for i in range(n):
    if conv[i][0] >= e:
        e = conv[i][1]
        cnt += 1
print(cnt)