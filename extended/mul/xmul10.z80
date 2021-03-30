#ifndef included_xmul10
#define included_xmul10
#include "pushpop.z80"
#include "mov.z80"
#include "mul/xOP1mul10.z80"
xmul10:
  call pushpop
  push bc
  ld de,xOP1
  call mov10
  call xOP1mul10
  ld hl,xOP1
  pop de
  jp mov10
#endif
