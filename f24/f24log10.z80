#ifndef included_f24log10
#define included_f24log10


#include "f24log.z80"
#include "f24mul.z80"

f24log10:
;log10(x) ==> AHL
  call f24log
;multiply by 1/log(10)
  ld c,$3D
  ld de,48312
  jp f24mul
#endif
