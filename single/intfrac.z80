#ifndef included_intfrac
#define included_intfrac
iPartSingle:
    push af
    push hl
    push de
    push bc
    ld e,(hl)
    inc hl
    ld d,(hl)
    inc hl
    ld b,(hl)
    inc hl
    ld a,(hl)
    or a
    jp z,ret_input
    cp 7Fh+24
    jp nc,ret_input
    sub 80h
    jp c,ret_zero
    push af
    cpl
    add a,24
    push af
    ld c,b
    and 7
    ld b,a
    ld a,-1
;lower B bits should be zero of CDE
    jr z,$+5
    add a,a \ djnz $-1
    ld b,a
    pop af
    sub 8 \ jr nc,$+7
    ld a,e \ and b \ ld e,a \ jr intout
    ld e,0
    sub 8 \ jr nc,$+7
    ld a,d \ and b \ ld d,a \ jr intout
    ld d,e \ ld a,b \ and c \ ld c,a
intout:
    pop af
    pop hl
    push hl
    ld (hl),e
    inc hl
    ld (hl),d
    inc hl
    ld (hl),c
    inc hl
    ld (hl),a
    pop bc
    pop de
    pop hl
    pop af
    ret
ret_zero:
    ld de,0
    ld b,e
ret_input:
    pop hl
    ld a,b
    ld c,l
    ld b,h
    ld (hl),e \ inc hl
    ld (hl),d \ inc hl
    ld (hl),a \ inc hl
    ld (hl),0
    pop de
    pop hl
    pop af
    ret
#endif
