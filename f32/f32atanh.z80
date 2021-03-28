#ifndef included_f32atanh
#define included_f32atanh
#include "pushpop.z80"
#include "f32log.z80"
#include "f32sqrt.z80"
#include "f32div.z80"
#include "f32rsub.z80"
#include "f32add.z80"

f32atanh:
;atanh(x) = log((1+x)/(1-x))/2
;
  call pushpop
  push bc
  ld de,f32_const_1
  ld bc,f32bgi_g
  call f32rsub
  ld bc,f32bgi_a
  call f32add
  ld h,b
  ld l,c
  ld de,f32bgi_g
  call f32div
  pop bc
  call f32log
  ld h,b
  ld l,c

  inc hl
  inc hl
  ld a,(hl)
  add a,a
  inc hl
  ld a,(hl)
  adc a,a
  ret z
  inc a
  ret z
  dec a
  dec a
  rra
  ld (hl),a
  dec hl
  rl (hl)
  rrc (hl)
  ret
#endif
