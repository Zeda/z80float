#ifndef included_f32tox
#define included_f32tox
#include "pushpop.z80"

f32tox:
;convert an IEEE-754 binary32 to an extended-precision float.
;Input: HL points to the input float, BC points to where to output
;Destroys: None
  call pushpop
  ld d,b
  ld e,c
  xor a
  ld (de),a
  inc de
  ld (de),a
  inc de
  ld (de),a
  inc de
  ld (de),a
  inc de
  ld (de),a
  inc de
  ldi
  ldi
  ld a,(hl)
  inc hl
  ld c,a
  or %10000000
  ld (de),a
  inc de
  ld a,c
  add a,a
  ld a,(hl)
  adc a,a
  jr z,f32tox_return_0
  inc a
  jr z,f32tox_return_infnan
;A-128+16384 is the exponent
  rr c    ; save the sign
  sub 128
  ld (de),a
  inc de
  ld a,%10000000
  sbc a,0
  rl c
  rra
  ld (de),a
  ret

f32tox_return_infnan:
  rr c  ; save the sign
  ex de,hl
  dec hl
  ld a,(hl)
  add a,a
  dec hl
  or (hl)
  dec hl
  or (hl)
  inc hl
  inc hl
  sub 1   ; if A was 0 (inf),sets carry, else resets
  ld a,$80
  rra
  ld (hl),a
  xor a
  ex de,hl
  rl c  ; restore the sign
  .db 1 ; start of `ld bc,**` to eat the next two bytes
f32tox_return_0:
  dec de
  ld (de),a
  inc de
  ld (de),a
  inc de
  rra
  ld (de),a
  ret
#endif
