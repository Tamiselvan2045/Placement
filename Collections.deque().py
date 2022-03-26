import collections
n=int(input())
l1=[]
for i in range(n):
    d=list(map(str,input().split()))
    if d[0]=="append":
        l1.append(d[1])
    elif d[0]=="pop":
        l1.pop()
    elif d[0]=="appendleft":
        l1.insert(0,d[1])
    elif d[0]=="popleft":
        l1.pop(0)
s=collections.deque(l1)
for i in s:
    print(i,end=" ")
