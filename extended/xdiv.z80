#ifndef included_xdiv
#define included_xdiv
#include "mov.z80"
#include "div/div64.z80"
#include "routines/cmp64.z80"

#define var_q xOP1
#define var_x xOP2
#define var_n xOP3
xdiv:
;597+{0,220+{0,6}}+{0,3}+div64+cmp64+mov8+2*mov10
;1075+{0,220+{0,6}}+{0,3}+div64+cmp64
;min: 1075+div64+cmp64
;     7800cc
;max: 1532+div64
;     13001cc
;avg: 1075+{0,220+{0,6}}+{0,3}+div64+cmp64
;     10971.151cc
  push hl
  push de
  push bc
  push af
  push ix
  push bc
  call +_
  ex (sp),hl
  ex de,hl
  ld hl,var_q
  call mov8
  ex de,hl
  pop de
  ld (hl),e
  inc hl
  ld (hl),d
  pop ix
  pop af
  pop bc
  pop de
  pop hl
  ret
_:
  push hl
  ex de,hl
  ld de,xOP2    ;denom
  call mov10
  pop hl
  call mov10
	ld hl,(xOP3+8) ;numer
	ld de,(xOP2+8) ;denom
	ld a,h
	xor d
;save the sign
  push af

	res 7,d
	res 7,h
	ld a,h \ or l \ jp z,casediv
	ld a,d \ or e \ jp z,casediv2
  ld bc,$3FFF
  add hl,bc
  sbc hl,de
  jp z,div_zero
  jp c,div_zero
  jp m,div_inf
  ;HL is the new exponent
  push hl
;Need to verify that mantissa var_n<var_x
  ld de,var_n+7
  ld hl,var_x+7
  call cmp64
  jr c,+_
  pop hl
  inc l
  jr nz,$+5
  inc h
  jr z,div_zero
  push hl
  ld hl,var_n+7
  srl (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl)
_:
  call div64
  pop hl
  sla h
  pop af
  add a,a
  rr h  
  ret
div_zero:
  xor a
  ld (xOP1+7),a
  ld l,a
  pop bc
  sla b
  rra
  ld h,a
  ret
div_inf:
  ld hl,0
  ld a,-1
  ld (xOP1+7),a
  pop bc
  sla b
  rr h
  ret
casediv:
;0/0   ==> NaN
;0/NaN ==> NaN
;0/x ==> 0
;inf/NaN ==> NaN
;inf/inf ==> NaN
;inf/x ==> inf
;NaN/x  ==> NaN

  ld a,(xOP3+7)
  and $C0
  ld a,d
  jr z,casediv_0
  jp p,div_NaN
;inf/NaN ==> NaN
;inf/inf ==> NaN
;inf/x ==> inf
  or e
  jr nz,div_inf
  ld a,(xOP2+7)
  and $C0
  jr z,div_inf
  jr div_NaN

casediv_0:
;0/0   ==> NaN
;0/NaN ==> NaN
;0/x ==> 0
  or e
  jr nz,div_zero
  ld a,(xOP2+7)
  and $C0
  jp m,div_zero
  jr div_NaN
casediv2:
;x/0   -> inf
;x/inf -> 0
;x/NaN -> NaN
  ld a,(xOP2+7)
  and $C0
  jr z,div_inf
  jp m,div_zero
div_NaN:
  pop bc
  ld hl,0
  ld a,$40
  ld (xOP1+7),a
  ret
#endif
