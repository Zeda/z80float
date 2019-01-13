#Written by Zeda Thomas
#Based on the paper of B.C. Carlson (http://www.ams.org/journals/mcom/1972-26-118/S0025-5718-1972-0307438-2/S0025-5718-1972-0307438-2.pdf)
#Included is some example usage, as well as the useful `bgcoef` function, used to generate coefficients for fixed-iteration implementations.
#current example usage:
#   python bgc.py 3

import sys
def atan(x):
  x=float(x)
  return x/bgc(1.0,(1+x*x)**.5)
def log(x):
  x=float(x)
  return (x-1)/bgc((1+x)/2,x**.5)
def asin(x):
  x=float(x)
  return x/bgc((1-x*x)**.5,1.0)
def acos(x):
  x=float(x)
  return (1-x*x)**.5/bgc(x,1.0)
def atanh(x):
  x=float(x)
  return x/bgc(1.0,(1-x*x)**.5)
def asinh(x):
  x=float(x)
  return x/bgc((1+x*x)**.5,1.0)
def acosh(x):
  x=float(x)
  return (x*x-1)**.5/bgc(x,1.0)
def bgc(a,g):
  d=[a]
  c=0
  n=0
  while abs(c-d[0])>2**-50:
    c=d[0]
    n+=1
    a=(a+g)/2
    g=(a*g)**.5
    d+=[a]
    b=1
    for k in range(n):
      b*=4
      d[n-k-1]=(b*d[n-k]-d[n-k-1])/(b-1)
  return d[0]
def bgci(a,g):
  l=[a]
  for i in range(4):
    a=.5*(a+g)
    g=(a*g)**.5
    l+=[a]
  return 722925/(1048576*l[4]-348160*l[3]+22848*l[2]-340*l[1]+l[0])
def bgc6(a,g):
  a0=a
  a=.5*(a+g)
  a1=a*4
  g=(a*g)**.5
  a=.5*(a+g)
  a2=a*64
  g=(a*g)**.5
  a=.5*(a+g)
  a3=a*(1<<12)*85
  g=(a*g)**.5
  a=.5*(a+g)
  a4=a*(1<<20)
  g=(a*g)**.5
  a=.5*(a+g)
  a5=a*(1<<30)
  g=(a*g)**.5
  a=.5*(a+g)
  a*=(1<<42)

  b=(a5+a1)*105
  e=(a4+a2)*21
  f=(e-a3)*11*31
  z=(f-b)*13+a+a0
  #print(z)
  return z/3028466566125
def bgcoef(n):
  #Returns of [d,[c0,c1,c2,...,c_n]], where the B-G algorithm limit is approximated by (c0*a0+c1*a1+...+c_n*a_n)/d
  l=[1]
  c=1
  k=1
  d=1
  while k<=n:
    c*=4
    d*=(c-1)
    l+=[0]
    l=[c*l[0]]+[c*l[i]-l[i-1] for i in range(1,k+1)]
    k+=1
  return [d,l[::-1]]
#print(log(2))
#print(atan(1))
#print(asin(.7))
#print(1/bgci(3,4))
#print(bgc(3.0,4.0))
#print(1/bgc6(3.14159265358979,2.718281828))
#print(1/bgc6(.5*(1+3.14159265358979),3.14159265358979**.5))
print(bgcoef(int(sys.argv[1])))
