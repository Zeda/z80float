#ifndef included_xtanh
#define included_xtanh
#include "pushpop.z80"
#include "mov.z80"
#include "xrsub.z80"
#include "xadd.z80"
#include "xinv.z80"
#include "xexp.z80"
#include "constantsx.z80"
#include "mul/xmul2.z80"

;https://www.math.utah.edu/~beebe/software/ieee/tanh.pdf
;p0 = -1613.4119023996228053
;p1 = -99.225929672236083313
;p2 = -.96437492777225469787
;q0 = 4840.2357071988688686
;q1 = 2233.7720718962312926
;q2 = 112.74474380534949335
;g=x*x
;r = g * ((p2 * g + p1) * g + p0)/(((g + q2)*g + q1) * g + q0)
;return x+x*r
;
;tanh(a+b) = (tanh(a)+tanh(b))/(1+tanh(a)tanh(b))
;We could precompute a table for `a` from 1 to 23

xtanh:
;Just going to go with the standard method
;tanh(x) = sinh(x)/cosh(x)
;  = (e^x-e^-x)/(e^x+e^-x)
;  = 1-2/(e^2x+1)

  call pushpop
  push bc
  ld bc,xOP1
  call xmul2
  ld h,b
  ld l,c
  call xexp
  ld de,xconst_1
  call xadd
  call xinv
  call xmul2
  pop bc
  jp xrsub
#endif
