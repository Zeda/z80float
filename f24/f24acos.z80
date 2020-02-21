#ifndef included_f24acos
#define included_f24acos

#include "f24sub.z80"
#include "f24bg.z80"
#include "f24sqr.z80"

f24acos:
;acos(AHL) ==> AHL
;sqrt(1-x^2)/BG(x,1)
;
;Future work:
;   Maybe we cantake advantage of:
;       acos(x) = pi/2 - asin(x)

;acos(-x) = pi - acos(x)

  rlca
  or a
  rra
  jr nc,+_
  call +_
  ld c,$40
  ld de,37408
  jp f24rsub
_:
;save x
  push hl
  push af

;sqrt(1-x^2)
  call f24sqr
  ld c,$3F
  ld de,0
  call f24rsub
  call f24sqrt

;restore x and push current
  pop bc
  ex (sp),hl
  push af
  ld a,b

;1/(BG(x,1)
  ld c,$3F
  ld de,0
  call f24bg

  pop bc
  pop de
  ld c,b
  jp f24mul
#endif
