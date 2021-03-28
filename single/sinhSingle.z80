#ifndef included_sinhSingle
#define included_sinhSingle
#include "pushpop.z80"
#include "expSingle.z80"
#include "invSingle.z80"
#include "ameanSingle.z80"

#define hyperout scrap+9
#define hyperout2 scrap+13
sinhSingle:
  call pushpop
  push bc
  ld bc,hyperout
  call expSingle
  ld h,b
  ld l,c
  ld bc,hyperout2
  call invSingle
  ld a,(hyperout2+2)
  xor 80h
  ld (hyperout2+2),a
  ld d,b
  ld e,c
  pop bc
  jp ameanSingle_no_pushpop
#endif
