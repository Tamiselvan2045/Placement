L=[]
N=int(input())
for i in range(N):
    c=input().split()
    i+=1
    if c[0]=="insert":
        L.insert(int(c[1]),int(c[2]))
    elif c[0]=="pop":
        L.pop()
    elif c[0]=="append":
        L.append(int(c[1]))
    elif c[0]=="remove":
        L.remove(int(c[1]))
    elif c[0]=="sort":
        L.sort()
    elif c[0]=="reverse":
        L.reverse()
    elif c[0]=="print":
        print(L)

        
