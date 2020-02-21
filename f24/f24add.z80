#ifndef included_f24add
#define included_f24add

f24add:
;AHL + CDE ==> AHL
;Destroys BC,DE
;
;save A
  ld b,a

;check for special values
  and $7F
#ifdef included_return_CDE
  jp z,return_CDE
#else
#define included_return_CDE
  jr nz,+_
return_CDE:
  ld a,c
  ex de,hl
  ret
_:
#endif
  inc a
  jp m,f24add_op1_inf_nan

  ld a,c
;check for special values
  and $7F
  jp z,return_exp_b

  inc a
  jp m,return_CDE


  ld a,b
  xor c
  jp m,f24add_subtract
;we need to add

  call f24add_reorder
  jr z,f24add_add_same_exp
  ret nc
  push bc
  call rshift_1DE
  sla b
  adc hl,de
  ;if carry is reset, then we are all good :)
  pop de
  ld a,d
  ret nc
;otherwise, we need to increment the sign and see if it overflows to inf
  and $7F
  cp $7E
  ld a,d
  jr z,f24_return_inf
  inc a

;we also need to shift a 0 down into the HL
  srl h
  rr l
  ret nc
  inc hl
  ret

f24add_add_same_exp:
  ld a,b
  and $7F
  cp $7E
  ld a,b
  jr z,f24_return_inf
  inc a
  add hl,de
  rr h
  rr l
  ret nc
  inc l
  ret nz
  inc h
  ret nz
  inc a
  ret

f24_return_inf:
  or %01111111
  ld hl,0
  ret


f24add_subtract:
  call f24add_reorder
  jr z,f24add_subtract_same_exp
  ret nc
  push bc
  call rshift_1DE
  sub c
  ld c,a
  ld a,0
  sbc a,b
  ld b,a
  sbc hl,de
  ;if carry is not set, then we are all good :)
  pop de
  ld a,d
  ret nc

  ;otherwise, the implicit bit is set to 0, so we need to renormalize
normalize_D_HLBC:
;D is the sign+exponent
;HLBC is the significand
;returns AHLBC
  ;make sure HLBC is not 0
  ld a,h
  or l
  or b
  or c
  ret z

  ld a,d
normalize_D_HLBC_nonzero:
  ;save the sign
  add a,a
  push af
  rrca

_:
  dec a
  jr z,+_
  sla c
  rl b
  adc hl,hl
  jp nc,-_
  ;now round
  sla c
  ld bc,0
  adc hl,bc
  ;if carry is set, then the implicit bit is 2, and the rest of the exponent is 0
  ;so we can just increment A and keep HL as 0
  adc a,b
  add a,a
_:
  ld d,a
  pop af
  ld a,d
  rra
  ret

f24add_subtract_same_exp:
;subtract the significands
  ld a,b
;  or a
  sbc hl,de

;if zero, then the result is zero, but we'll keep the same sign
  jr nz,$+5
  and %10000000
  ret

  ;if the carry flag is set, then we need to change the sign of the output
  ;and negate the significand. if reset, then we still need to normalize and whatnot
  ld bc,0
  jr nc,normalize_D_HLBC_nonzero
  xor $80
  ld d,a
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  ld a,d
  jr normalize_D_HLBC_nonzero

f24add_reorder:
  xor c
  rlc c
  rla
;Want to rearrange so that A-C>=0
  sub c
  ret z
  jr nc,+_
  neg
  ;A is the difference in exponents
  rrc c
  ld b,c
  ex de,hl
_:
;A is how many bits to shift DE right
;B is the sign+exponent of the result
  or a
  rra
  cp 18
  ret c
return_exp_b:
  ld a,b
  ret

f24add_op1_inf_nan:
  ld a,h
  or l
  jr nz,return_exp_b
;so op1 is +inf or -inf
;If op2 is finite, then just return op1
  or c
  jr z,return_exp_b
  inc a
  add a,a
  jr nz,return_exp_b

;if op2 is NaN, return NaN
  ld a,d
  or e
  ld a,c
  jr nz,+_

;so |op1| and |op2| are inf
;if they have the same sign, fine, else return NaN
  cp b
  ret z
_:
  dec hl
  ret

rshift_1DE:
  ld bc,0
  scf
_:
  rr d
  rr e
  rr b
  rr c
  dec a
  jr nz,-_
  ret

#endif
