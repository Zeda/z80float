#ifndef included_f32sin
#define included_f32sin

#include "f32cos.z80"
#include "f32rsub.z80"
#include "f32mul.z80"
#include "f32mod1.z80"
#include "f32abs.z80"
#include "f32horner_step.z80"

#define f32cos_x scrap
#define f32cos_y scrap+4
f32sin:
;sin(x) = cos(pi/2 - x)
  call pushpop
  ld de,f32_const_pi_div_2
  call f32rsub
  ld h,b
  ld l,c
  jp f32cos_nopushpop

f32sin_range_reduced:
;multiply by 2pi
  ld de,f32_const_2pi
  call f32mul

;sine(-pi/4<=x<pi/4)
;y=x*x
;a1=2^-3 * 11184804/2^23
;a2=2^-7 * 8946604/2^23
;a3=2^-13 * 13408017/2^23
;x(1-y(a1-y(a2-y*a3)))

  ld bc,f32cos_y
  ld d,h
  ld e,l
;-x^2 ==> y
  call f32mul
  ld hl,f32cos_y+3
  set 7,(hl)

  pop de
  ld hl,f32sin_a3
  ldi
  ldi
  ldi
  ld a,(hl)
  ld (de),a
  ld b,d
  ld c,e
  dec bc
  dec bc
  dec bc
  ld de,f32cos_y
  ld hl,f32sin_a2
  call f32horner_step
  ld hl,f32sin_a1
  call f32horner_step
  ld hl,f32_const_1
  call f32horner_step
  ld hl,f32cos_x
  ld d,b
  ld e,c
  jp f32mul

f32sin_a3:
.db $11,$97,$4C,$39  ;1.951123268e-4
f32sin_a2:
.db $AC,$83,$08,$3C  ;.0083321742713
f32sin_a1:
.db $A4,$AA,$2A,$3E  ;.1666665673
#endif
