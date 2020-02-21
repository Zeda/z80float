#ifndef included_f24sin
#define included_f24sin

#include "f24cos.z80"
#include "f24sqr.z80"
#include "f24div.z80"
#include "f24mod1.z80"

f24sin:
;sin(AHL) ==> AHL

;save A
  ld b,a

;sin(0) == 0
  add a,a
  ret z

;sin(inf)==sin(NaN)==NaN
  rrca
  cp $7F
  jr nz,+_
  ld h,a
  ret
_:

  ld a,b
;Need to apply range reduction
; We want the input on [-pi/4,pi/4]
;multiply by 1/(2pi)
  ld c,$3C
  ld de,$45F3
  call f24mul

; Add .25
  ld c,$3D
  ld de,$0
  call f24add

;Now grab mod 1
  call f24mod1

  jp xcos_stepin

f24sin_range_reduced:
;multiply by 2pi
  ld c,$41
  ld de,$9220
  call f24mul

;x is on [0,pi/4]
;return x * (1 - x^2 * (0.16663360595703125 - x^2 * 8.1627368927001953125e-3)

;save x
  push hl
  push af

;-x^2
  call f24sqr
  xor $80

;save x^2
  push hl
  ld c,a
  push bc

;multiply by 8.1627368927001953125e-3
  ld c,$38
  ld de,$0B7A
  call f24mul

;add 0.16663360595703125
  ld c,$3C
  ld de,$5544
  call f24add

;multiply by -x^2
  pop bc
  pop de
  call f24mul

;add 1
  ld c,$3F
  ld de,$0
  call f24add

;multiply by x
  pop bc
  pop de
  ld c,b
  jp f24mul

#endif
