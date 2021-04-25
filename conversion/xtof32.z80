#ifndef included_xtof32
#define included_xtof32
#include "pushpop.z80"

xtof32:
;Inputs:
;   HL points to the input extended-precision float
;   BC points to where to output the result
;Outputs:
;   The extended-precision float is converted to an f32 at BC.
;Destroys:
;   None
;

  call pushpop
xtof32_nopush:
; We don't need the first 5 bytes
  inc hl
  inc hl
  inc hl
  inc hl
  inc hl
  ld d,b
  ld e,c
  ldi
  ldi
  ld c,(hl)
  inc hl
  ld b,(hl)
  inc hl
  ld a,(hl)
;AB is the exponent and sign
  add a,a
  or b
  jr z,xtof32_special
  ld a,c
  ld (de),a
  inc de
  ld c,(hl)
  res 7,c

  ld a,b
  sub 129
  ld (de),a
  ld a,c
  sbc a,63
  jr c,xtof32_zero
  jr nz,xtof32_inf
  ld a,(de)
  inc a
  jr z,xtof32_inf
  ld a,(hl)
  add a,a ; get the sign
  ld a,(de)
  rra
  ld (de),a
  dec de
  ld a,(de)
  rla
  rrca
  ld (de),a
  ret

xtof32_zero:
  xor a
  ld (de),a
  dec de
  ld (de),a
  ret
xtof32_inf:
  ex de,hl
  ld a,(de)
  or %01111111
  ld (hl),a
  dec hl
  ld (hl),%10000000
  dec hl
  ld (hl),0
  dec hl
  ld (hl),0
  ret

xtof32_special:
  inc de
  ld a,c
  add a,a
  jr c,xtof32_inf
  jp p,xtof32_zero
xtof32_nan:
;significand needs to be non-zero to encode NaN
  ld a,(hl)
  or %01111111
  ld (de),a
  add a,a
  dec de
  ld (de),a
  ret
#endif
