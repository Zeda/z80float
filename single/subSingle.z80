#ifndef included_subSingle
#define included_subSingle
;#include "pushpop.z80"
#include "addSingle.z80"

subSingle:
;x-y
    push af
    push hl
    push de
    push bc
    push hl
    ex de,hl
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
    ex de,hl
    pop hl
    ld de,addend2
    jp addInject    ;jumps in to the addSingle routine
#endif
