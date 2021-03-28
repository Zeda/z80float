#ifndef included_xlg
#define included_xlg
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xln.z80"

xlg:
;lg(x) = ln(x)/ln(2)
  call pushpop
  call xln
  ld h,b
  ld l,c
  ld de,xconst_lg_e
  jp xmul
#endif
