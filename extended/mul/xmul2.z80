#ifndef included_xmul2
#define included_xmul2
#include "pushpop.z80"
#include "mov.z80"
xmul2:
  call pushpop
  ld d,b
  ld e,c
  call mov8
  ld c,(hl)
  inc hl
  ld b,(hl)
  inc c
  jr nz,+_
  ld a,b
  inc b
  xor b
  jp m,+_
  xor b
  sla b
  rla
  rr b
  ;ld a,$80  ;If this overflow occurs, then A must currently be %1111111x :D
  dec de
  ld (de),a
  inc de
_:
  ex de,hl
  ld (hl),c
  inc hl
  ld (hl),b
  ret
#endif
