#ifndef included_ameanSingle
#define included_ameanSingle
#include "routines/pushpop.z80"
#include "addSingle.z80"

ameanSingle:
;Not entirely correct. addSingle might overflow to infinity before dividing by 2
    call pushpop
ameanSingle_no_pushpop:
    call addSingle
    ld h,b
    ld l,c
    inc hl
    inc hl
    inc hl
    ld a,(hl)
    or a
    ret z
    dec (hl)
    ret
#endif
