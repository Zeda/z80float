#ifndef included_xmul7
#define included_xmul7
#include "pushpop.z80"
#include "mov.z80"
#include "routines/srl64.z80"
#include "routines/rsub64.z80"
#include "routines/normalizexOP1.z80"
#include "mul/xmul3.z80"

xmul7:
  call pushpop
  push bc
  call +_
  call normalizexOP1
  pop de
  ld hl,xOP1
  jp mov10
_:
  ld de,xOP1
  call mov10
  ld hl,(xOP1+8)
  ld a,h
  or l
  ret z
  ld hl,xOP1
  call mov8
  call srlxOP1_mantissa
  call srlxOP1_mantissa
  call srlxOP1_mantissa
  ld de,xOP2
  call rsbc64
  ld hl,xOP1+8
  ld a,(hl)
  add a,3
  ld (hl),a
  ret nc
  inc hl
  ld a,(hl)
  inc (hl)
  xor (hl)
  jp m,constmul_overflow
  ret
#endif
