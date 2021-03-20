#ifndef included_f24mul
#define included_f24mul
#include "mul16.z80"

f24mul:
;AHL * CDE ==> AHL
;Destroys BC,DE
;

;put the output sign in the top bit of A
  ld b,a
  ld a,c
  and $80
  xor b

;check for special values
;NaN*x ==> NaN
;0*fin ==> 0
;0*inf ==> NaN
;inf*fin ==> inf
;inf*inf ==> inf

;save A
  ld b,a
  and $7F
  jr z,f24mul_op1_0
  inc a
  jp m,f24mul_op1_inf_nan

;so the first value is finite
  ld a,c
  and $7F
  ld c,a
  ret z
  inc a
#ifdef included_return_CDE
  jp m,return_CDE
#else
#define included_return_CDE
  jp p,+_
return_CDE:
  ld a,c
  ex de,hl
  ret
_:
#endif

;upper bit of B is the output sign
;first approximation of the exponent is
; (B&7F) + (C&7F) - 63
  ld a,b
  and $7F
  add a,c
  sub 63
  jr nc,$+4
  xor a     ;underflowed, so return 0
  ret

  cp $7F
  jr c,+_
f24mul_return_inf:
  ld a,b
  or %01111111
  ld hl,0   ;overflow so return inf
  ret
_:

  xor b
  and $7F
  xor b
f24mul_significand:
;save the exponent
  push af

;now compute (1.HL * 1.DE)
; = (1+.HL)(1+.DE)
; = 1+.HL+.DE+.HL*.DE
  ld b,h
  ld c,l
  push hl
  push de
  call mul16
  ;result is .DEHL
  ;we can discard HL, but first round
  xor a
  sla h
  ex de,hl
  pop bc
  adc hl,bc
  adc a,0
  pop bc
  add hl,bc
  adc a,0
  rra
;now 1+A.HL is the significand
  pop bc    ;B is the exponent
  ld a,b
  ret z
  ccf
  rr h
  rr l
  inc a
  inc a
  add a,a
  jr z,f24mul_return_inf
  rra
  dec a
  ret

f24mul_op1_0:
  ld a,c
  and $7F
  ret z
  inc a
  jp m,f24mul_return_NaN
  xor a
  ret

f24mul_op1_inf_nan:
  ld a,h
  or l
  ld a,b
  ret nz    ;NaN

;inf*0 is NaN
  ld a,c
  and $7F
  jr nz,+_
f24mul_return_NaN:
  dec a   ;inf*0
  ld h,a  ;=
  ld l,a  ;NaN
  ret
_:
  inc a
  jp m,+_
  ld a,b    ;returning inf
  ret
_:

;op1 is inf
;op2 is is either NaN or inf
; inf*NaN ==> NaN
; inf*inf ==> inf
;so just return op2's significand
  ld a,c
  ex de,hl
  ret

#endif
