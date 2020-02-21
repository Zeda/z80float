#ifndef included_f24sub
#define included_f24sub

f24sub:
;AHL - CDE ==> AHL
;Destroys BC,DE
;
  ld b,a
  ld a,c
  xor $80
  ld c,a
  ld a,b
#ifdef included_f24add
  jp f24add
#else
#ifndef included_f24rsub
  db $DA    ;start of `jp c,**` since carry is reset, this eats two bytes
#endif
#endif
#endif

#ifndef included_f24rsub
#define included_f24rsub

f24rsub:
;-AHL + CDE ==> AHL
;Destroys BC,DE
;
  xor $80
#ifdef included_f24add
  jp f24add
#endif
#endif


#include "f24add.z80"
