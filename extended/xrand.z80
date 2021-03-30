#ifndef included_xrand
#define included_xrand
#include "pushpop.z80"
#include "rand.z80"
#include "mov.z80"
#include "constantsx.z80"

xrand:
;Stores a pseudo-random number on [0,1) with uniform distribution.
;speed: 312+pushpop+m*40+n*(67+rand)+4*rand
;          n is at least 1
;          m is the number of random bits that we had to generate
;          probability that n <= k is 1-65536^-k
;          probability that n == k is 65535*65536^-k
;          probability that m == k is 2^-k
;
;min: 2160cc
;max:~1056448cc  (absurdly unlikely to happen before heatdeath of the universe).
;avg: 2200.00595102cc
;85 bytes.

  call pushpop
  push bc

;The first thing we'll do is generate the exponent.
;Initialize to 0 (stored as 0x4000) and we'll generate
;random bits, decrementing the exponent until we get a 1.

  ld bc,$4000    ;exponent
  jr xrand_gen_exp
_:
  dec bc
  add hl,hl
  jr c,+_   ;we have completed calculation of the exponent
  dec a
  jr nz,-_

;make sure the exponent isn't zero!
  ld a,b
  or c
  jr z,xrand_zero

xrand_gen_exp:
  push bc
  call rand
  pop bc
  ld a,16
  jr -_
_:

; Now we have generated the exponent, let's generate the mantissa
  pop ix    ;pointer to the output
  ld (ix+8),c
  ld (ix+9),b


  call rand
  ld (ix),h
  ld (ix+1),l

  call rand
  ld (ix+2),h
  ld (ix+3),l


  call rand
  ld (ix+4),l   ;it's "random" anyways, just fun to change it up :P
  ld (ix+5),h

  call rand
  ld (ix+6),h
  set 7,l
  ld (ix+7),l

  ret

xrand_zero:
  pop de
  ld hl,xconst_0
  jp mov10
#endif
