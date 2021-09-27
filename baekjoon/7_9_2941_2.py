n=input()
m=len(n)
for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    m -= n.count(i)
print(m)