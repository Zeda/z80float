#ifndef included_f32rand
#define included_f32rand
#include "pushpop.z80"
#include "rand.z80"

f32rand:
;Generates a pseudo-random number on [0,1) with uniform distribution.
  call pushpop
  push bc
;The first thing we'll do is generate the exponent.
;Initialize to -1 (stored as 0x7E) and we'll generate
;random bits, decrementing the exponent until we get a 1.

;we'll start at +2 to make detecting underflow easier
  ld a,$80    ;exponent
rand_gen_exp:
  push af
  call rand
  pop af
  ld b,16
_:
  dec a
  add hl,hl
  jr c,+_   ;we have completed calculation of the exponent
  djnz -_
; If we made it here, we need to generate more random bits to determine the
; exponent. We also need to make sure make sure the exponent isn't zero!
  jr nz,rand_gen_exp
  .db $FE   ;start of `cp *`, eats the next byte (dec a) so that A stays 0.
_:
; Now we have generated the exponent, let's generate the significand
  dec a
  push af
  call rand
  push hl
  call rand
  pop de
  ld b,h
  pop af
  pop hl
;B,D,E are random bytes, A is the exponent, HL is where to write
  ld (hl),e
  inc hl
  ld (hl),b
  inc hl
  srl a     ;shift in a 0 for the sign, shifting out the lsb of the exponent
  rr d      ;shift in the lsb of the exponent into the msb of the significand
  ld (hl),d
  inc hl
  ld (hl),a
  ret
#endif
