#ifndef included_f24pow10
#define included_f24pow10

#include "f24exp.z80"
#include "f24mul.z80"

f24pow10:
;10^x ==> AHL
;x*ln(10)
  ld c,$40
  ld de,9915
  call f24mul
  jp f24exp
#endif
