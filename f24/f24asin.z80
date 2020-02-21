#ifndef included_f24asin
#define included_f24asin

#include "f24sub.z80"
#include "f24bg.z80"
#include "f24sqr.z80"

f24asin:
;asin(AHL) ==> AHL
;x/BG(sqrt(1-x^2),1)
;

;save x
  push hl
  push af

;sqrt(1-x^2)
  call f24sqr
  ld c,$3F
  ld de,0
  call f24rsub
  call f24sqrt

;if A is 0, this is actually a special value!
  add a,a
  jr nz,+_
  pop af
  pop hl
  ld hl,37408
  ;A is either 3F or BF, so we can keep it that way :)
  ret
_:
  rra

;1/BG(sqrt(1-x^2),1)
  ld c,$3F
  ld de,0
  call f24bg

;multiply by X
  pop bc
  pop de
  ld c,b
  jp f24mul
#endif
