#ifndef included_f24toi8
#define included_f24toi8

f24toi8:
;AHL to an 8-bit signed integer
;NaN ==> 0
;+inf ==> 127
;-inf ==> -128

;save the sign of the output
  ld c,a

;Check if the input is 0
  add a,a
  ret z

;check if inf or NaN
  cp $FE
  jr nz,+_
  ld a,h
  or l
  jr nz,f24toi8_return_0
f24toi8_return_inf:
  sla c
  ld a,127
  adc a,0
  ret
_:

;now if exponent is less than 0, just return 0
  cp 63*2
  jr nc,+_
f24toi8_return_0:
  xor a
  ret
_:

;if the exponent is greater than 6, return 127 or -128
  rra
  sub 63
  cp 7
  jr nc,f24toi8_return_inf

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
