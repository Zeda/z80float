#ifndef included_f64tox
#define included_f64tox

#include "routines/rl64.z80"
#include "mov.z80"
#include "pushpop.z80"

f64tox:
;Inputs:
;   HL points to the input double-precision float
;   BC points to where to output the result
;Outputs:
;   The double-precision float (binary64) is converted to an extended-precision
;   float at BC.
;
  call pushpop
f64tox_nopush:
  ld d,b
  ld e,c


;bottom 8 bits are 0
  xor a
  ld (de),a
  inc de

;load the next 7 bytes
  call mov7
  ;load the upper 8 bits of the sign/exponent into c
  ld c,(hl)

;now shift the mantissa up 4 times
;lower 4 bits of BC contain the mantissa, upper 12 are the exponent and sign
  ld hl,-7
  ex de,hl
  add hl,de
  inc e
  rlc c   ;\
  srl c   ; |
  sbc a,a ; | Get the sign where it needs to be
  and 8   ; | also resets carry, helpfully
  ld b,a  ;/
                     call rl56 \ rl c \ rl b
  add hl,de \ or a \ call rl56 \ rl c \ rl b
  add hl,de \ or a \ call rl56 \ rl c \ rl b

;now the top bit of the mantissa contains the bottom bit of the exponent.
;we also need to replace that top bit with a 1
  ld a,(hl)
  rlca
  scf
  rra
  ld (hl),a
  rl c
  rl b

; BC is the input exponent, check if it is special
  ld a,b
  add a,a
  or c
  jr z,f64tox_zero

  ld a,c
  inc a
  jr nz,+_
  ld a,b
  inc a
  and 7
  jr z,f64tox_infnan

  ;now we need to subtract 1023 and add 16384
  ld a,(16384-1023)&255
  add a,c
  inc hl
  ld (hl),a

  ld a,(16384-1023)>>8
  adc a,b
  inc hl
  ld (hl),a
  ret

f64tox_zero:
  xor a
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),b
  ret
f64tox_infnan:
  or (hl)
  ld a,$80
  jr nz,+_
  scf
_:
  rra
  ld (hl),a
  xor a
  inc hl
  ld (hl),a
  inc hl
  rl b
  rra
  ld (hl),a
  ret
#endif
