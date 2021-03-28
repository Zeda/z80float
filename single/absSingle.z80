#ifndef included_absSingle
#define included_absSingle
#include "pushpop.z80"
absSingle:
;HL points to the float
;BC points to where to output the result
    call pushpop
    ld d,b
    ld e,c
    ldi
    ldi
    ld a,(hl)
    and %01111111
    ld (de),a
    inc hl
    inc de
    ld a,(hl)
    ld (de),a
    ret
#endif
