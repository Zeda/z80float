#ifndef included_f32pow10
#define included_f32pow10

#include "f32constants.z80"
#include "f32pow2.z80"
#include "f32mul.z80"

f32pow10:
;  10^x = 2^(x*lg(10))
  push de
  ld de,f32_const_lg_10
  call f32mul
  pop de
  push hl
  ld h,b
  ld l,c
  call f32pow2
  pop hl
  ret
#endif
