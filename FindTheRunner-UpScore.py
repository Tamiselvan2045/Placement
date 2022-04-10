n=int(input())
assert 2<=n<=10
num=list(map(int,input().split()))
assert max(num)<=100
assert min(num)>=-100
m=max(num)
while m==max(num):
    num.remove(max(num))
print(max(num))
