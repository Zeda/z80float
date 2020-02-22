#ifndef included_f24geomean
#define included_f24geomean

#include "f24mul.z80"
#include "f24sqrt.z80"

f24geomean:
;sqrt(AHL*CDE) ==> AHL

;return NaN if the product is negative
  xor c
  jp p,+_
  ld a,$7F
  ld h,a
  ret
_:

;the product is positive, so we can just set the inputs to positive
  xor c
  and $7F
  ret z   ;may as well exit if the input is 0
  cp $7F
  jr z,f24geomean_sub
  ld b,a

  ld a,c
  and $7F
  ret z
  cp $7F
  jr z,f24geomean_sub

;now calculate the output exponent
  add a,b
  rra
  push af

  ld a,63
  ld c,a
  adc a,0
  call f24geomean_sub
  pop bc
  add a,b
  sub 63
  ret

f24geomean_sub:
  call f24mul
  jp f24sqrt
#endif
