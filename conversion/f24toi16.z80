#ifndef included_f24toi16
#define included_f24toi16

f24toi16:
;AHL to a 16-bit signed integer
;NaN ==> 0
;+inf ==> 32767
;-inf ==> -32768

;save the sign of the output
  ld c,a

;Check if the input is 0
  add a,a
  jr z,f24toi16_return_0

;check if inf or NaN
  cp $FE
  jr nz,+_
  ld a,h
  or l
  jr nz,f24toi16_return_0
f24toi16_return_inf:
  sla c
  ld hl,32767
  ret nc
  inc hl
  ret
_:

;now if exponent is less than 0, just return 0
  cp 63*2
  jr nc,+_
f24toi16_return_0:
  ld hl,0
  ret
_:

;if the exponent is greater than 14, return +- "inf"
  rra
  sub 63
  cp 15
  jr nc,f24toi16_return_inf

;all is good!
;A is the exponent
;1+A is the number of bits to read
  or a
  ld b,a
  ld d,0
  ld a,1
  jr z,+_

  add hl,hl
  rla
  rl d
  djnz $-4
_:
  sla c
  ld e,a
  ex de,hl
  ret nc
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  ret
#endif
