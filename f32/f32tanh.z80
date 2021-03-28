#ifndef included_f32tanh
#define included_f32tanh
#include "pushpop.z80"
#include "f32exp.z80"
#include "f32mul2.z80"
#include "f32div.z80"
#include "f32rsub.z80"

f32tanh:
;tanh(x) = (e^(2x)-1)/(e^(2x)+1)
;        = 1-2/(e^(2x)+1)
;
  call pushpop
  push hl
  push de
;e^(2x)+1
  call f32mul2
  ld h,b
  ld l,c
  call f32exp
  ld de,f32_const_1
  call f32add

;1-2/ans
  ex de,hl
  call f32div
  ex de,hl
  call f32mul2
  jp f32rsub
#endif
