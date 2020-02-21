#ifndef included_f24log2
#define included_f24log2

#include "f24log.z80"
#include "f24mul.z80"

f24log2:
;log2(x) ==> AHL
  call f24log
;multiply by 1/log(2)
  ld c,$3F
  ld de,29012
  jp f24mul
#endif
