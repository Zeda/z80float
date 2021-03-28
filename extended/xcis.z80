#ifndef included_xcis
#define included_xcis
#include "pushpop.z80"
#include "xcos.z80"
#include "xmul.z80"
#include "xsqrt.z80"
#include "xrsub.z80"

xcis:
;; Computes cosine and sine
;; Named after the reresentation, cis(x) = cos(x)+i*sin(x)
;; This is like exp(i*x), but we are computing it as:
;;   cos(x)+i*sqrt(1-cos(x)^2)
  call pushpop

;Compute cosine and store it back to BC
  call xcos

;Now we need to square this and store it to BC+10
  ld h,b
  ld l,c
  ld d,b
  ld e,c

;Advance BC by 10
  ld a,c
  add a,10
  ld c,a
  jr nc,+_
  inc b
_:
  call xmul

  ld de,xconst_1
  ld h,b
  ld l,c
  call xrsub

  jp xsqrt
#endif
