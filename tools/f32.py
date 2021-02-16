#!/usr/bin/python3

import sys
#This program converts a number to a binary32 float to insert into assembly source code

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
    return [255, 255, 255, 127]

  x=float(x)
  if x == 0:
    return [0, 0, 0, 0]
  sign = 0
  if x < 0:
    sign = 128
    x =- x
  if x == float('inf'):
    return [0, 0, 128, 127+sign]

  exp=0
  while x<1:
    exp -= 1
    x += x

  while x>=2:
    exp += 1
    x /= 2

  if exp > 127:
    return [0, 0, 128, 127+sign]

  if exp < -126:
    return [0, 0, 0, 0]  #zero

  exp += 127
  l = [(exp >> 1) + sign]
  x -= 1
  x += exp&1
  x /= 2
  x*=256
  for k in range(n-1):
    a = int(x)
    x-= a
    l = [a] + l
    x*= 256
  #rounding
  x+=.5
  l=[int(x)]+l
  k=0
  while (k<n) and (l[k]==256):
    l[k] = 0
    k += 1
    l[k] += 1
  return l
for i in sys.argv[1:]:
  print(dbify(tofloat(i))+"  ;"+i)
