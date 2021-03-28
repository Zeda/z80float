#ifndef included_xatanh
#define included_xatanh
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xrsub.z80"
#include "xsqrt.z80"
#include "xbg.z80"

#include "xrsub.z80"
#include "xdiv.z80"
#include "xdiv2.z80"
#include "xln.z80"

;x/BG(1,sqrt(1-x^2))
#define var_x  xOP1+152
xatanh:
;log((1+x)/(1-x))/2
  call pushpop
  push bc

  ld bc,xOP4
  ld de,xconst_1
  call xadd
  ld bc,xOP5
  ld de,xconst_1
  call xrsub
  ld d,b
  ld e,c
  ld hl,xOP4
  call xdiv
  ld h,b
  ld l,c
  call xln
  pop bc
  jp xdiv2
#endif
