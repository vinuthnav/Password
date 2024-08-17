def AddDistinctDuplicate(a,b,c,d):
    e=[]
    e.append(a)
    e.append(b)
    e.append(c)
    e.append(d)
    v=[]
    x=0
    s=0
    for i in range(len(e)):
        if e[i] not in v:
            v.append(e[i])
        else:
           x=e[i]
    if x in v:
        v.remove(x)
    for i in range(len(v)):
        s+=v[i]
    return s-(x)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(AddDistinctDuplicate(a,b,c,d))
    
