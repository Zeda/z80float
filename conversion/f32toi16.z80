#ifndef included_f32toi16
#define included_f32toi16

f32toi16:
;Inputs: HL points to an f32 float
;Outputs: HL is the signed 16-bit integer part of the input (rounded down)
;Special cases:
;   NaN              ==> 0
;   greater than 127 ==> 32767
;   less than -128   ==> -32768
  push de
  push bc
  push af

  ld c,(hl)
  inc hl
  ld e,(hl)
  inc hl
  ld a,(hl)
  rlca
  scf
  rra
  ld d,a
  inc hl
  ld a,(hl)
  adc a,a
; carry flag is sign, DEC is the significand, A is the exponent
  call f32toi16_get_int
f32toi16_return:
  pop af
  pop bc
  pop de
  ret

f32toi16_infnan:
  ; if the exponent is 128, return 0 if NaN, else inf
  ld a,d
  add a,a
  or e
  or c
  ret nz
f32toi16_inf:
  ld hl,32767
  rr b
  ret nc
  inc hl
  ret

f32toi16_zero_ish:
  rr b
  ret nc
  ld a,d
  add a,a
  or e
  or c
  ret z
  dec hl
  ret

f32toi16_get_int:
  rl b    ; save the sign
  ld hl,0
  inc a
  jr z,f32toi16_infnan
  jp p,f32toi16_zero_ish
  sub 128
  cp 15
  jr nc,f32toi16_inf
  ex de,hl  ; significand is in HLC now, but we don't need to track C
  ;DE is 0
  cp 7
  jr c,$+7
  ;shift up by 8
  sub 8
  ld e,h
  ld h,l
  ld l,d    ; 0

  ld d,b    ; save sign
  ld b,a
  xor a
  ;AE.HLC
  inc b
  jr z,$+8
  add hl,hl
  rl e
  rla
  djnz $-4

  ld b,d    ; save sign again
  ld d,a
  ex de,hl
  ; HL is the result, DEC has any fractional bits

  rrc b   ; if carry is reset, then we are done
  ret nc
  ; otherwise the number is negative, so if the fractional part is non-zero,
  ; need to round down

  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a

  ld a,c
  or d
  or e
  ret z
  dec hl
  ret
#endif
