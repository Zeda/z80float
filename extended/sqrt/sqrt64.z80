#ifndef included_sqrt64
#define included_sqrt64
#include "sqrt/sqrt32.z80"
#include "div/div32.z80"

sqrt64:
;avg: 7544.059294cc
;Speed: 106+{0,47}+{0,109+{0,18+{0,18+{0,18+{0,17}/256}/256}/256}}+sqrt32+div32_32
;min: 106+min(sqrt32)+min(div32_32)
;     4560cc
;max: 333+max(sqrt32)+max(div32_32)
;     6547cc
;avg: 188.517647+avg(sqrt32)+avg(div32_32)
;     5708.042cc

  call sqrt32
;AHLBC is the remainder

  rra
  rr h
  rr l
  rr b
  rr c
  rra
  jr nc,+_
  xor a
  ld d,a \ sub c \ ld c,a
  ld a,d \ sbc a,b \ ld b,a
  ld a,d \ sbc a,l \ ld l,a
  ld a,d \ sbc a,h \ ld h,a
_:
  push af
  ld d,b
  ld e,c
  call div32_32
  ;append to var_x
  pop af
  ret nc
  ld hl,var_x
  xor a
  ld b,a \ sbc a,(hl) \ ld (hl),a \ inc hl
  ld a,b \ sbc a,(hl) \ ld (hl),a \ inc hl
  ld a,b \ sbc a,(hl) \ ld (hl),a \ inc hl
  ld a,b \ sbc a,(hl) \ ld (hl),a
  ret nc
  inc hl \ dec (hl) \ ret nz
  inc hl \ dec (hl) \ ret nz
  inc hl \ dec (hl) \ ret nz
  inc hl \ dec (hl)
  ret
#endif
