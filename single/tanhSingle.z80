#ifndef included_tanhSingle
#define included_tanhSingle
#include "pushpop.z80"
#include "expSingle.z80"
#include "invSingle.z80"
#include "rsubSingle.z80"
#include "ameanSingle.z80"

#define hyperout scrap+9
#define hyperout2 scrap+13

tanhSingle:
    call pushpop
    push bc
    ld de,hyperout
    ldi
    ldi
    ldi
    ld a,(hl)
    or a
    jr z,tanh_inf
    inc a
    jr z,tanh_zero
    ld (de),a
    ld hl,hyperout
    ld b,h
    ld c,l
    call expSingle
    ld de,const_1
    call ameanSingle
    call invSingle
    pop bc
    jp rsubSingle
tanh_zero:
    pop hl
    ld b,h
    ld c,l
    xor a
    ld (hl),a \ inc hl
    ld (hl),a \ inc hl
    ld (hl),a \ inc hl
    dec a
    ld (hl),a
    ret
tanh_inf:
    dec hl
    ld a,(hl)
    add a,a
    jp p,tanh_NAN
    pop hl
    ld b,h
    ld c,l
    ld a,0
    ld (hl),a \ inc hl
    ld (hl),a \ inc hl
    rra
    ld (hl),a \ inc hl
    ld (hl),80h
    ret
tanh_NAN:
    pop hl
    ld b,h
    ld c,l
    xor a
    ld (hl),a \ inc hl
    ld (hl),a \ inc hl
    ld (hl),a \ inc hl
    ld (hl),a
    ret
#endif
