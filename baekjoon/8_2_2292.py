n = int(input())
room = 1
num = 1
num_six = 6

while n > num:
    room += 1
    num += num_six
    num_six += 6
print(room)