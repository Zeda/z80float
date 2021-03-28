#ifndef included_xlog10
#define included_xlog10
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xln.z80"

xlog10:
;lg(x) = ln(x)/ln(2)
  call pushpop
  call xln
  ld h,b
  ld l,c
  ld de,xconst_log10_e
  jp xmul
#endif
