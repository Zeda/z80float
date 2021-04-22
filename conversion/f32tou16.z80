#ifndef included_f32tou16
#define included_f32tou16

f32tou16:
;Inputs: HL points to an f32 float
;Outputs: HL is the unsigned 16-bit integer part of the input (rounded down)
;Special cases:
;   NaN                ==> 0
;   greater than 65535 ==> 65535
;   less than 0        ==> 0

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
  ccf
  jr nc,f32tou16_return_carry
  or a
  jr z,f32tou16_return_carry
  inc a
  jr z,f32tou16_infnan

  add a,256-143
  jr c,f32tou16_return_carry
  add a,15
  jr nc,f32tou16_return_carry

  ld b,a
  inc b
  ex de,hl
  xor a
  ld e,a

  add hl,hl
  rl e
  rla
  djnz $-4

  ld l,e
  ld h,a

  .db $01 ; start of `ld bc,**` to skip the next two bytes
f32tou16_return_carry:
  sbc hl,hl

f32tou16_return:
  pop af
  pop bc
  pop de
  ret
f32tou16_infnan:
  ld a,d
  add a,a
  or e
  or c
  sub 1
  jr f32tou16_return_carry
#endif
