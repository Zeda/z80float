#ifndef included_f24pow2
#define included_f24pow2

#include "f24exp.z80"
#include "f24mul.z80"

f24pow2:
;2^x ==> AHL
;x*ln(2)
  ld c,$3E
  ld de,25316
  call f24mul
  jp f24exp
#endif
