#ifndef included_xadd
#define included_xadd
#include "pushpop.z80"
#include "mov.z80"
#include "routines/swapxOP2xOP3.z80"
#include "routines/sub64.z80"
#include "routines/add64.z80"

xadd:
;Input:
;  HL points to one number
;  DE points to another
;  BC points to output
;945
;+{0,57+swapxOP2xOP3}
;+{0,123+{0,249}+{0,430}+{0,210}+21*n+{0,232-26n}}, n from 0 to 9
;+{sub,add}
;sub:
;  84+{0,256}+sbc64  ;there is a 25% chance of it going here, I believe
;  {0,333+{0,7+13+{0,7+13+{0,7+13+{0,7+13+{0,7+13+{0,7+13+{0,29}}}}}}}}   ;this part happens at most once (50%) unless inputs have the same exponent, then it is about 8/3 (accurate to 17 digits)
;add:
;  69+adc64+{0,201+{0,39}
;avg: 2111.3076938cc, I think. A lot of weird probability.
  call pushpop
  push bc
  call +_
  pop de
  ld hl,xOP3
  jp mov10
_:
;copy the inputs to xOP2 and xOP3, leaving xOP1 open for shifting
  push de
  ld de,xOP2
  call mov10
  pop hl
  call mov10
subadd_stepin:
	ld de,(xOP2+8)
	ld hl,(xOP3+8)
  res 7,h
  res 7,d
  xor a
  ld (xOP2-1),a
  ld a,h
  or l
  jp z,caseadd1
  ld a,d
  or e
  jp z,caseadd
; Now make sure xOP3 has the bigger exponent
  sbc hl,de
  jr nc,+_
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  push hl
  call swapxOP2xOP3   ;need to swap xOP2 and xOP3
  pop hl
_:
  ld a,h
  or a
  ret nz
  ld a,l
  cp 66
  ret nc
;Now we need to shift down by A bits.
  or a
  jr z,add_shifted
  rra \ call c,srlxOP2_mantissa
  rra \ call c,srl2xOP2_mantissa
  rra \ call c,srl4xOP2_mantissa
  and $1F
  ld l,a
  ld bc,(xOP2&255)-1
  ld h,xOP2>>8
  add hl,bc
  sub 10
  cpl
  ld c,a
  ld de,xOP2-1
  ldir
  ld c,a
  ld a,9
  sub c
  jr z,add_shifted
  ld b,a
  xor a
  ld (de),a \ inc de \ djnz $-2
add_shifted:
;If the signs match, then just add
;If they differ, then subtract
	ld hl,xOP2+9
	ld a,(xOP3+9)
  xor (hl)
  jp p,xadd_add
;subtract the mantissas
  xor a
  ld hl,xOP2-1
  sub (hl)
  ld (hl),a
  inc hl
  ld de,xOP3
  call sbc64
  jr nc,+_
  ;now we need to negate the mantissa, invert the sign
  inc de
  inc de
  ld a,(de)
  xor 80h
  ld (de),a
  ld hl,xOP2-1
  xor a
  ld c,a
  sub (hl)
  ld (hl),a
  ld hl,xOP3
  ld a,c \ sbc a,(hl) \ ld (hl),a
  inc hl \ ld a,c \ sbc a,(hl) \ ld (hl),a
  inc hl \ ld a,c \ sbc a,(hl) \ ld (hl),a
  inc hl \ ld a,c \ sbc a,(hl) \ ld (hl),a
  inc hl \ ld a,c \ sbc a,(hl) \ ld (hl),a
  inc hl \ ld a,c \ sbc a,(hl) \ ld (hl),a
  inc hl \ ld a,c \ sbc a,(hl) \ ld (hl),a
  inc hl \ ld a,c \ sbc a,(hl) \ ld (hl),a
_:
  ret m
;need to shift up until top bit is 1. Should be at most 1 shift, I think


  ld de,(xOP3+8)
  ld a,(xOP2-1)
  ld hl,xOP3-1
  ld (hl),a
;We need to make sure that the mantissa isn't zero
  inc hl \ or (hl) \ jr nz,+_
  inc hl \ or (hl) \ jr nz,+_
  inc hl \ or (hl) \ jr nz,+_
  inc hl \ or (hl) \ jr nz,+_
  inc hl \ or (hl) \ jr nz,+_
  inc hl \ or (hl) \ jr nz,+_
  inc hl \ or (hl) \ jr nz,+_
  inc hl \ or (hl) \ jr nz,+_
  ld h,a
  ld l,a
  ld (xOP3+8),hl
  ret
add_zero:
  ld (xOP3+7),a
  ld h,a
  ld l,a
  ld (xOP3+8),hl
  ret
_:
  dec de
  ld a,d
  and $7F
  or e
  jr z,add_zero

  ld hl,xOP3-1
  sla (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl)
  jp p,-_
  ld (xOP3+8),de
  ret
xadd_add:
  ;add the mantissas
  ld hl,xOP2-1
  rl (hl)
  inc hl
  ld de,xOP3
  call adc64
  ret nc
  ex de,hl
  inc hl
  inc (hl) \ jr nz,+_
  inc hl
  inc (hl)
  ld a,(hl)
  dec hl
  and $7F
  jr z,add_inf
  scf
_:
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  dec hl \ rr (hl)
  ret
srl4xOP2_mantissa:
;242cc
  ld hl,xOP2+7
  ld b,a
  xor a
  rrd \ dec hl
  rrd \ dec hl
  rrd \ dec hl
  rrd \ dec hl
  rrd \ dec hl
  rrd \ dec hl
  rrd \ dec hl
  rrd \ dec hl
  rrd
  ld a,b
  ret
srl2xOP2_mantissa:
;423
  call srlxOP2_mantissa
srlxOP2_mantissa:
;203
  ld hl,xOP2+7
  srl (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl)
  ret
add_inf:
  ld (xOP3+7),a
  ld hl,-1
  ld (xOP3+8),hl
  ret

caseadd:
;OP2 is special, OP3 is not
;zero+x => x for all x
;NaN +x => NaN for all x
;inf +x => inf, x != inf
  ld a,(xOP2+7)
  and $C0
  ret z
xadd_return_xOP2:
  pop hl    ;pop the return
  pop de    ;pop the pointer to the output
  ld hl,xOP2
  jp mov10


caseadd1:
;OP3 is special, OP2 is unknown
;x+zero => x
;x+inf  => inf
;x+NaN  => NaN
;return result in xOP3
  ld a,(xOP3+7)
  and $C0
  jr z,xadd_return_xOP2   ;xOP3 is 0, so return xOP2
  ret p   ;NaN+x == NaN, NaN in xOP3 so return

;if xOP2 is NaN or -inf, return NaN
;otherwise, return xOP2
  ld a,d
  or e
  ret nz
  ld a,(xOP2+7)
  and $C0
  ret z
  jp p,xadd_return_NaN
;both inputs are inf, so make sure signs match
  ld a,(xOP3+9)
  ld d,a
  ld a,(xOP2+9)
  xor d
  ret p
xadd_return_NaN:
  pop hl
  pop de
  ld hl,xconst_NaN
  jp mov10

#endif
