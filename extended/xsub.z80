#ifndef included_xsub
#define included_xsub
#include "pushpop.z80"
#include "mov.z80"
#include "xadd.z80"

xsub:
;Input:
;  HL points to one number
;  DE points to another
;xadd+54
  call pushpop
  push bc
  call +_
  pop de
  ld hl,xOP3
  jp mov10
_:
;copy the inputs to xOP2 and xOP3, leaving xOP1 open for shifting
  push de
  ld de,xOP2
  call mov10
  pop hl
  call mov10
  dec de
  ld a,(de)
  xor 80h
  ld (de),a
  jp subadd_stepin

#endif
