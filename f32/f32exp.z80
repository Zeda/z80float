#ifndef included_f32exp
#define included_f32exp

#include "f32constants.z80"
#include "f32pow2.z80"
#include "f32mul.z80"

f32exp:
;  e^x = 2^(x*lg(e))
  push de
  ld de,f32_const_lg_e
  call f32mul
  pop de
  push hl
  ld h,b
  ld l,c
  call f32pow2
  pop hl
  ret
#endif
