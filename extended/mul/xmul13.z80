#ifndef included_xmul13
#define included_xmul13
#include "pushpop.z80"
#include "mov.z80"
#include "routines/srl64.z80"
#include "routines/addmantissa0102.z80"
#include "mul/xmul3.z80"

xmul13:
  call pushpop
  push bc
  call +_
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
  call srlxOP2
  call addmantissa0102
  call srlxOP2
  call srlxOP2
  call addmantissa0102
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
