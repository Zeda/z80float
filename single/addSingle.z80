#ifndef included_addSingle
#define included_addSingle

addend = scrap
addend2= scrap+7    ;4 bytes

;Still need to tend to special cases
addSingle:
;x+y
    push af
    push hl
    push de
    push bc
addInject:
    inc de
    inc de
    inc hl
    inc hl
    ld a,(de)
    xor (hl)
    push af
    inc de
    inc hl
    ex de,hl
    ld a,(de)
    sub (hl)
    ex de,hl
    jr nc,$+5
    ex de,hl
    neg
    cp 24
    jp nc,add_unneeded
    push hl
    ld hl,addend+6
    dec de
    ld bc,0408h
    dec hl
    ld (hl),0
    sub c
    jr nc,$-5
    add a,c
    push af
    push hl
    ex de,hl
    ld a,(hl) \ or 80h \ ld (de),a \ dec de \ dec hl
    ldd
    ldd
    ex de,hl
    dec b
    jr z,$+7
    ld (hl),0 \ dec hl \ djnz $-3
    pop hl
    pop af
    ld b,a
    jr z,noshift
    set 7,(hl)
_:
    push hl
    srl (hl) \ dec hl
    rr (hl) \ dec hl
    rr (hl) \ dec hl
    rr (hl)
    pop hl
    djnz -_
noshift:
    pop hl  ;bigger float
    dec hl
    ld b,(hl)
    dec hl
    dec hl
    ex de,hl
    pop af
    jp m,subtract
    ld hl,addend+2
    ld a,(hl) \ rla \ inc hl
    ld a,(de) \ adc a,(hl) \ ld (hl),a \ inc hl \ inc de
    ld a,(de) \ adc a,(hl) \ ld (hl),a \ inc hl \ inc de
    ld a,(de) \ set 7,a \ adc a,(hl) \ ld (hl),a \ inc hl \ inc de
    ld a,(de) \ ld (hl),a
    jp nc,add_done
    inc (hl)
    jp z,add_overflow
    dec hl \ rr (hl)
    dec hl \ rr (hl)
    dec hl \ rr (hl)
    jp add_done
subtract:
    ld hl,addend
    xor a
    ld c,a \ sub (hl) \ ld (hl),a \ inc hl
    ld a,c \ sbc a,(hl) \ ld (hl),a \ inc hl
    ld a,c
    sbc a,(hl) \ ld (hl),a \ inc hl
    ld a,(de) \ sbc a,(hl) \ ld (hl),a \ inc hl \ inc de
    ld a,(de) \ sbc a,(hl) \ ld (hl),a \ inc hl \ inc de
    ld a,(de) \ set 7,a
    sbc a,(hl) \ ld (hl),a \ inc hl \ inc de
    ld a,(de) \ ld (hl),a
    dec de
    ex de,hl
    jr nc,negated
    ld hl,addend
    ld a,80h \ xor b \ ld b,a
    ld a,c \ sub (hl) \ ld (hl),a \ inc hl
    ld a,c \ sbc a,(hl) \ ld (hl),a \ inc hl
    ld a,c \ sbc a,(hl) \ ld (hl),a \ inc hl
    ld a,c \ sbc a,(hl) \ ld (hl),a \ inc hl
    ld a,c \ sbc a,(hl) \ ld (hl),a \ inc hl
    ld a,c \ sbc a,(hl) \ ld (hl),a
negated:
    jp m,add_done
    push bc
    ld hl,(addend)
    ld de,(addend+2)
    ld bc,(addend+4)
    ld a,h \ or l \ or d \ or e \ or b \ or c
    jp z,add_underflow
    ld a,(addend+6)
normalize:
    dec a \ jr z,add_underflow
    add hl,hl \ rl e \ rl d \ rl c \ rl b
    jp p,normalize
    ld (addend),hl
    ld (addend+2),de
    ld (addend+4),bc
    ld (addend+6),a
    pop bc
add_done:
;Need to adjust sign flag
    ld hl,addend+5
    ld a,(hl)
    rla \ rl b \ rra \ ld (hl),a
    dec hl
    dec hl
add_copy:
    pop de
    push de
    ldi
    ldi
    ldi
    ld a,(hl)
    ld (de),a
    pop bc
    pop de
    pop hl
    pop af
    ret
add_underflow:
;How many push/pops are needed?
;return ZERO
    ld hl,0
    ld (addend+3),hl
    ld (addend+5),hl
    pop bc
    jr add_done
add_overflow:
;How many push/pops are needed?
;return INF
    dec hl
    ld (hl),40h
    jr add_done
add_unneeded:
;How many push/pops are needed?
;Return bigger number
    pop af
    dec hl
    dec hl
    dec hl
    jr add_copy
#endif
