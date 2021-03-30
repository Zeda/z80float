#ifndef included_xtoTI
#define included_xtoTI
#include "mov.z80"
#include "pushpop.z80"
#include "xtostr.z80"
#include "strtox.z80"

#ifdef char_TI_TOK
#define char_NEG  $1A
#define char_ENG  $1B
#define char_DEC  '.'
#else
;otherwise, char_TI_CHR
#define char_NEG  $B0
#define char_ENG  $3B
#define char_DEC  $3A
#endif
#ifndef strtox_ptr
#define strtox_ptr xOP1+25
#endif

#define OP1 8478h
;NOTE! Doesn't check special cases!
xtoTI:
  call pushpop
  push bc

;Convert the float to a string
  ld bc,xOP1+9
  call xtostr

;Convert the string to a TI-float
;Check if there is a negative sign.
  pop de
  ld h,b
  ld l,c
  ld a,(hl)
  sub char_NEG
  sub 1
  ld a,0
  jr nc,+_
  rra
  inc hl
_:
  ld (de),a
  push de
  call strtox_sub0
  pop de
  inc de
;Now we have 10 base-100 digits at xOP1 and BC is our exponent
  ld a,c
  add a,127
  jr nc,+_
  inc b
_:
  dec b
  inc b
  jr nz,xtoTI_inf

  ld (de),a
  ld bc,$0700
  ld hl,xOP1+9
_:
  inc de
  push hl
  ld l,(hl)
;L_To_BCD_no_overflow:
    ld h,c
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,h \ daa  \ rl l
    adc a,a \ daa \ rl l
    adc a,a \ daa \ rl l
    adc a,a \ daa \ rl l
    adc a,a \ daa
  ld (de),a
  pop hl
  dec hl
  djnz -_
  ret
xtoTI_inf:
  ex de,hl
  ld hl,OP1+1
  ld (hl),128+99
  ld bc,$0799
_:
  inc hl
  ld (hl),c
  djnz -_
  ret
#endif
