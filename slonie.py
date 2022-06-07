#!/usr/bin/env python
n=int(input())
m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
p=[0]*(n+1);
odw= [False] * (n + 1)
minweight=min(m)
w=0
for i in range(n):
    p[b[i]]=a[i]
for i in range(n):
    if not odw[i]:
        c = 0
        suma = 0
        x = i
        minc=float('inf')
        while True:
            c += 1
            suma = suma + m[x-1]
            minc=min(m[x-1],minc)
            odw[x] = True
            x=p[x]
            if x==i:
                break
        metoda1= suma + (c - 2) * minc
        metoda2= suma + minc + (c + 1) * minweight
        w = w + min(metoda1, metoda2)

print(w)







