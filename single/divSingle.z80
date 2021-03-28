#ifndef included_divSingle
#define included_divSingle
#include "pushpop.z80"
quot=scrap+1
divSingle:
;HL points to numerator
;DE points to denominator
;BC points to where the quotient gets written
  call pushpop
divSingle_no_pushpop:
    inc hl \ inc de
    inc hl \ inc de
    ld a,(de)   ;\
    xor (hl)    ; |Get sign of output
    add a,a     ; |
    push af     ;/
    push bc
    inc hl \ inc de
    ld a,(hl)   ;\
    ex de,hl    ; |Get exponent
    sub (hl)    ; |
    ex de,hl    ; |

    ld b,-1
    jr nc,+_
    dec b
_:
    add a,128
    jr nc,+_
    inc b
_:
    inc b
    jr z,+_
    jp p,divunderflow
    jp m,divoverflow
_:
    ld (quot+3),a
    dec hl
    dec de
    ld b,(hl)
    dec hl
    ld a,(hl)
    dec hl
    ld l,(hl)
    ld h,a
    ex de,hl

    ld c,(hl)
    dec hl
    ld a,(hl)
    dec hl
    ld l,(hl)
    ld h,a
    ex de,hl

    set 7,c
    ld a,b
    or 80h
    sbc hl,de \ sbc a,c
    jr nz,+_
    or h
    or l
    jr z,setmantissa0
    xor a
_:
    jr nc,startdiv
    ld b,a
    ld a,(quot+3)
    dec a
    ld (quot+3),a
    ld a,b
    add hl,hl
    adc a,a
    add hl,de
    adc a,c
startdiv:
    ld b,1
    call divsub0+3
    ld (quot+1),bc
    call divsub0
    ld (quot),bc
    call divsub0
    ld (quot-1),bc
    add hl,hl \ rla \ jr c,+_
    sbc hl,de \ sbc a,c \ ccf
_:
    ld hl,(quot)
    ld de,(quot+2)
    ld bc,0
    adc hl,bc
    ex de,hl
    adc hl,bc
    ld b,h
    ld c,l
writeback:
    pop hl
    ld (hl),e \ inc hl
    ld (hl),d \ inc hl
    rl c
    pop af
    rr c
    ld (hl),c \ inc hl
    ld (hl),b
    ret
divoverflow:
    ld b,$40
    jr +_
divunderflow:
  ld b,0
  jr +_
setmantissa0:
  ld bc,(quot+2)
_:
  ld de,0
  ld c,e
  jr writeback
divsub0:
;882cc max
    call divsub1    ;34 or 66
    call divsub1    ;
    call divsub1
    call divsub1
    call divsub1
    call divsub1
    call divsub1
    call divsub1
    or a
    sbc hl,de \ sbc a,c
    inc b
    ret nc
    dec b
    add hl,de
    adc a,c
    ret
divsub1:
;34cc or 66cc or 93cc
    sla b \ add hl,hl \ rla \ ret nc
    or a
    inc b \ sbc hl,de \ sbc a,c
    ret c
    inc b \ sbc hl,de \ sbc a,c
    ret
#endif
