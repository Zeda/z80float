#ifndef included_f24tou8
#define included_f24tou8

f24tou8:
;AHL to an 8-bit unsigned integer
;NaN ==> 0
;too big ==> 255 (even if neg)
;negative values in range are mod 256

;save the sign
  ld c,a

;Check if the input is 0
  add a,a
  ret z


;check if inf or NaN
  cp $FE
  jr nz,+_
  ld a,h
  or l
  jr nz,f24tou8_return_0
f24tou8_return_inf:
  ld a,255
  ret
_:

;now if exponent is less than 0, just return 0
  cp 63*2
  jr nc,+_
f24tou8_return_0:
  xor a
  ret
_:

;if the exponent is greater than 7, return 255
  rra
  sub 63
  cp 8
  jr nc,f24tou8_return_inf

;all is good!
;A is the exponent
;1+A is the number of bits to read
  ld b,a
  or a
  ld a,1
  jr z,+_

  add hl,hl
  rla
  djnz $-2
_:
  sla c
  ret nc
  neg
  ret

#endif
