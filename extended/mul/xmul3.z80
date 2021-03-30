#ifndef included_xmul3
#define included_xmul3
#include "pushpop.z80"
#include "mov.z80"
#include "routines/rr64.z80"
#include "routines/add64.z80"

xmul3:
;535+{0,7+rr64}+{0,31}+2*mov10+mov8+adc64
;1365-{0,1}+{0,31}
;min: 1364scc
;max: 1396cc
;avg: 1380cc
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
  dec hl \ srl (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  ld de,xOP2
  ex de,hl
  call adc64
  ex de,hl
  push af
  call c,rr64
  ld hl,xOP1+8
  pop af
  ld a,(hl)
  adc a,1
  ld (hl),a
  ret nc
  inc hl
  ld a,(hl)
  inc (hl)
  xor (hl)
  ret p
constmul_overflow:
  xor $80
  ld (hl),a
  ld hl,xOP1+7
  ld (hl),-1
  ret
#endif
