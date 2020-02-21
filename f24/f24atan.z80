#ifndef included_f24atan
#define included_f24atan

#include "f24sub.z80"
#include "f24bg.z80"
#include "f24sqr.z80"

f24atan:
;atan(AHL) ==> AHL
;Computed as x/BG(1.0,sqrt(1+x^2))
;

;atan(-x) = atan(x)
  rlca
  or a
  rra
  jr nc,+_
  call +_
  xor $80
  ret
_:

;If x>=1.0, calculate as pi/2-atan(1/x)
  cp 63
  jr c,+_
  call f24inv
  call +_
  ld c,$3F
  ld de,37408
  jp f24rsub
_:
  push af
  push hl
  call f24sqr
  ld c,$3F
  ld de,0
  call f24add
  call f24sqrt
  ex de,hl
  ld c,a
  ld a,$3F
  ld hl,0
  call f24bg

  pop de
  pop bc
  ld c,b
  jp f24mul
#endif
