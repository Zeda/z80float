#ifndef included_i16tof32
#define included_i16tof32
#include "pushpop.z80"

i16tof32:
;Inputs:
;   HL holds a 16-bit signed integer, (-32768 to 32767)
;   BC points to where to write the float
;Outputs:
;   Converts A to an f32 float at BC
;
  call pushpop

  xor a
  ld (bc),a
  inc bc

  ld a,l
  or h
  ld d,a
  jr z,i16tof32_finish

  ld a,h
  or a
  jp p,$+10
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  scf

  rla         ; save the sign
  ld d,$7F+16 ;Initial exponent

  dec d
  add hl,hl
  jr nc,$-2

  rra   ; shift out the sign
  rr d  ; shift the exponent down, shifting in the sign
  rr h  ; shift the lsb of the exponent into the significand
  rr l

  ld a,l
i16tof32_finish:
  ld (bc),a
  inc bc
  ld a,h
  ld (bc),a
  inc bc
  ld a,d
  ld (bc),a
  ret
#endif
