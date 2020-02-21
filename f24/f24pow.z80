#ifndef included_f24pow
#define included_f24pow

#include "f24exp.z80"
#include "f24log.z80"
#include "f24mul.z80"

f24pow:
;x^y ==> AHL

; save y
  push de
  push bc

;ln(x)
  call f24log

;*y
  pop bc
  pop de
  call f24mul

  jp f24exp
#endif
