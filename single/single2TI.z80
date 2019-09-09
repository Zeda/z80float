#ifndef included_single2ti
#define included_single2ti
#include "single2str.z80"
single2ti:
;Turns a single precision float into a TI-float
;HL points to the input float.
;BC points to the output.
    push af
    push hl
    push de
    push bc
    ld bc,scrap
    call single2str
    pop hl
    push hl
    ld a,(bc)
    sub $1A
    sub 1
    ld a,0
    rra
    ld (hl),a
    inc hl
    push hl     ;HL is where exponent will get written
;
    ld de,017Fh
    call toti_sub2
    call toti_sub2
    call toti_sub2
    call toti_sub2
    xor a
    inc hl \ ld (hl),a
    inc hl \ ld (hl),a
    inc hl \ ld (hl),a
    ld a,(bc)
    or a
    jr z,write_ti_exp
    inc bc
    ld a,(bc)
    cp $1A
    push af     ;sign
    jr nz,$+4
    inc bc \ ld a,(bc)
    sub 30h
    ld h,a
    inc bc
    ld a,(bc)
    or a
    jr z,sign_exp
    ld l,a
    add a,a
    add a,a
    add a,h
    add a,a
    add a,l
    ld h,a
sign_exp:
    pop af
    ld a,h
    jr nz,$+4
    neg
    add a,e
    ld e,a
write_ti_exp:
    pop hl
    ld (hl),e
    pop bc
    pop de
    pop hl
    pop af
    ret
toti_sub2:
    inc hl
    call toti_sub
toti_sub:
    ld a,(bc)
    or a
    jr z,toti_sub_end
    sub $1B
    jr z,toti_sub_end
    cp '.'-$1B
    jr nz,$+4
    inc bc
    dec d
    ld a,d
    add a,e
    ld e,a
    ld a,(bc)
    inc bc
toti_sub_end:
    rld
    ret
#endif
