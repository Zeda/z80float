#ifndef included_x_to_int16
#define included_x_to_int16

x_to_int16:
;Input: HL points to an extended-precision float
;Output: HL is a 16-bit signed integer representation of the input float.

  push ix
  push de
  push bc
  push af
  call +_
  pop af
  pop bc
  pop de
  pop ix
  ret
_:
  push hl
  pop ix
  ld e,(ix+6)
  ld d,(ix+7)
  ld a,(ix+9)
  ld hl,0
  add a,a
  jp p,x_to_int16_zero
  add a,a
  jr nz,x_to_int16_inf
  ld a,(ix+8)
  cp 15       ;at most 15 bits since signed
  jr nc,x_to_int16_inf
  inc a
  cp 8
  jr c,+_
  sub 8
  ld l,d
  ld d,e
  jr z,x_to_int16_end
_:
  ld b,a
  ld a,d
_:
  rla
  adc hl,hl
  djnz -_
x_to_int16_end:
  ld a,(ix+9)
  add a,a
  ret nc
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  ret


x_to_int16_zero:
  ret nz
;maybe it is a special number, though
  ld a,(ix+8)
  or a
  ret nz
;it is special, so now we check for special values
; 0 --> 0
; NAN --> 65535
; -INF --> 65535
;INF --> 32767
  ld a,d
  add a,a
  jr c,x_to_int16_inf
  ret z
x_to_int16_inf:
  dec hl
  ld a,(ix+9)
  add a,a
  ret c
  res 7,h
  ret

#endif
