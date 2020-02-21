#ifndef included_f24cmp
#define included_f24cmp
#include "f24sub.z80"

f24cmp:
;returns the flags for float AHL minus float CDE
;   AHL >= CDE, nc
;   AHL < CDE,  c
;   AHL == CDE, z (and nc)
;
;Note:
;   This allows some wiggle room in the bottom two bits. For example, if the two
;   exponents are the same and the two significands differ by at most 3, they are
;   considered equal.
;
;Note:
;   NaN is a special case. This routines returns that NaN<x for all x.
;   This gives the weird property NaN<NaN, and when sorting, NaN will be the
;   smallest element.
;

;check for inf and NaN
  ld b,a
  and $7F
  inc a
  jp m,f24cmp_special
  ld a,b

;save the old exponent
  push af
  call f24sub

;restore the old exponent
  pop bc

; if 0, return equal
  xor 80h
  ret z
  xor 80h
  ret z

;if the difference was only in the bottom two bits, we'll call it good
;check if (B&7F)-(A&7F) >= 15
;check if (B&7F) > 14 + (A&7F)
  ld c,a    ;new exponent, need to save the sign for later comparison
  res 7,b
  and $7F
  add a,14
  sub b
  jr nc,$+4
  xor a
  ret

;otherwise, not equal, so let's return the sign in c and nz
  ld a,c
return_nz_sign_a:
  or $7F
  add a,a
  ret

f24cmp_special:
  ld a,h
  or l
  ccf
  ret nz

;so the first op is inf

;if second of is finite, return the sign of B in carry and nz

  ld a,c
  and $7F
  inc a
  ld a,b
  jp p,return_nz_sign_a

;second op is either NaN or inf
  ld a,d
  or e
  ret nz

; op1 op2 result
; 7F  7F  z, nc
; 7F  FF  nz,nc
; FF  7F  nz,c
; FF  FF  z, nc
  ld a,c
  cp b
  ret
#endif
