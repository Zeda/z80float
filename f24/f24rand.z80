#ifndef included_f24rand
#define included_f24rand
#include "rand.z80"

f24rand:
;Generates a pseudo-random number on [0,1) with uniform distribution.

;The first thing we'll do is generate the exponent.
;Initialize to -1 (stored as 0x3E) and we'll generate
;random bits, decrementing the exponent until we get a 1.

;we'll start at +2 to make detecting underflow easier
  ld a,$40    ;exponent
  jr rand_gen_exp
_:
  dec a
  add hl,hl
  jr c,+_   ;we have completed calculation of the exponent
  djnz -_

;make sure the exponent isn't zero!
  ret z

rand_gen_exp:
  push af
  call rand
  pop af
  ld b,16
  jr -_
_:

; Now we have generated the exponent, let's generate the significand
  push af
  call rand
  pop af
  dec a
  ret
#endif
