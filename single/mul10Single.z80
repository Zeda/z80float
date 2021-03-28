#ifndef included_mul10Single
#define included_mul10Single
;#include "pushpop.z80"
mul10Single:
;Multiplies a single precision float by 10
    push af
    push hl
    push de
    push bc
    ld c,(hl) \ inc hl
    ld b,(hl) \ inc hl
    ld e,(hl) \ inc hl
    ld a,(hl)
    push de
    or 80h
    rra \ rr e \ rr b \ rr c
    srl a \ rr e \ rr b \ rr c
    dec hl \ dec hl \ dec hl
    ld d,a
    ld a,(hl) \ adc a,c \ ld c,a \ inc hl
    ld a,(hl) \ adc a,b \ ld c,a \ inc hl
    ld a,(hl) \ adc a,e \ ld c,a \ inc hl
    ld a,(hl) \ set 7,a \ adc a,d \ inc hl
    jr nc,$+10
    rra \ rr e \ rr b \ rr c \ scf
    add a,a
    ld d,a
    ld a,(hl) \ adc a,3 \ jr c,mul10_overflow
    ld (hl),a
    ld l,a
    pop af
    add a,a
    rr d
    ld a,l
    pop hl
    push hl
    ld (hl),c \ inc hl
    ld (hl),b \ inc hl
    ld (hl),e \ inc hl
    ld (hl),d \ inc hl
    ld (hl),a
    pop bc
    pop de
    pop hl
    pop af
    ret
mul10_overflow:
    xor a
    pop de
    pop hl
    ld b,h
    ld c,l
    ld (hl),a \ inc hl
    ld (hl),a \ inc hl
    rl d
    or 80h
    rra
    ld (hl),a \ inc hl
    ld(hl),-1
    pop de
    pop hl
    pop af
    ret
#endif
