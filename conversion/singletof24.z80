#ifndef included_singletof24
#define included_singletof24

singletof24:
;convert a single-precision float (the format in this lib) at HL
;to an f24 float in AHL
;destroys BC,DE

  ld c,(hl)
  inc hl
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
;check for special values
  or a
  jr nz,+_
  ;get the sign
  rl d
  rra
  ret z
  or $7F
  rl d
  ccf
  sbc hl,hl
  ret
_:

;Make sure the exponent isn't too large
  cp 64+128
  jr c,+_
  ld a,d
  or $7F
  ld h,b
  ld l,b
  ret
_:

;Make sure the exponent isn't too small
  sub 128-62
  jr nc,+_
  xor a
  ret
_:

;okay, now adjust the exponent
  inc a
  add a,a

;shift the mantissa up 1
  sla c
  ex de,hl
  adc hl,hl
;shift the sign into a
  rra

;round
  sla c
  ld bc,0
  adc hl,bc
  adc a,b
  ret
#endif
