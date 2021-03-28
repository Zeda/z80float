#ifndef included_f32acosh
#define included_f32acosh
#include "pushpop.z80"
#include "f32log.z80"
#include "f32sqrt.z80"
#include "f32mul.z80"
#include "f32sub.z80"
#include "f32add.z80"

f32acosh:
;acosh(x) = log(x+sqrt(x^2-1))
;
  call pushpop
  push bc
  push hl
  ld bc,f32bgi_a
  ld d,h
  ld e,l
  call f32mul
  ld h,b
  ld l,c
  ld de,f32_const_1
  call f32sub
  call f32sqrt
  pop de
  call f32add
  pop bc
  jp f32log
#endif
