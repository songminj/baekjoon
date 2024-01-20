h1, m1, s1 = map(int, input().split(sep=':'))
h2, m2, s2 = map(int, input().split(sep=':'))


now = s1 + m1*60 + h1*60*60
mission = s2 + m2*60 + h2*60*60

if mission < now :
  left_time = 60*60*24 + mission - now
else : 
  left_time = mission -now

left = {}
left['sec'] = left_time % 60 
left['min'] = (left_time // 60) % 60
left['hour'] = (left_time // 60) // 60

for time in left:
  if left[time] < 10 :
    left[time] = '0'+str(left[time])

print(f'{left["hour"]}:{left["min"]}:{left["sec"]}')