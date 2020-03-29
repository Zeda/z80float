#ifndef included_f16toi16
#define included_f16toi16

f16toi16:
  ld a,h
  and %01111100
  jr z,f16toi16_zero
  rra
  rra
;A is the exponent + 15
  sub 15
  jr c,f16toi16_zero
  cp 15
  jr nc,f16toi16_inf
  ld b,a

;save the sign
  ld d,h

;set HL as the significand
  ld a,h
  and 3
  or 4
  ld h,a

  call f16toi16_sub

  sla d
  ret nc
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  ret

f16toi16_sub:
;if B is 10, can basicaly return HL
  ld a,b
  sub 10
  ret z
  jr nc,f16toi16_shiftleft
;HL needs to be shifted right
  srl h
  rr l
  dec a
  ret z
  srl h
  rr l
  dec a
  ret z
  srl h
  ld b,a
  ld a,l
f16toi16_loop:
  rra
  or a
  djnz f16toi16_loop
  ld l,a
  ret

f16toi16_shiftleft:
  add hl,hl
  djnz f16toi16_shiftleft
  ret

f16toi16_inf:
  sla h
  ld hl,$7FFF
  ret nc
  inc hl
  ret

f16toi16_zero:
  ld hl,0
  ret

#endif
