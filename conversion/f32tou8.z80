#ifndef included_f32tou8
#define included_f32tou8

f32tou8:
;Inputs: HL points to an f32 float
;Outputs: A is the unsigned 8-bit integer part of the input (rounded down)
;Special cases:
;   NaN              ==> 0
;   greater than 255 ==> 255
;   less than 0      ==> 0

  push hl
  push de
  push bc
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
  rlca
  scf
  rra
  ld c,a
  inc hl
  ld a,(hl)
  adc a,a
  ccf
  jr nc,f32tou8_return_carry
  or a
  jr z,f32tou8_return_carry
  inc a
  jr z,f32tou8_infnan

  add a,256-135
  jr c,f32tou8_return_carry
  add a,7
  jr nc,f32tou8_return_carry

  ld b,a
  inc b
  xor a
  rl c
  rla
  djnz $-3

  .db $FE
f32tou8_return_carry:
  sbc a,a
f32tou8_return:
  pop bc
  pop de
  pop hl
  ret

f32tou8_infnan:
  ld a,c
  add a,a
  or d
  or e
  sub 1
  jr f32tou8_return_carry
#endif
