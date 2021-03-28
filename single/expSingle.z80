#ifndef included_expSingle
#define included_expSingle
#include "pushpop.z80"
#include "constants.z80"
#include "mulSingle.z80"
#include "pow2Single.z80"
;requires       by
;   lgSingle    powSingle
;   mulSingle   powSingle,expSingle
;   invSingle   powSingle,expSingle,exp2Single

#define var_x   scrap     ;4 bytes
#define var_c   scrap+4   ;4 bytes

;           HL  DE  BC      desc

expSingle:
;Computes e^x
;HL points to x
;BC points to the output
  call pushpop
  ld de,const_lg_e
  push bc
pow_inject:
;DE points to lg(y), HL points to x, BC points to output
  ld bc,var_x
  call mulSingle
  ld h,b
  ld l,c
  jp exp_inject
#endif
