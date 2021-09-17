s = input().lower()         # 소문자
s_list = list(set(s))       # 문자열 중복제거
cnt_list = []

for i in s_list:            # 중복제거한 문자열이 리스트 s에서
    cnt = s.count(i)        # 각각 몇 번 나오는지 count
    cnt_list.append(cnt)    # 각 문자의 count 값 리스트에 따로 저장 -> 가장 많이 사용된 문자 찾기 위해

if cnt_list.count(max(cnt_list)) > 1:   # 가장 많이 사용된 문자가 2개 이상일 때
    print("?")
else:
    print(s_list[(cnt_list.index(max(cnt_list)))].upper())      # 가장 많이 사용된 문자의 인덱스 값 = 중복제거한 리스트의 인덱스 값 -> 해당 문자열 대문자로 출력