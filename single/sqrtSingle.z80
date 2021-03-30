#ifndef included_sqrtSingle
#define included_sqrtSingle
#include "pushpop.z80"
#include "mov4.z80"
#include "routines/sqrt24_mant.z80"
#include "constants.z80"

sqrtSingle:
;552+{0,19}+8{0,3+{0,3}}+pushpop+sqrtHLIX
;min: 1784
;max: 1987
;avg: 1872
; need to be recalculated, but guessing around +30cc
  call pushpop
  push bc
  ld b,(hl)
  inc hl
  ld e,(hl)
  inc hl
  ld a,(hl)
  add a,a
  jp c,sqrtSingle_NaN
  scf
  rra
  ld d,a
  inc hl
  ld a,(hl)
  or a
  jp z,sqrtSingle_special
  add a,80h
  ld c,0
  rra
  push af   ;new exponent
  jr c,+_
  srl d
  rr e
  rr b
  rr c
_:
  call sqrt24_mant

  pop bc
  ld a,l
  pop hl
  ;BDEA
  ld (hl),a
  inc hl
  ld (hl),e
  inc hl
  res 7,d
  ld (hl),d
  inc hl
  ld (hl),b
  ret
sqrtSingle_NaN:
  ld hl,const_NaN
  pop de
  jp mov4
sqrtSingle_special:
  dec hl
  dec hl
  pop de
  jp mov4
#endif
