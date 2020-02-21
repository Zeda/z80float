#ifndef included_f24cosh
#define included_f24cosh

#include "f24exp.z80"
#include "f24amean.z80"

f24cosh:
;cosh(x) ==> AHL

;save x
  push hl
  push af

;e^-x
  xor 80h
  call f24exp

;e^x
  pop bc
  ex (sp),hl
  push af
  ld a,b
  call f24exp

;(e^x+e^-x))/2
  pop bc
  pop de
  ld c,b
  jp f24amean
#endif
