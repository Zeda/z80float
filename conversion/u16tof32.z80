#ifndef included_u16tof32
#define included_u16tof32
#include "pushpop.z80"

u16tof32:
;Inputs:
;   HL holds a 16-bit unsigned integer, (0 to 65535)
;   BC points to where to write the float
;Outputs:
;   Converts HL (unsigned) to an f32 float at BC
;
  call pushpop

  xor a
  ld (bc),a
  inc bc

  ld a,l
  or h
  ld d,a
  jr z,u16tof32_finish

  ld d,$7F+16 ;Initial exponent

  dec d
  add hl,hl
  jr nc,$-2

  srl d ; shift the exponent down, shifting in the sign
  rr h  ; shift the lsb of the exponent into the significand
  rr l

  ld a,l
u16tof32_finish:
  ld (bc),a
  inc bc
  ld a,h
  ld (bc),a
  inc bc
  ld a,d
  ld (bc),a
  ret
#endif
