word_set = set()
word_len = []
num = int(input())

for i in range(num):
  word = str(input())
  word_set.add(word)

word_list = list(word_set)

for need_count in word_list:
  word_len.append(len(need_count))

for i in range(num):
  print(word_len[i])