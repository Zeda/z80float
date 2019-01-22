import sys
import mpmath
#This program converts a number to a single-precision float to insert into assembly source code
def dbify(l):
    s='.db $'
    for i in l:
        t=hex(i)[2:].upper()
        if len(t)==1:
            t='0'+t
        s+=t[-2:]+",$"
    return s[0:-2]
def tofloat(x,n=8,bias=16384):
    mpmath.mp.dps=30
    x=mpmath.mpf(x)
    if x==0:
        return [0]*(n+2)
    sign=0
    if x<0:
        sign=1
        x=-x
    exp=0
    while x<1:
        exp-=1
        x+=x
    while x>=2:
        exp+=1
        x/=2
    if exp>16383:
        return [255]*n+[0,sign<<7] #infinity
    if exp<-127:
        return [0]*(n+2)    #zero
    l=[]
    x*=128
    for k in range(n-1):
        a=int(x)
        x-=a
        l=[a]+l
        x*=256
    #rounding
    x+=.5
    l=[int(x)]+l
    k=0
    while k<n-1 and l[k]==256:
        l[k]=0
        k+=1
        l[k]+=1
    if l[k]==256:
        l[k]=0
        exp+=1
        if exp==bias+16384:
            return [255]*n+[0,sign<<7] #infinity
    exp+=bias+(sign<<15)
    return l+[exp&255,exp>>8]
for i in sys.argv[1:]:
    print(dbify(tofloat(i))+"    ;"+i)
