#ifndef included_lgSingle
#define included_lgSingle
#include "pushpop.z80"
#include "constants.z80"
#include "mulSingle.z80"
#include "lnSingle.z80"
lgSingle:
;lg(x) = ln(x)/ln(2)
  call pushpop
  call lnSingle
  ld h,b
  ld l,c
  ld de,const_lg_e
  jp mulSingle
#endif
