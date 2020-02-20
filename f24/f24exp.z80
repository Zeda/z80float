#ifndef included_f24exp
#define included_f24exp

#include "f24div.z80"
#include "f24mul.z80"
#include "f24add.z80"

f24exp:

;range reduction!
  rlca
  or a
  rra
  jr nc,f24exp_pos
  call f24exp_pos
  jp f24inv

f24exp_pos:
  or a
  jr nz,+_
  ld h,a
  ld l,a
  ld a,$3F
  ret
_:
  cp $7F
  ret z

;multiply by 1/ln(2)
  ld c,$3F
  ld de,29012
  call f24mul

;now add .5
  ld c,$3E
  ld de,0
  call f24add

;now int(x) is how many powers of 2 to add to the end result
  ld bc,$3F00    ;B=exponent of the result, C=0 for later


  cp 63+7
  jr c,+_
  ld a,$7F
  ld h,c
  ld l,c
  ret
_:

  cp b
  jr c,f24exp_range_reduced
  inc c
  sub 63
  jr z,+_
  add hl,hl
  rl c
  dec a
  jr nz,$-4
_:
  ;add C to B
  ld a,b
  add a,c
  ld b,a
  cp $7F
  jr c,f24exp_norm
  ld a,$7F
  ld hl,0
  ret
f24exp_norm:
;gotta renormalize!
  ld a,h
  or l
  jr z,f24exp_range_reduced
  ld a,$3F
  dec a
  add hl,hl
  jr nc,$-2
f24exp_range_reduced:
;multiply by ln(2)
  push bc

;subtract .5
  ld c,$BE
  ld de,0
  call f24add

  ld c,$3E
  ld de,25316
  call f24mul

  ld c,a
  ex de,hl
  ld a,$3A \ ld hl,$5546
  push bc
  push de
  call f24mul
  ld c,$3C \ ld de,$57E9
  call f24add
  pop de
  pop bc

  push bc
  push de
  call f24mul
  ld c,$3E \ ld de,$0002
  call f24add
  pop de
  pop bc

  push bc
  push de
  call f24mul
  ld c,$3E \ ld de,$FFFB
  call f24add
  pop de
  pop bc

  call f24mul
  ld c,$3F \ ld de,0
  call f24add

  pop bc
  sub 63
  add a,b
  ret

#endif
