#ifndef included_powSingle
#define included_powSingle
#include "pushpop.z80"
#include "lgSingle.z80"
#include "expSingle.z80"
#define var_x   scrap     ;4 bytes
#define var_c   scrap+4   ;4 bytes
powSingle:
;Computes y^x
;HL points to y
;DE points to x
;BC points to output
    call pushpop
    push bc
    ld bc,var_c
    call lgSingle
    ld h,b
    ld l,c
    ex de,hl
    jp pow_inject
#undefine var_x
#undefine var_c
#endif
