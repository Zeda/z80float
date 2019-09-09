#ifndef included_mulSingle
#define included_mulSingle
#include "routines/C_Times_BDE.z80"
;Need to check special cases inf,zero,NAN
var48 = scrap+4
mulSingle:
;Inputs: HL points to float1, DE points to float2, BC points to where the result is copied
;Outputs: float1*float2 is stored to (BC)
;573+mul24+{0,34}+{0,30}
;min: 1398cc
;max: 2563cc
;avg: 2054.63839751681cc
    push af
    push hl
    push de
    push bc

    call +_   ;CHLB
    ld a,c
    ex de,hl
    pop hl
    push hl
    ld (hl),b \ inc hl
    ld (hl),e \ inc hl
    ld (hl),d \ inc hl
    ld (hl),a
    pop bc
    pop de
    pop hl
    pop af
    ret


_:
;return float in CHLB
    push de
    ld e,(hl)
    inc hl
    ld d,(hl)
    inc hl
    ld c,(hl)
    inc hl
    ld a,(hl)
    or a
    jr z,mulSingle_case0
    ex de,hl
    ex (sp),hl
    ld e,(hl)
    inc hl
    ld d,(hl)
    inc hl
    ld b,(hl)
    inc hl
    inc (hl)
    dec (hl)
    jr z,mulSingle_case1
    add a,(hl)      ;\
    pop hl          ; |
    rra             ; |Lots of help from Runer112 and
    adc a,a         ; |calc84maniac for optimizing
    jp po,bad       ; |this exponent check.
    xor 80h         ; |
    jr z,underflow  ;/
    push af         ;exponent
    ld a,b
    xor c
    push af         ;sign
    set 7,b
    set 7,c
    call mul24      ;BDE*CHL->HLBCDE, returns sign info
    pop de
    ld a,e
    pop de
    jp m,+_
    rl c
    rl b
    adc hl,hl
    .db $FE   ;start of `cp *` to skip the `inc d`
_:
    inc d
    jr z,overflow
    rl c
    ld c,d
    ld de,0
    push af
    ld a,b
    adc a,e
    ld b,a
    adc hl,de
    jr nc,+_
    inc c \ jr z,overflow
    rr h
    rr l
    rr b
_:
    pop af
    cpl
    and $80
    xor h
    ld h,a
    ret
bad:
    jr nc,overflow
underflow:
    ld hl,0
    rl b
    rr h
    ld c,l
    ld b,l
    ret
overflow:
    ld hl,$8000
    jr underflow+3
mulSingle_case1:
;x*0   -> 0
;x*inf -> inf
;x*NaN -> NaN
  pop hl
  ld h,b
  ld l,d
  ld b,e
  ld c,0
  ret
mulSingle_case0:
;special*x = special
;NaN*x = NaN
;0*0 = 0
;0*NaN = NaN
;0*Inf = NaN
;Inf*Inf  = Inf
;Inf*-Inf =-Inf
  ;0CDE
  pop hl
  inc hl
  inc hl
  inc hl
  ld a,(hl)
  or a
  jr z,+_
  ld h,c
  ld c,0
  ret
_:
  dec hl
  ld b,(hl)
;basically, if b|c has bit 5 set, return NaN
  ld a,b
  or c
  ld h,$20
  and h
  jr z,+_
  ld c,0
  ret
_:
  ld a,c
  xor b
  rl b
  rlca
  rr b
  res 4,b

  rl c
  rrca
  rr c

  ld a,c
  and $E0
  add a,b
  rra
  ld h,a
  ld c,0
  ret
mul24:
;BDE*CHL -> HLBCDE
;155 bytes
;402+3*C_Times_BDE
;fastest:1201cc
;slowest:1753cc
;avg    :1464.9033203125cc (1464+925/1024)
;min: 825cc
;max: 1926cc
;avg: 1449.63839751681cc

    push bc
    ld c,l
    push hl
    call C_Times_BDE
    ld (var48),hl
    ld l,a
    ld h,c
    ld (var48+2),hl

    pop hl
    ld c,h
    call C_Times_BDE
    push bc
    ld bc,(var48+1)
    add hl,bc
    ld (var48+1),hl
    pop bc
    ld b,c
    ld c,a
    ld hl,(var48+3)
    ld h,0
    adc hl,bc
    ld (var48+3),hl

    pop bc
    call C_Times_BDE
    ld de,(var48+2)
    add hl,de
    ld (var48+2),hl
    ld d,c
    ld e,a
    ld b,h
    ld c,l
    ld hl,(var48+4)
    ld h,0
    adc hl,de
    ld de,(var48)
    ret
#endif
