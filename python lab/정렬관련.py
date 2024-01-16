count = int(input())
answer = []

for i in range(count):
    answer.append(input())

# short_len_sort = answer.sort(key = len)
# short_len = sorted(answer, key = len)      # 짧은 순 정렬 ok -> but, 사전 순 정렬 x

# set_short_len = set(short_len)

# result = sorted(set_short_len)

set_answer = set(answer)
sorted_answer = sorted(set_answer)
result = sorted(sorted_answer, key = len)   

print("=====================================")

for j in result:
    print(j)