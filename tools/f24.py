#!/usr/bin/python3

import sys
#This program converts a number to a 24-bit float to insert into assembly source code

def dbify(l):
  s='.db $'
  for i in l:
    t=hex(i)[2:].upper()
    if len(t)==1:
      t='0'+t
    s+=t[-2:]+",$"
  return s[0:-2]

def tofloat(x,n=2):
  if x.lower() == "nan":
    return [255,255,127]

  x=float(x)
  if x==0:
    return [0,0,0]
  sign=0
  if x<0:
    sign=1
    x=-x
  if x==float('inf'):
    return [0,0,127+(sign<<7)]

  exp=0
  while x<1:
    exp-=1
    x+=x
  while x>=2:
    exp+=1
    x/=2
  if exp>63:
    return [0,0,127+(sign<<7)]  #infinity
  if exp<-62:
    return [0,0,0]  #zero
  l=[exp+63+(sign<<7)]
  x -= 1
  x*=256
  for k in range(n-1):
    a=int(x)
    x-=a
    l=[a]+l
    x*=256
  #rounding
  x+=.5
  l=[int(x)]+l
  k=0
  while (k<n) and (l[k]==256):
    l[k]=0
    k+=1
    l[k]+=1
  return l
for i in sys.argv[1:]:
  print(dbify(tofloat(i))+"  ;"+i)
