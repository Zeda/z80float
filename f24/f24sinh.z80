#ifndef included_f24sinh
#define included_f24sinh

#include "f24exp.z80"
#include "f24amean.z80"

f24sinh:
;sinh(x) ==> AHL

;save x
  push hl
  push af

;-e^-x
  xor 80h
  call f24exp
  xor 80h

;e^x
  pop bc
  ex (sp),hl
  push af
  ld a,b
  call f24exp

;(e^x+(-e^-x))/2
  pop bc
  pop de
  ld c,b
  jp f24amean
#endif
