#ifndef included_f32cos
#define included_f32cos

#include "f32sin.z80"
#include "f32mul.z80"
#include "f32mod1.z80"
#include "f32sub.z80"
#include "f32neg.z80"
#include "f32abs.z80"
#include "f32horner_step.z80"

#define f32cos_x scrap
#define f32cos_y scrap+4
f32cos:
;cos(x)
  call pushpop
f32cos_nopushpop:
  push bc
  ld de,f32cos_x
  ldi
  ldi
  ld a,(hl)
  add a,a
  ldi
  ld a,(hl)
; we can drop the sign since cos(-x) = cos(x)
  adc a,a
  rra
  ld (de),a
  jp z,f32cos_return_1
  adc a,a
  inc a
  jp z,f32cos_return_NaN

  ld hl,f32cos_x
  ld b,h
  ld c,l
  ld de,f32_const_2pi_inv
  call f32mul

; Add .5
  ld de,f32_const_p5
  call f32add

;Now grab mod 1
  call f32mod1

f32cos_stepin:
;subtract off the .5
  ld de,f32_const_p5
  call f32sub

;  cos(-x)=cos(x)
  ld hl,f32cos_x+2
  ld a,(hl)
  add a,a
  inc hl
  res 7,(hl)
  ld a,(hl)
  adc a,a   ; A is a copy of the exponent
  jr z,f32cos_return_1

;  cos(x-pi)=-cos(x)
;   if our x is now on [.25,.5], then subtract x from .5 absolute value,
;   and return the negative result.
  pop bc
  cp $7D
  jr c,+_
  ; do (.5 - x)
  ; ld de,f32_const_p5
  push bc
  ld bc,f32cos_x
  ld h,b
  ld l,c
  call f32rsub
  ld hl,f32cos_x+2
  ld a,(hl)
  add a,a
  inc hl
  ld a,(hl)
  adc a,a   ; A is a copy of the exponent
  pop bc
  call +_
  ld h,b
  ld l,c
  jp f32neg
_:
  push bc
  ld bc,f32cos_x

;  cos(pi/2-x)=sin(x)
;    if our x is now on [.125,.25], subtract it from .25 and feed it to the sine routine.
  cp $7C
  jr c,f32cos_range_reduced
  ;(.25-x)
  ld hl,f32cos_x
  ld de,f32_const_p25
  call f32rsub
  jp f32sin_range_reduced

f32cos_range_reduced:
;multiply by 2pi
  ld hl,f32cos_x
  ld de,f32_const_2pi
  call f32mul

;cos(-pi/4<=x<pi/4)
;y=x*x
;1-y(.49999887-y(.041655882-y.0013591743))
;1-y(a1-y(a2-y*a3))

  ld bc,f32cos_y
  ld d,h
  ld e,l
;-x^2 ==> y
  call f32mul
  ld hl,f32cos_y+3
  set 7,(hl)

  pop de
  ld hl,f32cos_a3
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
  ld hl,f32cos_a2
  call f32horner_step
  ld hl,f32cos_a1
  call f32horner_step
  ld hl,f32_const_1
  jp f32horner_step

f32cos_return_NaN:
  ld hl,f32_const_NaN
  jr f32cos_return
f32cos_return_1:
  ld hl,f32_const_1
f32cos_return:
  pop de
  jp mov4

f32cos_a3:
.db $52,$26,$B2,$3A  ;.0013591743
f32cos_a2:
.db $5C,$9F,$2A,$3D  ;.041655882
f32cos_a1:
.db $DA,$FF,$FF,$3E  ;.49999887
#endif
