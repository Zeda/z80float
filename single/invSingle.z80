#ifndef included_invSingle
#define included_invSingle
#include "pushpop.z80"
#include "divSingle.z80"
#include "constants.z80"
invSingle:
;HL points to denominator
;BC points to where the quotient gets written
;
  call pushpop
  ex de,hl
  ld hl,const_1
  jp divSingle_no_pushpop
#endif
