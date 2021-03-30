#ifndef included_xamean
#define included_xamean
#include "pushpop.z80"
#include "mov.z80"
#include "xadd.z80"

xamean:
;229+{0(special case),17}+mov10+xadd
  call pushpop
  push bc
  ld bc,xOP1
  call xadd
  ld hl,(xOP1+8)
  ld a,h
  and $7F
  or l
  jr z,+_
  dec hl
  ld (xOP1+8),hl
_:
  ld hl,xOP1
  pop de
  jp mov10
#endif
