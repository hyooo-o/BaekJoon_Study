s = input().lower()
s_list = list(set(s))
cnt_list = []

for i in s_list:
    cnt = s.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(s_list[(cnt_list.index(max(cnt_list)))].upper())