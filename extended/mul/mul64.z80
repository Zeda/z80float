#ifndef included_mul64
#define included_mul64
#include "mov.z80"
#include "mul/mul32.z80"

#define var_z xOP3+16
#define z0_64 var_z
#define z2_64 z0_64+8
#define z0_32 z2_64+8
#define z2_32 z0_32+4

mul64:
;multiplies the 64-bit integers at xOP1 and xOP2
;min: 1740+3*min(mul32)
;     5631cc
;max: 1901+3*max(mul32)
;     10013cc
;avg: 1797+3*avg(mul32) + 9572881/2^24
;   :~8720.733cc

  ld de,(xOP1+6)
  ld hl,(xOP1+4)
  ld bc,(xOP2+6)
  ld ix,(xOP2+4)
  call mul32
  ;copy the 8 bytes at z0_32 to z2_64
  ld hl,z0_32
  ld de,z2_64
  call mov8


  ld de,(xOP1+2)
  ld hl,(xOP1)
  ld bc,(xOP2+2)
  ld ix,(xOP2)
  call mul32
  ;copy the 8 bytes at z0_32 to z0_64
  ld hl,z0_32
  ld de,z0_64
  call mov8

;now I need to subtract the 32-bit digits from each other
  xor a
  ld hl,(xOP1)
  ld bc,(xOP1+4)
  sbc hl,bc
  ex de,hl
  ld hl,(xOP1+2)
  ld bc,(xOP1+6)
  sbc hl,bc
  jr nc,+_
  ld b,a \ sub e \ ld e,a
  ld a,b \ sbc a,d \ ld d,a
  ld a,b \ sbc a,l \ ld l,a
  ld a,b \ sbc a,h \ ld h,a
  ld a,b
_:
  rla
  push hl   ;top byte
  push de

  ld hl,(xOP2)
  ld bc,(xOP2+4)
  sbc hl,bc
  ex de,hl
  ld hl,(xOP2+2)
  ld bc,(xOP2+6)
  sbc hl,bc
  jr nc,+_
  ld c,a
  xor a
  ld b,a
  sub e \ ld e,a
  ld a,b \ sbc a,d \ ld d,a
  ld a,b \ sbc a,l \ ld l,a
  ld a,b \ sbc a,h \ ld h,a
  ld a,c
  inc a
_:
  ex de,hl
  pop ix
  pop bc
  push af
  call mul32
  pop af    ;holds the sign in the low bit

  rra
  jp c,mul64_add
;need to perform z0+z2-result
  xor a
  ld hl,(z0_64)
  ld de,(z2_64)
  add hl,de
  ld (xOP1),hl
  ld hl,(z0_64+2)
  ld de,(z2_64+2)
  adc hl,de
  ld (xOP1+2),hl
  ld hl,(z0_64+4)
  ld de,(z2_64+4)
  adc hl,de
  ld (xOP1+4),hl
  ld hl,(z0_64+6)
  ld de,(z2_64+6)
  adc hl,de
  ld (xOP1+6),hl
  rla
;now need to subtract
  ld hl,(xOP1)
  ld de,(z0_32)
  sbc hl,de
  ld (xOP1),hl
  ld hl,(xOP1+2)
  ld de,(z0_32+2)
  sbc hl,de
  ld (xOP1+2),hl
  ld hl,(xOP1+4)
  ld de,(z0_32+4)
  sbc hl,de
  ld (xOP1+4),hl
  ld hl,(xOP1+6)
  ld de,(z0_32+6)
  sbc hl,de
  ld (xOP1+6),hl
  sbc a,0
mul64_final:
;now need to add it back in
  ld hl,(z0_64+4)
  ld de,(xOP1)
  add hl,de
  ld (z0_64+4),hl
  ld hl,(z0_64+6)
  ld de,(xOP1+2)
  adc hl,de
  ld (z0_64+6),hl
  ld hl,(z0_64+8)
  ld de,(xOP1+4)
  adc hl,de
  ld (z0_64+8),hl
  ld hl,(z0_64+10)
  ld de,(xOP1+6)
  adc hl,de
  ld (z0_64+10),hl
  ld hl,z0_64+12
  adc a,(hl)
  ld (hl),a
  ret nc
  inc hl \ inc (hl) \ ret nz
  inc hl \ inc (hl) \ ret nz
  inc hl \ inc (hl) \ ret
mul64_add:
;add to the current result
;z0+z2+result
  xor a
  ld hl,(z0_64)
  ld de,(z2_64)
  add hl,de
  ld (xOP1),hl
  ld hl,(z0_64+2)
  ld de,(z2_64+2)
  adc hl,de
  ld (xOP1+2),hl
  ld hl,(z0_64+4)
  ld de,(z2_64+4)
  adc hl,de
  ld (xOP1+4),hl
  ld hl,(z0_64+6)
  ld de,(z2_64+6)
  adc hl,de
  ld (xOP1+6),hl
  rla
;now need to subtract
  ld hl,(xOP1)
  ld de,(z0_32)
  add hl,de
  ld (xOP1),hl
  ld hl,(xOP1+2)
  ld de,(z0_32+2)
  adc hl,de
  ld (xOP1+2),hl
  ld hl,(xOP1+4)
  ld de,(z0_32+4)
  adc hl,de
  ld (xOP1+4),hl
  ld hl,(xOP1+6)
  ld de,(z0_32+6)
  adc hl,de
  ld (xOP1+6),hl
  adc a,0
  jp mul64_final
#endif
