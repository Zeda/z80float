#ifndef included_f32toi8
#define included_f32toi8

f32toi8:
;Inputs: HL points to an f32 float
;Outputs: A is the signed 8-bit integer part of the input (rounded down)
;Special cases:
;   NaN              ==> 0
;   greater than 127 ==> 127
;   less than -128   ==> -128

  push hl
  push de
  push bc
  ld a,(hl)
  inc hl
  or (hl)
  ld d,a    ; save the OR of the bottom two bytes of the significand
  inc hl
  ld a,(hl)
  rlca
  scf
  rra
  ld c,a
  inc hl
  ld a,(hl)
  adc a,a

  rr e    ; save the sign
; E has the sign, C is the portion of the significand that matters,
; A is the exponent

  call f32toi8_get_int

f32toi8_return:
  pop bc
  pop de
  pop hl
  ret

f32toi8_zero_ish:
  xor a
  rl e
  ret nc
  ld a,c
  add a,a
  or d
  add a,255
  sbc a,a
  ret

f32toi8_infnan:
  ; if the significand is non-zero, return NaN
  ld a,c
  add a,a
  or d
  sub 1
  sbc a,a
  ret z
f32toi8_inf:
  ld a,127
  rl e
  adc a,0
  ret

f32toi8_get_int:
  inc a
  jr z,f32toi8_infnan
  jp p,f32toi8_zero_ish
  sub 128
  cp 7
  jr nc,f32toi8_inf

  ld h,0
  ld l,c    ; upper 8 bits of the significand, H is 0
  ld b,a
  inc b
  add hl,hl
  djnz $-1
  ld a,h
  rl e
  ret nc
  ld a,l
  or d
  add a,255
  sbc a,a
  sub h
  ld h,a
  ret
#endif
