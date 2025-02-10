import os
os.chdir("C:/Users/omoni/OneDrive/Desktop/OMPR")
l=os.listdir()
d={}
totalwords=[]
for i in l:
    f=open(i,"r")
    q=f.read().lower()
    q=q.split()
    for x in q:
        if(not(x.isalnum())):
            p=list(x).copy()
            for t in x:
                if(not t.isalnum()):
                    p.remove(t)
                    flag=0
            if(flag==0):
                q[q.index(x)]=''.join(p)
    s=sorted(list(set(((q)))))
    totalwords+=s
    d[i]=s
    f.close()
totalwords=sorted(list(set(totalwords)))
w=[]
dic={}
for x in totalwords:
    dic[x]=[]
    for y in d:
        if(x in d[y]):
            dic[x].append(y)
for i in dic:
    print(i,':','->'.join(dic[i]))

def finding(x):
    if x not in dic:
        return []
    return dic[x]
'''def subs(g):
    d=[]
    for x in totalwords:
        if(g in x):
            d+=finding(x,dic)
    return d'''


result=[]
print("Searching with the help of Inverted Index!!!")
a=input("Enter a BooleanQuery to search in available Collection:").lower()
a=a.split()
d=[]
result=[]
f=[]
s=[]
top=-1
temp=1
for x in range(0,len(a)):
    if(temp==0):
        temp=1
        continue
    if(a[x] in ['not']):
        f.append(set(l)-set(finding(a[x+1])))
        temp=0
    elif(a[x] not in ["and","or"]):
        f.append(set(finding(a[x])))
    elif(a[x]=='and'):
        top+=1
        s.append('and')
    elif(a[x]=='or'):
        while(top>-1 and s[top]=='and'):
            g=f[len(f)-1]
            h=f[len(f)-2]
            f.remove(g)
            f.remove(h)
            f.append(g.intersection(h))
            top-=1
        top+=1
        s.insert(top,'or')
while(top!=-1):
    g=f[len(f)-1]
    h=f[len(f)-2]
    f.remove(g)
    f.remove(h)
    if(s[top]=='and'):
        f.append(g.intersection(h))
    elif(s[top]=='or'):
        f.append(g.union(h))
    top-=1
if(len(list(f[0]))==0):
    print("No Related Documents found!!!");
else:
    print("Related documents for given query are:",end=' ')
    for x in f:
        for y in sorted(list(x)):
            print(y,end=' ')

