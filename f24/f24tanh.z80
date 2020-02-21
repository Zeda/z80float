#ifndef included_f24tanh
#define included_f24tanh

#include "f24exp.z80"
#include "f24mul2.z80"
#include "f24div.z80"

f24tanh:
;tanh(x) ==> AHL
;(e^(2x)-1)/(e^(2x)+1)
; = 1-2/(e^(2x)+1)
;
;e^(2x)+1
  call f24mul2
  call f24exp
  ld c,$3F
  ld de,0
  call f24add

;1-2/ans
  ex de,hl
  ld c,a
  ld a,$C0
  ld hl,0
  call f24div
  ld c,$3F
  ld de,0
  jp f24add

#endif
