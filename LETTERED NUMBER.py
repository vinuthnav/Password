n=int(input())
v=input()
v=v.upper()
s=0
for i in range(len(v)):
    if v[i]=='A':
        s+=1
    elif v[i]=='B':
        s+=10
    elif v[i]=='C':
        s+=100
    elif v[i]=='D':
        s+=1000
    elif v[i]=='E':
        s+=10000
    elif v[i]=='F':
        s+=100000
    elif v[i]=='G':
        s+=1000000
    else:
        s+=0
print(s)
        
