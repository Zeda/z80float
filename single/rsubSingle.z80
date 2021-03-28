#ifndef included_rsubSingle
#define included_rsubSingle
;#include "pushpop.z80"
#include "addSingle.z80"
rsubSingle:
;-x+y
    push af
    push hl
    push de
    push bc
    push de
    ld de,addend2
    ldi
    ldi
    ld a,(hl)
    xor 80h
    ld (de),a
    inc de
    inc hl
    ld a,(hl)
    ld (de),a
    pop de
    ld hl,addend2
    jp addInject    ;jumps in to the addSingle routine
#endif
