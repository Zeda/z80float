#ifndef included_f32tan
#define included_f32tan

#include "f32cos.z80"
#include "f32sin.z80"
#include "f32div.z80"


#define f32tan_x f32cos_y+4
f32tan:
;tan(x)
  call pushpop
  push bc
  call f32cos
  ld bc,f32tan_x
  call f32sin
  ld h,b
  ld l,c
  pop bc
  ld d,b
  ld e,c
  jp f32div
#endif
