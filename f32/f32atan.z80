#ifndef included_f32atan
#define included_f32atan
#include "pushpop.z80"
#include "mov4.z80"
#include "f32constants.z80"
#include "f32mul.z80"
#include "f32add.z80"
#include "f32sqrt.z80"
#include "f32bgi.z80"

#define f32atan_x f32bgi_c+4

f32atan:
;atan(x)
;Computed as x/BG(1.0,sqrt(1+x^2))
;

  call pushpop
  push bc


; copy x to f32atan_x
  ld de,f32atan_x
  call mov4

; compute x^2
  ld de,f32atan_x
  ld h,d
  ld l,e
  ld bc,f32bgi_g
  call f32mul

; now x^2 + 1
  ld de,f32_const_1
  ld h,b
  ld l,c
  call f32add

; sqrt(1+x^2)
  call f32sqrt

; now DE points to 1.0, we need to compute 1/BG(1, sqrt(1+x^2))
  ex de,hl
  call f32bgi

  ld hl,f32atan_x
  pop bc
  jp f32mul
#endif
