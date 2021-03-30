#ifndef included_mul24
#define included_mul24
#include "C_Times_BDE.z80"
mul24:
;BDE*CHL ->  BHLDEA
;510+{0,39}+{0,8}+3*C_Times_BDE
;61 bytes
    push hl
    pop ix
    call C_Times_BDE  ; CAHL
    push hl
    ld l,a
    ld h,c
    ex (sp),hl
    push hl

    ld a,b
    push ix
    pop bc
    ld b,a
    call C_Times_BDE  ; CAHL
    ;CA + stack without destroying BDE
    ex (sp),hl
    add a,l
    ld l,a
    ld a,c
    adc a,h
    ld h,a
 ;   {1}HL{2}
    ld a,b
    push ix
    pop bc
    ld c,b
    ld b,a
    pop ix
  ;  IXHL{1}
    jr nc,+_
    ex (sp),hl
    inc hl
    ex (sp),hl
_:
    push hl
    push ix
;    {3}{2}{1}

    call C_Times_BDE
    dec sp
    ;CAHL
    pop de    ;D is the bottom byte
    ld b,d    ;B is the bottom byte
    pop de
    add hl,de ;HL is bytes 1 and 2
    ld d,c
    ld e,a
    ex (sp),hl
    adc hl,de ;HL is bytes 3 and 4
    pop de    ;DE is bytes 1 and 2
    ld a,b    ;A is the bottom byte
    dec sp
    pop bc    ;B is the top byte
    ret nc
    inc b
;    BHLDEA
    ret
#endif
