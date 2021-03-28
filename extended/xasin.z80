#ifndef included_xasin
#define included_xasin
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xrsub.z80"
#include "xsqrt.z80"
#include "xbg.z80"

;x/BG(sqrt(1-x^2),1)
#define var_x  xOP1+152
xasin:
  call pushpop
  push bc
  push hl
  ld d,h
  ld e,l
  ld bc,xOP1
  call xmul
  ld h,b
  ld l,c
  ld de,xconst_1
  call xrsub
  call xsqrt
  call xbg
  pop de
  pop bc
  jp xmul
#endif
