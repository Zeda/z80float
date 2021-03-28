#ifndef included_f32sinh
#define included_f32sinh

#include "pushpop.z80"
#include "f32exp.z80"
#include "f32amean.z80"

#define f32sinh_x scrap+4
f32sinh:
;sinh(x) = (e^x+(-e^-x)))/2
  call pushpop
  push bc
  ld bc,f32sinh_x
  call f32exp
  ld d,b
  ld e,c
  pop bc
  ld hl,f32_const_n1
  call f32div
  ld h,b
  ld l,c
  jp f32amean
#endif
