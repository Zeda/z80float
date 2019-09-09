#ifndef included_negSingle
#define included_negSingle
negSingle:
;HL points to the float
;BC points to where to output the result
    push hl
    push de
    push bc
    push af
    ld d,b
    ld e,c
    ldi
    ldi
    ld a,(hl)
    xor 80h
    ld (de),a
    inc hl
    inc de
    ld a,(hl)
    ld (de),a
    pop af
    pop bc
    pop de
    pop hl
    ret
#endif
