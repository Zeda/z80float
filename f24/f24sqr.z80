#ifndef included_f24sqr
#define included_f24sqr
#include "f24mul.z80"

f24sqr:
;AHL * AHL ==> AHL
;Destroys BC,DE
;

;0*0 ==> 0
  and $7F
  ret z

;NaN*NaN ==> NaN
;inf*inf ==> inf
  inc a
  jp p,+_
  dec a
  ret
_:

;first approximation of the exponent is
; (A-1)+(A-1) - 63
  add a,a   ;won't overflow since top bit is guaranteed reset at this point
  sub 65
  jr nc,$+4
  xor a     ;underflowed, so return 0
  ret

  cp $7F
  jp nc,f24mul_return_inf+1

  ld d,h
  ld e,l

  jp f24mul_significand
#endif
