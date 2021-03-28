#ifndef included_randSingle
#define included_randSingle
#include "pushpop.z80"
#include "rand.z80"

randSingle:
;Generates a pseudo-random number on [0,1) with uniform distribution.

  call pushpop
  push bc

;The first thing we'll do is generate the exponent.
;Initialize to -1 (stored as 0x7F) and we'll generate
;random bits, decrementing the exponent until we get a 1.

  ld c,$80    ;exponent
  jr rand_gen_exp
_:
  dec c
  add hl,hl
  jr c,+_   ;we have completed calculation of the exponent
  djnz -_

;make sure the exponent isn't zero!
  inc c
  dec c
  jr z,rand_zero

rand_gen_exp:
  push bc
  call rand
  pop bc
  ld b,16
  jr -_
_:

; Now we have generated the exponent, let's generate the mantissa

  push bc
  call rand
  push hl
  call rand
  pop de
  pop bc
  ld b,h
;Now our float is stored in CBDE

; Make the float positive
  res 7,b

  .db $FE   ;start of `cp *` to skip `ld b,c`
rand_zero:
  ld b,c

  pop hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),b
  inc hl
  ld (hl),c
  ret
#endif
