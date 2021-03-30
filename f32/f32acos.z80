#ifndef included_f32acos
#define included_f32acos
#include "pushpop.z80"
#include "mov4.z80"
#include "f32constants.z80"
#include "f32mul.z80"
#include "f32rsub.z80"
#include "f32sqrt.z80"
#include "f32bgi.z80"

#define f32acos_x f32bgi_c+4

f32acos:
;sqrt(1-x*x)*bgi(x,1)
  call pushpop
  push bc


; copy x to f32bgi_a
  ld de,f32bgi_a
  call mov4

; compute x^2
  ld de,f32bgi_a
  ld h,d
  ld l,e
  ld bc,f32acos_x
  call f32mul

; now 1-x^2
  ld de,f32_const_1
  ld h,b
  ld l,c
  call f32rsub

; sqrt(1-x^2)
  call f32sqrt

; now DE points to 1.0, we need to compute 1/BG(x, 1)
  ld hl,f32bgi_a
  ld b,h
  ld c,l
  call f32bgi

  ld de,f32acos_x
  pop bc
  jp f32mul
#endif
