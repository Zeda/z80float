#ifndef included_f32div
#define included_f32div
#include "pushpop.z80"
#include "routines/div24_24.z80"

f32div:
;x/y ==> z
  call pushpop
  push bc
  push de
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld b,(hl)
  inc hl
  ld a,b
  add a,a
  ld a,(hl)
  adc a,a
  ;A is the exponent, carry is the sign
  pop hl
  jp z,f32div_0_op2
  inc a
  jp z,f32div_infnan_op2
  dec a
  push af
  push de



  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld c,(hl)
  inc hl
  ld a,c
  add a,a
  ld a,(hl)
  adc a,a
  ;A is the exponent, carry is the sign
  pop hl
  jp z,f32div_op1_0
  inc a
  jp z,f32div_op1_infnan
  push af

  set 7,c
  set 7,b
  ;CHL is the first operand, BDE is the second operand
  ; if CHL >= BDE then need to increment exponent and shift CHL>>1
  or a
  sbc hl,de
  ld a,b
  sbc a,c
  jr nc,+_
  add hl,de
  adc a,c
_:
  ld b,a
  sbc a,a
  inc a
  ;A is 1 if we need to shift a 1 into the result of the division, else 0
  push af ;nc if we need to shift in a 1
  call div24_24
  pop hl

  rr h      ;shift out the bottom bit, shift round bit into H
  jr nc,+_
  rr b
  rr d
  rr e
  pop af
  dec a
  .db $0E ;start of `ld c,*` to eat the next byte
_:
  pop af
  ld l,a
  rr h
  pop af
  rr h    ;top 2 bits of H are signs

  ;H.BDE, need to add carry
  bit 5,h
  jr z,+_
  inc e
  jr nz,+_
  inc d
  jr nz,+_
  inc b
  jr nz,+_
  dec l
_:

  sub l
  ld l,0
  jr nc,$+3
  dec l
  add a,7Fh
  jr nc,$+3
  inc l
  dec l
  jr z,f32div_return_inf
  inc l
  jr nz,f32div_return_zero

f32div_return:
;BDE is the significand
  sla b
  ld l,a  ;exponent
  ld a,h
  and %11000000
  jp pe,$+4
  scf
  ld a,l
  rra
  rr b
  pop hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),b
  inc hl
  ld (hl),a
  ret

f32div_0_op2:
; if op2 is 0 or NaN, return NaN, else 0
;if OP2 is 0, inf, or NaN, return NaN
  rr b       ;save the sign of OP1
  ld a,(hl)
  inc hl
  or (hl)
  inc hl
  ld c,(hl)
  sla c
  or c
  ld c,a    ;c is zero if the significand is zero
  ld a,(hl)
  add a,a
  inc hl
  ld a,(hl)
  adc a,a
  ld h,b
  jr z,f32div_return_NaN
  rr h
  inc a
  ;If A is not zero, return 0
  ;If A is 0 and C is 0, then continue
  ;If A is 0 and C is not 0, NaN
  jr nz,f32div_return_zero
  or c
  jr z,f32div_return_zero
  jr f32div_return_NaN2

f32div_infnan_op2:
;if OP2 is 0, inf, or NaN, return NaN
  rr c      ;save the sign of OP1
  inc hl
  inc hl
  ld a,(hl)
  add a,a
  inc hl
  ld a,(hl)
  adc a,a
  ld h,c
  jr z,f32div_return_NaN
  inc a
  jr z,f32div_return_NaN
  ;otherwise, return OP1, BDE ==> BDE
  rr h
  ld a,-1
  jr f32div_return

f32div_op1_0:
  rr h
  pop af
f32div_return_NaN:
  rr h
f32div_return_NaN2:
  ld a,-1
  ld b,a  ;something > 1
  jr f32div_return

f32div_op1_infnan:
;if the second op is NaN, return NaN, else 0
  rr h
  pop af
  rr h
  ld a,c
  add a,a
  or d
  or e
  jr z,f32div_return_zero
  jr f32div_return_NaN2

f32div_return_inf:
  ld a,$FF
  .db $FE
f32div_return_zero:
  xor a
  ld b,a
  jr f32div_return
#endif
