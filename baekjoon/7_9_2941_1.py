alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in alp:
    a = a.replace(i, '@')

print(len(a))