#ifndef included_cmpSingle
#define included_cmpSingle
#include "subSingle.z80"

cmpSingle:
;Input: DE points to float1, HL points to float2
;Output:
;      float1 >= float2 : nc
;      float1 <  float2 : c,nz
;      float1 == float2 : z
;  There is a margin of error allowed in the lower 2 bits of the mantissa.
;
;Currently fails when both numbers have magnitude less than about 2^-106
  push hl
  push de
  push bc
  call +_
  pop bc
  pop de
  pop hl
  ret
_:
  inc de
  inc de
  inc de
  ld a,(de)
  inc hl
  inc hl
  inc hl
  cp (hl)
  jr nc,+_
  ld a,(hl)
_:
  dec hl
  dec hl
  dec hl
  dec de
  dec de
  dec de
  push af
  ld bc,scrap
  call subSingle
  ld a,(scrap+3)    ;new power
  pop bc            ;B is old power
  or a
  jr z,cmp_close
  sub b
  jr nc,cmp_is_sign
  dec a
  add a,22
  jr nc,cmp_close
cmp_is_sign:
  ld a,(scrap+2)
  or 1    ;not equal, so reset z flag
  rla     ;if negative, float1<float2, setting c flag as wanted, else nc.
  ret
cmp_close:
  xor a
  ret
#endif
