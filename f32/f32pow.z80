#ifndef included_f32pow
#define included_f32pow

#include "f32constants.z80"
#include "f32pow2.z80"
#include "f32log2.z80"
#include "f32mul.z80"

f32pow:
; x^y = 2^(y*lg(x))
  push hl
  call f32log2
  ld h,b
  ld l,c
  call f32mul
  call f32pow2
  pop hl
  ret
#endif
