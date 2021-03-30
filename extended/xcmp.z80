#ifndef included_xabs
#define included_xabs
#include "mov.z80"
#include "xsub.z80"

xcmp:
;Input: DE points to float1, HL points to float2
;Output:
;      float1 >= float2 : nc
;      float1 <  float2 : c,nz
;      float1 == float2 : z
;  There is a margin of error allowed in the lower 2 bits of the mantissa.
;
;Currently fails when both numbers have magnitude less than about 2^-16322
  push hl
  push de
  push bc
  call +_
  pop bc
  pop de
  pop hl
  ret
_:
  push de
  ld de,xOP2
  call mov10
  pop hl
  call mov10

  ld hl,(xOP2+8)
  ld de,(xOP3+8)
  or a
  sbc hl,de
  add hl,de
  jr nc,$+3
  ex de,hl
  res 7,h
  push hl   ;exponent
  ld hl,xOP2
  ld de,xOP3
  ld b,h
  ld c,l
  call xsub
  pop hl
  ld de,(xOP2+8)
  ld a,d
  or e
  jr nz,+_
  ld a,(xOP2+7)
  or a
  ret
_:
  xor a
  sla d
  rra
  rr d
  sbc hl,de
  ;want HL>=62
  inc h
  dec h
  jr nz,+_
  ld h,a
  ld a,l
  cp 62
  ld a,h
  jr c,+_
  xor a
  ret
_:
  or 1
  rla
  ret
#endif
