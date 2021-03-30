#ifndef included_xmod1
#define included_xmod1
#include "pushpop.z80"
#include "mov.z80"
#include "routines/sla64.z80"
#include "routines/normalizexOP1.z80"
#include "constantsx.z80"
#include "xadd.z80"


;This routine performs `x mod 1`, returning a non-negative value.
;+inf -> NaN
;-inf -> NaN
;NaN  -> NaN

xmod1:
  call pushpop
  push bc
  ld de,xOP1
  call mov10

;Take care of special cases
  ld hl,(xOP1+8)
  ld a,h
  and $7F
  ld h,a
  or l
  jp z,xmod1_special

;If H<0x40, then there is no integer part!
  ld a,h
  sub $40
  jr c,xmod1_end

;if A is non-zero, then this number is too big to have stored an integer part
  jp nz,xmod1_return_0

;If L is >=63, then this number is too big to have stored an integer part
  ld a,l
  cp 63
  jp nc,xmod1_return_0
  inc a
;Now we need to shift the mantissa up to remove the integer part
  cp 32
  jr c,+_
  sub 32
  ld hl,(xOP1+2) \ ld (xOP1+6),hl
  ld hl,(xOP1) \ ld (xOP1+4),hl
  ld hl,0
  ld (xOP1),hl \ ld (xOP1+2),hl
_:
  cp 16
  jr c,+_
  sub 16
  ld hl,(xOP1+4) \ ld (xOP1+6),hl
  ld hl,(xOP1+2) \ ld (xOP1+4),hl
  ld hl,(xOP1) \ ld (xOP1+2),hl
  ld hl,0
  ld (xOP1),hl
_:
  cp 8
  jr c,+_
  ld hl,(xOP1+5) \ ld (xOP1+6),hl
  ld hl,(xOP1+3) \ ld (xOP1+4),hl
  ld hl,(xOP1+1) \ ld (xOP1+2),hl
  ld hl,(xOP1)
  ld l,0
  ld (xOP1),hl
_:
  and 7
  jr z,xmod1_normalize
  ld b,a
_:
  call sla64_xOP1
  djnz -_
xmod1_normalize:
  ld a,(xOP1+9)
  add a,a
  ld hl,$7FFF
  rr h
  ld (xOP1+8),hl
  call normalizexOP1
xmod1_end:
;If it is negative, add 1
  ld a,(xOP1+9)
  add a,a
  jr nc,return_xOP1
  ld hl,xOP1
  ld de,xconst_1
  ld b,h
  ld c,l
  call xadd
return_xOP1:
  ld hl,xOP1
  pop de
  jp mov10
xmod1_special:
  ld a,(xOP1+7)
  add a,a
  jr nc,return_xOP1
  ld a,$40
  ld (xOP1+7),a
  jr return_xOP1
xmod1_return_0:
  xor a
  ld h,a
  ld l,a
  ld (xOP1+7),a
  ld (xOP1+8),hl
  jr return_xOP1
#endif
