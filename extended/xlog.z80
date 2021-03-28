#ifndef included_xlog
#define included_xlog
#include "pushpop.z80"
#include "xdiv.z80"
#include "xln.z80"

#define var_y  xOP1+162
#define var_y0  xOP1+172
xlog:
  call pushpop
  push bc
  ld bc,var_y0
  call xln
  ld bc,var_y
  ex de,hl
  call xln
  ld d,b
  ld e,c
  pop bc
  ld hl,var_y0
  jp xdiv
#undefine var_y
#endif
