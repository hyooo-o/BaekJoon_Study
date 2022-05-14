T = int(input())
list1 = [1, 3, 5, 7, 8, 10, 12]
list2 = [4, 6, 9, 11]

for i in range(1, T+1):
    case = list(input())
    year = ''.join(case[:4])
    month = ''.join(case[4:6])
    day = ''.join(case[6:])
    
    if int(month) in list1:
        if 1 > int(day) or int(day) > 31:
            print("#%d" %i, end=' ')
            print("-1")
            continue
    elif int(month) == 2:
        if 1 > int(day) or int(day) > 28:
            print("#%d" %i, end=' ')
            print("-1")
            continue
    elif int(month) in list2:
        if 1 > int(day) or int(day) > 30:
            print("#%d" %i, end=' ')
            print("-1")
            continue
    else:
        print("#%d" %i, end=' ')
        print("-1")
        continue
    print("#%d" %i, end=' ')
    print(year, month, day, sep = '/')