#ifndef included_TItox
#define included_TItox
#include "pushpop.z80"
#include "strtox.z80"

TItox:
;;converts a TI-float to a single precision float.
  call pushpop
  push bc

;Save the sign and exponent
  ld a,(hl)
  inc hl
  ld c,(hl)
  push af
  ld b,0
  ld a,c
  sub $7F
  ld c,a
  jr nc,+_
  dec b
_:
  push bc

;Convert 7 bytes of the mantissa (BCD) to an 8-bit integer on [0,99].
;TI's is big-endian and we want little endian copied to scrap
  ld de,xOP1+9
  ld b,7
_:
  inc hl
  ld a,(hl)
  and $F0
  rra
  ld c,a
  rra
  rra
  sub c
  add a,(hl)
  ld (de),a
  dec de
  djnz -_

;Load the next 3 bytes with zeros
  xor a
  ld (de),a
  dec de
  ld (de),a
  dec de
  ld (de),a
  pop bc

;Pass off to the strtox routine
  jp TItox_stepin
#endif
