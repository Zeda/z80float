#ifndef included_divSingle_special
#define included_divSingle_special
#include "pushpop.z80"
#include "C_Times_BDE.z80"

div255Single:
;HL points to the input, BC points to the output
;Divides a single-precision float by 255, better speed.
    call pushpop
    ld a,1
    jr divspecial_stepin
div85Single:
;HL points to the input, BC points to the output
;Divides a single-precision float by 85, better speed.
    call pushpop
    ld a,3
    jr divspecial_stepin
div51Single:
;HL points to the input, BC points to the output
;Divides a single-precision float by 51, better speed.
    call pushpop
    ld a,5
    jr divspecial_stepin
div17Single:
;HL points to the input, BC points to the output
;Divides a single-precision float by 17, better speed.
    call pushpop
    ld a,15
    jr divspecial_stepin
div15Single:
;HL points to the input, BC points to the output
;Divides a single-precision float by 15, better speed.
    call pushpop
    ld a,17
    jr divspecial_stepin
div5Single:
;HL points to the input, BC points to the output
;Divides a single-precision float by 5, better speed.
    call pushpop
    ld a,51
    jr divspecial_stepin
div3Single:
;HL points to the input, BC points to the output
;Divides a single-precision float by 3, better speed.
    call pushpop
    ld a,85
divspecial_stepin:
    push bc
    ld c,a
    call singleTimesCdiv255
    ld a,h
    pop hl
    ld (hl),a
    inc hl
    ld (hl),c
    inc hl
    ld (hl),b
    inc hl
    ld (hl),e
    ret
singleTimesCdiv255:
;HL points to the single precision float, multiplies it by C/255
;Returns float in EBCH
;can be used to efficiently divide by:
;   3   (C=85)
;   5   (C=51)
;   15  (c=17)
;   17  (C=15)
;   51  (C= 5)
;   85  (C= 3)
;   255 (C= 1)
;Assumes C is always less than 128.
    ld e,(hl)
    inc hl
    ld d,(hl)
    inc hl
    ld a,(hl)
    rlca
    scf
    rra
    ld b,a
    inc hl
    ld a,(hl)
    push af
;pop af returns sign in c flag, A is the exponent
    call C_times_BDE
    ld b,c
    ld c,a
    ex de,hl
    ld h,c
    ld l,h
    ex de,hl
    add hl,de
    ld a,b
    adc a,0
    add hl,bc
    adc a,c
    ld c,a
    jr nc,$+3
    inc b
    ld a,e
    add a,d
    ld d,a
    jr nc,+_
    inc l
    jr nz,+_
    inc h
    jr nz,+_
    inc bc
_:
    pop af
    ld e,a
    rra
    rr b
    rl b
    jp p,$+17
_:
    dec e
    sla d \ rl l \ rl h \ rl c \ rl b \ jp p,-_
    rl l
    jr nc,+_
    inc h
    jr nz,+_
    inc c
    jr nz,+_
    inc b
    jr nz,+_
    rla
    rr b
    inc e
    ret
_:
    rl b
    rla
    rr b
    ret
#endif
