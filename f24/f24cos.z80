#ifndef included_f24cos
#define included_f24cos

#include "f24sin.z80"
#include "f24sqr.z80"
#include "f24mod1.z80"
#include "f24sub.z80"

f24cos:
;cos(AHL) ==> AHL

;cos(0) == 0
  add a,a
  ret z

;cos(inf)==cos(NaN)==NaN
  rrca
  cp $7F
  jr nz,+_
  ld h,a
  ret
_:

;multiply by 1/(2pi)
  ld c,$3C
  ld de,$45F3
  call f24mul

; Add .5
  ld c,$3E
  ld de,$0
  call f24add

;Now grab mod 1
  call f24mod1

xcos_stepin:
;subtract off the .5
  ld c,$BE
  ld de,$0
  call f24add

;now x is on [-.5,.5], but we need to evaluate cos(x*2pi) with x on [-.125,.125]
;We need to employ some identities
;  cos(-x)=cos(x)
;    make x positive
  and $7F

;  cos(x-pi)=-cos(x)
;   if our x is now on [.25,.5], then subtract x from .5 absolute value,
;   and return the negative result.
  cp $3D
  jr c,+_
  xor 80h
  ld c,$3E
  ld de,$0
  call f24add
  call +_
  xor 80h
  ret
_:


;  cos(pi/2-x)=sin(x)
;    if our x is now on [.125,.25], subtract it from .25 and feed it to the sine routine.
  cp $3C
  jr c,+_
  xor $80
  ld c,$3D
  ld de,$0
  call f24add
  jp f24sin_range_reduced
_:

f24cos_range_reduced:
;multiply by 2pi
  ld c,$41
  ld de,$9220
  call f24mul

;x is on [0,pi/4]
;retun 1 + x^2 * (-0.5 + x^2 * (4.1660785675048828125e-2 + x^2 * (-1.36436522006988525390625e-3)))

;-x^2
  call f24sqr
  xor $80

;save x^2
  push hl
  ld c,a
  push bc

;multiply by 1.36436522006988525390625e-3
  ld c,$35
  ld de,$65A9
  call f24mul

;add 4.1660785675048828125e-2
  ld c,$3A
  ld de,$5549
  call f24add

;multiply by -x^2
  pop bc
  pop de
  push de
  push bc
  call f24mul

;add .5
  ld c,$3E
  ld de,$0
  call f24add

;multiply by -x^2
  pop bc
  pop de
  call f24mul

;add 1
  ld c,$3F
  ld de,$0
  jp f24add
#endif
