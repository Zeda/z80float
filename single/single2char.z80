#ifndef included_single2char
#define included_single2char
single2char:
;returns in A
    push hl
    push de
    push bc
    inc hl
    ld e,(hl)
    inc hl
    ld a,(hl)
    add a,a
    push af
    scf
    rra
    ld d,a
    inc hl
    ld a,(hl)
    sub 7Fh
    ex de,hl
    jr nc,$+4 \ xor a \ ld d,a
    jr z,return_char
    cp 8
    ld b,a
    ld a,0
    jr nc,return_char
    add hl,hl \ rla \ djnz $-2
return_char:
    ld d,a
    pop af
    ld a,d
    jr nc,$+4
    neg
    or a
    pop bc
    pop de
    pop hl
    ret
#endif
