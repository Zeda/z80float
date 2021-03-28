#ifndef included_xacos
#define included_xacos
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xsub.z80"
#include "xsqrt.z80"
#include "xbg.z80"

;sqrt(1-x^2)/BG(x,1)
#define var_x  xOP1+152
xacos:
  call pushpop
  push bc
  push hl
  ld d,h
  ld e,l
  ld bc,xOP1
  call xmul
  ld hl,xconst_1
  ld d,b
  ld e,c
  ld bc,var_x
  call xsub
  ex de,hl
  ld h,b
  ld l,c
  call xsqrt
  pop hl
  ld bc,xOP1
  call xbg
  ld h,b
  ld l,c
  ld de,var_x
  pop bc
  jp xmul
#endif
