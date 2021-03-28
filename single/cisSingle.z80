#ifndef included_cisSingle
#define included_cisSingle
#include "pushpop.z80"
#include "cosSingle.z80"
#include "mulSingle.z80"
#include "sqrtSingle.z80"
#include "rsubSingle.z80"

cisSingle:
; Computes cosine and sine
; Named after the reresentation, cis(x) = cos(x)+i*sin(x)
; This is like exp(i*x), but we are computing it as:
;   cos(x)+i*sqrt(1-cos(x)^2)
  call pushpop

;Compute cosine and store it back to BC
  call cosSingle

;Now we need to square this and store it to BC+4
  ld h,b
  ld l,c
  ld d,b
  ld e,c

;Advance BC by 10
  ld a,c
  add a,4
  ld c,a
  jr nc,+_
  inc b
_:

  call mulSingle

  ld de,const_1
  ld h,b
  ld l,c
  call rsubSingle

  jp sqrtSingle
#endif
