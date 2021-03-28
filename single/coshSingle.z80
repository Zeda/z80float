#ifndef included_coshSingle
#define included_coshSingle
#include "pushpop.z80"
#include "expSingle.z80"
#include "invSingle.z80"
#include "ameanSingle.z80"

#define hyperout scrap+9
#define hyperout2 scrap+13
coshSingle:
  call pushpop
  push bc
  ld bc,hyperout
  call expSingle
  ld h,b
  ld l,c
  ld bc,hyperout2
  call invSingle
  ld d,b
  ld e,c
  pop bc
  jp ameanSingle_no_pushpop
#endif
