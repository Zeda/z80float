#ifndef included_f32cosh
#define included_f32cosh

#include "pushpop.z80"
#include "f32exp.z80"
#include "f32amean.z80"

#define f32cosh_x scrap+4
f32cosh:
;cosh(x) = (e^x+e^-x))/2
  call pushpop
  push bc
  ld bc,f32cosh_x
  call f32exp
  ld d,b
  ld e,c
  pop bc
  ld hl,f32_const_1
  call f32div
  ld h,b
  ld l,c
  jp f32amean
#endif
