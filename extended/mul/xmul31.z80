#ifndef included_xmul31
#define included_xmul31
#include "pushpop.z80"
#include "mov.z80"
#include "routines/srl64_x4.z80"
#include "routines/srl64.z80"
#include "routines/sub64.z80"
#include "routines/normalizexOP1.z80"
#include "mul/xmul3.z80"
xmul31:
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
  call srlxOP2_4
  call srlxOP2
  ld de,xOP1
  call sbc64
  ld hl,xOP1+8
  ld a,(hl)
  add a,5
  ld (hl),a
  ret nc
  inc hl
  ld a,(hl)
  inc (hl)
  xor (hl)
  jp m,constmul_overflow
  ret
#endif
