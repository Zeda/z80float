#ifndef included_lnSingle
#define included_lnSingle
#include "pushpop.z80"
;#include "constants.z80"
#include "sqrtSingle.z80"
#include "ameanSingle.z80"
#include "subSingle.z80"
#include "bg2iSingle.z80"
;#include "lnSingle.z80"
;Uses 27 bytes
#define var_a scrap+11
#define var_g var_a+4
#define var_b var_g+4
#define var_x var_b+4
;This algorithm is insired by the one outlined here:
;http://www.ams.org/journals/mcom/1972-26-118/S0025-5718-1972-0307438-2/S0025-5718-1972-0307438-2.pdf
;It offers quadratic convergence, instead of linear convergence for only a little more work each iteration.
;So only TWO iterations are needed for single precision instead of ten.
lnSingle:
;need to add ln(2)*x_exp to end result
    call pushpop
    push bc
    ld de,var_X
    ldi
    ldi
    ldi
    ld a,(hl)
    push af
    ld a,80h
    ld (de),a
    ld bc,var_g
    ld hl,var_x
    call sqrtSingle
    ld de,const_1
    ld bc,var_a
    call ameanSingle
    ld b,h
    ld c,l
    call subSingle

    ld hl,var_a
    ld de,var_g
    ld b,h
    ld c,l
    call bg2iSingle
    ld de,var_x
    call mulSingle
    pop af
    ;need to multiply ln2*(A-80h) and addd it to the final result
    sub 80h
    jr z,lnSingle_noadjust
    jr nc,+_
    neg
_:
    push af
    ld c,a
    ld b,$B1 \ ld de,$7218    ;ln(2)
    call C_times_BDE
    ;CAHL is the mantissa, need to adjust
    ld b,$7F
    inc c
    dec c
    jr z,lnSingle_noshift
_:
    inc b \ srl c \ rra \ rr h \ rr l
    inc c \ dec c
    jr nz,-_
lnSingle_noshift:
  ;C*BDE => CAHL
    ;BAHL
    ld c,a
    pop af
    jr c,+_
    res 7,c
_:
    ld (var_g),hl
    ld (var_g+2),bc
    ld de,var_a
    ld hl,var_g
    ld b,d
    ld c,e
    call addSingle
    ex de,hl
lnSingle_noadjust:
    pop de
    jp mov4
#undefine var_a
#undefine var_g
#undefine var_b
#undefine var_x
#endif
