#ifndef included_f32asin
#define included_f32asin
#include "pushpop.z80"
#include "mov4.z80"
#include "f32constants.z80"
#include "f32mul.z80"
#include "f32rsub.z80"
#include "f32sqrt.z80"
#include "f32bgi.z80"

#define f32asin_x f32bgi_c+4

f32asin:
;asin(x)
;x/BG(sqrt(1-x^2),1)
;
  call pushpop
  push bc


; copy x to f32asin_x
  ld de,f32asin_x
  call mov4

; compute x^2
  ld de,f32asin_x
  ld h,d
  ld l,e
  ld bc,f32bgi_a
  call f32mul

; now 1-x^2
  ld de,f32_const_1
  ld h,b
  ld l,c
  call f32rsub

; sqrt(1-x^2)
  call f32sqrt

; now DE points to 1.0, we need to compute 1/BG(sqrt(1-x^2), 1)
  call f32bgi

  ld de,f32asin_x
  pop bc
  jp f32mul
#endif
