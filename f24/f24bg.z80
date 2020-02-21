;This computes the inverse of the Borchardt-Gauss mean to adequate precision for
;24-bit floats. This is used for many of the inverse trancendental functions.
;
;The algorithm is fancy as frick, but at this low of precison, it boils down to:
;   b = (a+g)/2
;   g = sqrt(b*g)
;   c = (b+g)/2
;   return 45/(a-20b+64c)
;
;We'll optimize it for numerical stability:
;   b = (a+g)/2
;   g = sqrt(b*g)
;   return (45/32)/(a/32+3b/8+g)



#ifndef included_f24bg
#define included_f24bg

#include "f24amean.z80"
#include "f24add.z80"
#include "f24geomean.z80"
#include "f24div.z80"
#include "f24div_pow2.z80"
#include "f24mul3.z80"

f24bg:
;1/BG(AHL,CDE) ==> AHL
;
;save `A`
  push af
  push hl

;save `G`
  push bc
  push de

  call f24amean
  ;AHL is `B`

;pop G
  pop de
  pop bc

;save `B`
  push af
  push hl

  call f24geomean

;pop `B`
  pop de
  pop bc

;save `G`
  push af
  push hl

;B*3/8 ==> B
  ld a,b
  ex de,hl
  call f24mul3
  ld b,3
  call f24div_pow2


;pop `G`
  pop de
  pop bc
  ld c,b

;B+G ==> acc
  call f24add

;pop `A`
  pop de
  pop bc

;save `acc`
  push af
  push hl

;A/32 ==> A
  ld a,b
  ex de,hl
  ld b,5
  call f24div_pow2

;pop `acc`
  pop de
  pop bc
  ld c,b

;acc+A ==> acc
  call f24add

;return (45/32)/acc
  ex de,hl
  ld c,a
  ld a,$3F \ ld hl,26624  ;45/32
  jp f24div

#endif
