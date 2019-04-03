#ifndef included_singleTo_int16
#define included_singleTo_int16
singleTo_int16:
;Input:
; HL points to the single-precision float
;Output:
; HL is the 16-bit signed integer part of the float
  push de
  push bc
  push af
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
  add a,a
  push af
  scf
  rra
  ld c,a
  inc hl
  ld a,(hl)
  ld hl,0
  sub 80h
  jr c,no_shift_single_to_int16
  cp 39
  jr nc,no_shift_single_to_int16
  sub 8
  jr c,+_
  ld l,c
  ld c,d
  ld d,e
  ld e,h
  sub 8
  jr c,+_
  ld h,l
  ld l,c
  ld c,d
  ld d,e
  sub 8
  jr c,+_
  ld h,l
  ld l,c
  ld c,d
  sub 8
  jr c,+_
  ld h,l
  ld l,c
  .db $11 ;start of ld de,*
_:
  add a,9
  ld b,a
  ld a,e
_:
  add a,a
  rl d
  rl c
  adc hl,hl
  djnz -_
no_shift_single_to_int16:
  pop af
  jr nc,+_
  ;need to negate
  xor a
  sub e \ ld e,0
  ld a,e \ sbc a,d
  ld a,e \ sbc a,c
  ld d,e
  ex de,hl
  sbc hl,de
_:
  pop af
  pop bc
  pop de
  ret
#endif
