#ifndef included_xmul
#define included_xmul
#include "pushpop.z80"
#include "mov.z80"
#include "mul/mul64.z80"
#include "routines/rl64.z80"

#define var_z xOP3+16
;uses 60 bytes after xOP1
xmul:
;Input:
;  HL points to one number
;  DE points to another
;Timing, excluding special cases (which take ~ 800cc):
;1057+{0,3}+{0,172}+mul64
;max: 1232+max(mul64)
;     11245cc
;min: 1057+min(mul64)
;     6688cc
;avg: 1144.5+avg(mul64)
;     9865.233ccs


  push hl
  push de
  push bc
  push af
  push ix
  push bc
  call +_
  pop hl
  push de
  ex de,hl
  ld hl,var_z+8
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
  push de
  ld de,xOP1
  call mov10
  pop hl
  call mov10
	ld de,(xOP2+8)
	ld hl,(xOP1+8)
xmul_stepin_geomean:
	ld a,h
	xor d
  ld b,a
	res 7,d
	res 7,h
	ld a,h \ or l \ jp z,casemul
	ld a,d \ or e \ jp z,casemul2
  add hl,de
  ld de,$4000
  sbc hl,de
  jp c,mul_zero
  jp m,mul_inf
  sla b
  jr nc,+_
  set 7,h
_:
  push hl
	call mul64
  ld a,(var_z+15)
  add a,a
  pop de
  jr c,+_
#ifdef inc_FMA
  ld hl,var_z
  call rl64
#else
  ld hl,var_z+7
  sla (hl)
#endif
  inc hl
  jp rl64

_:
  inc de
  ret

casemul:
;xOP1 is inf/nan/0
  ld hl,xOP2+9
  ld a,(hl)
  and $7F
  dec hl
  or (hl)
  dec hl
  ld a,(hl)
  ld hl,xOP1
  jr nz,casemul2_copy
  ;now we have two special cases to multipy together
;inf*inf-> inf
;0*0    -> 0
;
;nan*nan-> NaN
;inf*nan-> NaN
;inf*0  -> NaN
;nan*inf-> NaN
;nan*0  -> NaN
;0*inf  -> NaN
;0*nan  -> NaN

  sla b
  ld de,0
  rr d
  and $C0
  ld c,a
  ld a,(xOP1+7)
  and $C0
  cp c
  jr z,+_
  ld a,$40
_:
  ld (var_z+15),a
  ret
casemul2:
;finite times inf/nan/0, so xOP2 -> out
  ld hl,xOP2
casemul2_copy:
  ld de,var_z+8
  call mov8
  ld e,(hl)
  inc hl
  ld d,(hl)
  ret
mul_zero:
  xor a
  ld (var_z+15),a
  ld d,a
  ret
mul_inf:
  ld d,e
  ld a,255
  ld (var_z+15),a
  ret
#endif
