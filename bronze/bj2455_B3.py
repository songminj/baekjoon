on = []
pop = 0

for _ in range(4):
    a, b = map(int, input().split())
    pop += b-a    
    on.append(pop)
print(max(on))