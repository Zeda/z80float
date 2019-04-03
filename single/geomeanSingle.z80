#ifndef included_geomeanSingle
#define included_geomeanSingle
#include "mulSingle.z80"
#include "sqrtSingle.z80"

geomeanSingle:
;not correct. Can cause overflow in mulSingle, but true geomean never overflows.
    push hl
    call mulSingle
    ld h,b
    ld l,c
    call sqrtSingle
    pop hl
    ret
#endif
