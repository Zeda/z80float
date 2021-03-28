#ifndef included_logSingle
#define included_logSingle
#include "pushpop.z80"
#include "divSingle.z80"
#include "lnSingle.z80"
logSingle:
  call pushpop
  call lnSingle
  push bc
  ld bc,scrap+5
  ex de,hl
  call lnSingle
  ld d,b
  ld e,c
  pop hl
  ld b,h
  ld c,l
  jp divSingle
#endif
