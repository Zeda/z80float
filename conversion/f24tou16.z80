#ifndef included_f24tou16
#define included_f24tou16

f24tou16:
;AHL to a 16-bit unsigned integer
;NaN ==> 0
;too big ==> 65535 (even if neg)
;negative values in range are mod 65536

;save the sign
  ld c,a

;Check if the input is 0
  add a,a
  jr z,f24tou16_return_0


;check if inf or NaN
  cp $FE
  jr nz,+_
  ld a,h
  or l
  jr nz,f24tou16_return_0
f24tou16_return_inf:
  ld hl,-1
  ret
_:

;now if exponent is less than 0, just return 0
  cp 63*2
  jr nc,+_
f24tou16_return_0:
  ld hl,0
  ret
_:

;if the exponent is greater than 15, return 255
  rra
  sub 63
  cp 16
  jr nc,f24tou16_return_inf

;all is good!
;A is the exponent
;1+A is the number of bits to read
  ld b,a
  or a
  ld a,1
  ld d,0
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
