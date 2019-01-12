# The Borchardt-Gauss Algorithm

## Motivation
For this project, we need a reliable way to compute some of the trickier functions like arctangent and the natural logarithm to high precision. It turns out that the Borchardt-Gauss Algorithm is actually a practical, efficient algorithm for the Z80.

## Description
The Borchardt-Gauss algorithm is a simple recurrence related to the Arithmetic-Geometric Mean (AGM). Given *a<sub>0</sub>* and *g<sub>0</sub>*,
*a<sub>n+1</sub>*=(*a<sub>n</sub>*+*g<sub>n</sub>*)/2 and *g<sub>n+1</sub>*=(*a<sub>n+1</sub>* *g<sub>n</sub>*)<sup>1/2</sup>. While these sequences do converge to a common limit *L*, they only gain about 2 bits per iteration, whereas the AGM doubles the digits of precision each iteration. [A paper by B.C. Carlson](http://www.ams.org/journals/mcom/1972-26-118/S0025-5718-1972-0307438-2/S0025-5718-1972-0307438-2.pdf) details a modification that accelerates the B-G algorithm. It adds an auxiliary sequence, with *d*(0,n)=*a<sub>n</sub>* and *d(k>0,n)*=(4<sup>k</sup>*d*(k-1,n)-*d*(k-1,n-1))/(4<sup>k</sup>-1) [modified from the source] and using *d*(n,n) as the output. In practice, *d*(3,3) provides roughly 8 digits of precision, and *d*(6,6) provides roughly 20 digits (more than 64 bits).

## Practical Considerations
The algorithms for computing logarithms and whatnot actually rely on computing 1/*L*, or 1/*d*(n,n) in our case. As well, we don't actually have to compute all of the *d*(k,n) if we are only performing a fixed number of iterations. We will, however, need O(n) space for all of the *a<sub>n</sub>*.

We also don't need to compute the very last *g<sub>n</sub>*, so that removes one square root from the computation.

Here is a little work for avoiding computing all of the *d*(k,n). It isn't
```
d(0,0) = a_0

------------------------------------
d(0,1) = a_1
d(1,1) = (4d(0,1)-d(0,0))/3
       = (4a_1-a_0)/3
------------------------------------
d(0,2) = a_2
d(1,2) = (4d(0,2)-d(0,1))/3
       = (4a_2-a_1)/3
d(2,2) = (16d(1,2)-d(1,1))/15
       = (16*(4a_2-a_1)/3-(4a_1-a_0)/3)/15
       = (64a_2-16a_1-4a_1+a_0)/45
       = (64a_2-20a_1+a_0)/45
------------------------------------
d(0,3) = a_3
d(1,3) = (4d(0,3)-d(0,2))/3
       = (4a_3-a_2)/3
d(2,3) = (16d(1,3)-d(1,2))/15
       = (16*(4a_3-a_2)/3-(4a_2-a_1)/3)/15
       = (64a_3-16a_2-4a_2+a_1)/45
       = (64a_3-20a_2+a_1)/45
d(3,3) = (64d(2,3)-d(2,2))/63
       = (64*(64a_3-20a_2+a_1)/45-(64a_2-20a_1+a_0)/45)/63
       = (4096a_3-1280a_2+64a_1-64a_2+20a_1-a_0)/2835
       = (4096a_3-1344a_2+84a_1-a_0)/2835
------------------------------------
d(0,4) = a_4
d(1,4) = (4d(0,4)-d(0,3))/3
d(2,4) = (16d(1,4)-d(1,3))/15
d(3,4) = (64d(2,4)-d(2,3))/63
       = (4096a_4-1344a_3+84a_2-a_1)/2835
d(4,4) = (256d(3,4)-d(3,3))/255
       = (256(4096a_4-1344a_3+84a_2-a_1) - (4096a_3-1344a_2+84a_1-a_0))/722925
       = (1048576a_4-348160a_3+22848a_2-340a_1+a_0))/722925
```

## Python Example
Here is the algorithm that we'll be using to compute the reciprocal Borchardt-Gauss algorithm, but in Python.
```
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
  return 3028466566125/z
```
