# BOJ 1181. 단어 정렬 

# # 필요한 변수 선언
# word_set = set()
# num = int(input())

# # Set에 담가서 중복된 단어를 제거 
# for i in range(num):
#   word = str(input())
#   word_set.add(word)

# # 순서가 있는 시퀀스를 만들기 위해 list에 담음
# word_list = list(word_set)
# word_list = sorted(word_list)
# word_list = sorted(word_list, key = len)

# for word in word_list:
#   print(word)

# 방법 2 
# 필요한 변수 선언
word_set = set()
num = int(input())
sort_list = []

# Set에 담가서 중복된 단어를 제거 
for i in range(num):
  word = str(input())
  word_set.add(word)

#(len(word), word) 를 리스트에 담아줄 것
word_list = list(word_set)
for word in word_list:
  sort_list.append((len(word), word))

# len(word) 기준으로 먼저 sort 하고 같을 땐 word 기준으로 sort한다
sort_list.sort()

# 뱉기

for len_word, word in sort_list:
  print(word)

# for sorted_word in sort_list:
#   print(sorted_word[1])