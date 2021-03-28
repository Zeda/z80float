#ifndef included_log10Single
#define included_log10Single
#include "pushpop.z80"
#include "constants.z80"
#include "mulSingle.z80"
#include "lnSingle.z80"
log10Single:
;lg(x) = ln(x)/ln(2)
  call pushpop
  call lnSingle
  ld h,b
  ld l,c
  ld de,const_log10_e
  jp mulSingle
#endif
