#!/usr/bin/python
import sys
#This program converts a number to a single-precision float to insert into assembly source code
def dbify(l):
  s='.db $'
  for i in l:
    t=hex(i)[2:].upper()
    if len(t)==1:
      t='0'+t
    s+=t[-2:]+",$"
  return s[0:-2]

def tofloat(x,n=3):
  if x.lower() == "nan":
    return [0,0,32,0]
  x=float(x)
  if x==0:
    return [0,0,0,0]
  sign=0
  if x<0:
    sign=1
    x=-x
  if x==float('inf'):
    return [255,255,64+(sign<<7),0]

  exp=0
  while x<1:
    exp-=1
    x+=x
  while x>=2:
    exp+=1
    x/=2
  if exp>127:
    return [255,255,64+(sign<<7),0]  #infinity
  if exp<-127:
    return [0,0,0,0]  #zero
  l=[exp+128]
  x+=sign-1
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
  while (k<n-1) and (l[k]==256):
    l[k]=0
    k+=1
    l[k]+=1
  if k!=n-1:
    return l
  if l[k]&127!=0:
    return l
  #Here, we have [0,0,128 or 256,???]
  l[k] -= 128
  l[k+1] += 1
  if l[k+1] == 256:
    l[k] |= 64
    l[k+1] = 0
  return l
for i in sys.argv[1:]:
  print(dbify(tofloat(i))+"  ;"+i)
