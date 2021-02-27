#ifndef included_f32log2
#define included_f32log2
#include "f32constants.z80"
#include "f32log.z80"
#include "f32mul.z80"

f32log2:
;log2(x)
  call f32log
  push hl
  push de
  ld h,b
  ld l,c
  ld de,f32_const_lg_e
  call f32mul
  pop de
  pop hl
  ret
#endif
