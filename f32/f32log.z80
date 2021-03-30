#ifndef included_f32log
#define included_f32log
#include "pushpop.z80"
#include "mov4.z80"
#include "routines/f32_muli8.z80"
#include "f32constants.z80"
#include "f32bgi.z80"
#include "f32mul.z80"
#include "f32sub.z80"
#include "f32add.z80"
#include "f32amean.z80"
#include "f32sqrt.z80"

#define f32log_x f32bgi_c+4


f32log:
;log(x) (natural logarithm)
;(x-1)/BG(.5(1+x), sqrt(x))
  call pushpop
  push bc

; copy to f32log_x, check special values
  ld de,f32log_x
  ldi
  ldi
  ld a,(hl)
  add a,a
  ldi
  ld a,(hl)
  ld (de),a
  adc a,a
  ;ln(-x) == NaN
  jr c,f32log_return_NaN
  ;ln(0) == -inf
  jr z,f32log_return_ninf
  inc a
  jr z,f32log_return_x
; A-1 is the exponent. We'll hold onto this for later.
  push af
; now set the exponent to 0
  ex de,hl
  ld (hl),%00111111
  dec hl
  set 7,(hl)

;(x-1)/BG(.5(1+x), sqrt(x))
  ld hl,f32log_x
  ld bc,f32bgi_g
  call f32sqrt
  ld de,f32_const_1
  ld bc,f32bgi_a
  call f32amean
  ld bc,f32log_x
  call f32sub

  ld hl,f32bgi_a
  ld de,f32bgi_g
  ld b,h
  ld c,l
  call f32bgi

  ld de,f32log_x
  call f32mul

  pop af
;(A-128)*log(2) + f32bgi_a
  sub 128
  ld hl,f32_const_ln2
  ld bc,f32bgi_g
  call f32_muli8
  ld h,b
  ld l,c
  ld de,f32bgi_a
  pop bc
  jp f32add

f32log_return_NaN:
  .db $3E ; start of `ld a,*`
f32log_return_ninf:
  xor a
  pop hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  or %10000000
  ld (hl),a
  inc hl
  ld (hl),-1
  ret

f32log_return_x:
  pop de
  ld hl,f32log_x
  jp mov4
#endif
