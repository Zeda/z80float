#ifndef included_f24log
#define included_f24log

#include "f24bg.z80"

f24log:
;log(AHL) ==> AHL
;(x-1)/BG(.5(1+x), sqrt(x))

;ln(-x) == NaN
  ld b,a
  add a,a
  jr nc,+_
  sbc a,a
  ld h,a
  ret
_:

;ln(0) == -inf
  jr nz,+_
  ld h,a
  ld l,a
  dec a
  ret
_:

;ln(inf) == inf; ln(NaN) == NaN
  cp $FE
  jr nz,+_
  rra
  ret
_:

  push hl

;need to take the exponent, multiply by ln(2) to add at the end
;given A is non-zero and only the top 7 bits are needed
  sub 126
  push af
  jr nc,+_
  neg
_:

  ld de,45426 ;ln(2)*65536
  ld bc,$0600
  ld h,c
  ld l,c

  add a,a
  jr z,f24log_offset_calculated

_:
  add hl,hl
  rla
  jr nc,$+4
  add hl,de
  adc a,c
  djnz -_

;AHL is the significand
  ld c,a
  pop af
  ld b,126+16
  rr b
  ld a,c
_:
  dec b
  add hl,hl
  rla
  jr nc,-_

  sla l
  ld l,h
  ld h,a
  jr nc,+_
  inc l
  jr nz,+_
  inc h
  jr nz,+_
  inc b
_:

  ld a,b
  .db $FE
f24log_offset_calculated:
  pop af
  ex (sp),hl
  push af


  ld a,$3F
  push hl
  push af

  push hl
  push af
  call f24sqrt
  pop bc
  ex (sp),hl
  push af
  ld a,b
  ld c,$3F
  ld de,0
  call f24amean
  pop bc
  pop de
  ld c,b
  call f24bg

  pop bc
  ex (sp),hl
  push af
  ld a,b
  ld c,$BF
  ld de,0
  call f24add
  pop bc
  pop de
  ld c,b
  call f24mul

  pop bc
  pop de
  ld c,b
  jp f24add

#endif
