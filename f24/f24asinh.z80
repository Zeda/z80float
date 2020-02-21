#ifndef included_f24asinh
#define included_f24asinh

#include "f24log.z80"
#include "f24sqr.z80"

f24asinh:
;asinh(AHL) ==> AHL
;log(x+sqrt(x^2+1))
;

;save x
  push hl
  push af

;sqrt(x^2+1)
  call f24sqr
  ld c,$3F
  ld de,0
  call f24add
  call f24sqrt

;+x
  pop bc
  pop de
  ld c,b
  call f24add
  jp f24log
#endif
