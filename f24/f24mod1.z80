#ifndef included_f24mod1
#define included_f24mod1

f24mod1:
;AHL % 1 ==> AHL

; save A
  ld c,a

; 0 mod 1 is 0
  add a,a
  ret z

;inf and NaN mod 1 are NaN
  cp $FE
  rrca    ;A is now the exponent
  jr nz,+_
  ld h,a  ; sets HL to non-zero
  ret
_:

;if A<63, the input is already less than 1
  cp 63
  jr c,mod_finished

;if a>=63+16, then the input won't have enough bits for a fractional part
  sub 63+16
  add a,16
  jr c,+_
  xor a
  ret
_:
  ;A+1 is the number of bits to shift out of HL
  ld b,a
  jr z,+_
  add hl,hl
  djnz $-1
_:

;now need to renormalize
  ld a,h
  or l
  ret z
  ld a,63
  dec a
  add hl,hl
  jr nc,$-2
mod_finished:
;now if the top bit of C is set, then we still need to do 1.0-AHL
  sla c
  ret nc
  ld c,63
  ld de,0
  jp f24rsub
#endif
