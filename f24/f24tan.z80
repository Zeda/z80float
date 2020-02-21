#ifndef included_f24tan
#define included_f24tan

#include "f24cos.z80"
#include "f24div.z80"


f24tan:
;tan(AHL) ==> AHL
  push hl
  push af
  call f24cos
  pop bc
  ex (sp),hl
  push af
  ld a,b
  call f24sin
  pop bc
  pop de
  ld c,b
  jp f24div
#endif
