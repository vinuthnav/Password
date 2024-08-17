n=int(input())
a=list(map(int,input().split()))
x=max(a)
print(x)
for i in range(len(a)):
    if x==a[i]:
        print(i)
