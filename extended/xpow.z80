#ifndef included_xpow
#define included_xpow
#include "pushpop.z80"
#include "xmul.z80"
#include "xlg.z80"
#include "xpow2.z80"

xpow:
;;Computes x^y
;;HL points to y
;;DE points to x
;;BC points to output
  call pushpop
  push bc
  push de
  ld bc,xOP1
  call xlg
  pop de
  ld h,b
  ld l,c
  call xmul
  pop bc
  jp xpow2
#endif
