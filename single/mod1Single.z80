#ifndef included_mod1Single
#define included_mod1Single
#include "pushpop.z80"
#include "addSingle.z80"
#include "constants.z80"

;This routine performs `x mod 1`, returning a non-negative value.
;+inf -> NaN
;-inf -> NaN
;NaN  -> NaN
mod1Single:
  call pushpop
  push bc
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld c,(hl)
  ld a,c
  xor 80h
  push af
  jp p,+_
  ld c,a
_:

  inc hl
  ld a,(hl)
  ld b,a
  or a
  jr z,mod1Single_special
  sub $80
  jr c,mod1_end
  inc a
  ld b,a
  ld a,c
  ex de,hl
_:
  add hl,hl
  rla
  djnz -_
  ld c,a

;If it is zero, need to set exponent to zero and return
  or h
  or l
  ex de,hl
  jr z,mod1_end

;Need to normalize
  ld b,$7F
  ld a,c
  or a
  jp m,mod1_end
  ex de,hl
_:
  dec b
  add hl,hl
  adc a,a
  jp p,-_
  ld c,a
  ex de,hl
mod1_end:
  pop af
  pop hl
  jp m,+_
  ;make sure it isn't zero else we need to add 1
  ld a,b
  or a
  jr z,+_
  ld (scrap),de
  ld (scrap+2),bc
  ld b,h
  ld c,l
  ld hl,scrap
  ld de,const_1
  jp addSingle
mod1Single_special:
;If INF, need to return NaN instead
;For 0 and NaN, just return itself :)
  pop af
  pop hl
  ld a,c
  add a,a
  jp p,+_
  ld c,$40
_:
  res 7,c
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),c
  inc hl
  ld (hl),b
  ret
#endif
