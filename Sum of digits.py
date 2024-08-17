n=int(input())
a=list(map(int,input().split()))
v=0
u=0
for i in range(n):
    x=str(a[i])
    for j in range(len(x)):
        u+=int((x[j]))
f1=u%10
f2=sum(a)%10
print(f1-f2)
