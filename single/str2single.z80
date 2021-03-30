#ifndef included_str2Single
#define included_str2Single
#include "pushpop.z80"
#include "mov4.z80"
#include "routines/ascii_to_uint8.z80"
#include "mulSingle.z80"
#include "constants.z80"
#include "lut.z80"

#define ptr_sto scrap+9
str2single:
;#Routines/Single Precision
;Inputs:
;  HL points to the string
;  BC points to where the float is output
;Output:
;  scrap+9 is the pointer to the end of the string
;Destroys:
;  11 bytes at scrap ?
  call pushpop
  push bc
;Check if there is a negative sign.
;   Save for later
;   Advance ptr
  ld a,(hl)
  sub char_NEG
  sub 1
  push af
  jr nc,$+3
  inc hl
;Skip all leading zeroes
  ld a,(hl)
  cp '0'
  jr z,$-4      ;jumps back to the `inc hl`
;Set exponent to 0
  ld b,0
;Check if the next char is char_DEC
  sub char_DEC
  or a      ;to reset the carry flag
  jr nz,+_
  .db $FE   ;start of cp *
;Get rid of zeroes
  dec b
  inc hl
  ld a,(hl)
  cp '0'
  jr z,$-5      ;jumps back to the `dec b`
  scf
_:
;Now we read in the next 8 digits
  ld de,scrap+3
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
;Now `scrap` holds the 4-digit base-100 number.
;b is the exponent
;if carry flag is set, just need to get rid of remaining digits
;Otherwise, need to get rid of remaining digits, while incrementing the exponent
  sbc a,a
  inc a
  ld c,a
_:
  ld a,(hl)
  cp 30h
  jr nz,+_
  inc hl
  ld a,b
  add a,c
  jp z,strToSingle_inf
  ld b,a
  jr -_
;Now check for engineering `E` to modify the exponent
_:
  cp char_ENG
  call z,str_eng_exp
;Gotta multiply the number at (scrap) by 2^24
  ld (ptr_sto),hl
  ld d,100
  call scrap_times_256
  ld a,c
  ld (scrap+6),a
  call scrap_times_256
  ld a,c
  ld (scrap+5),a
  call scrap_times_256
  ld a,c
  ld (scrap+4),a
  call scrap_times_256
  ld a,c
  ld (scrap+3),a
;Now scrap+3 is a 4-byte mantissa that needs to be normalized
;
  ld hl,(scrap+3)
  ld a,h
  or l
  ld hl,(scrap+5)
  or l
  or h
  jp z,strToSingle_zero-1
  ld c,$7F
  ld a,h
  or a
  jp m,strToSingle_normed
  ;Will need to iterate at most three times
_:
  dec c
  ld hl,scrap+3
  sla (hl) \ inc hl
  rl (hl) \ inc hl
  rl (hl) \ inc hl
  adc a,a
  jp p,-_
strToSingle_normed:
;Move the number to scrap
  ld hl,(scrap+4)
  ld (scrap),hl
  ld l,a
  ld h,c
  sla l
  pop af
  rr l
  ld (scrap+2),hl
;now (scrap) is our number, need to multiply by power of 10!
;Power of 10 is stored in B, need to put in A first
  xor a
  sub b
  ld de,pown10LUT
  jp p,+_
  ld a,b
  ld de,pow10LUT
  cp 40
  jp nc,strToSingle_inf+1
_:
  cp 40
  jp nc,strToSingle_zero
  ld hl,scrap
  ld b,h
  ld c,l
  call +_
  call +_
  call +_
  call +_
  call +_
  call +_
  pop de
  jp mov4
_:
  rra
  call c,mulSingle
  inc de
  inc de
  inc de
  inc de
  ret
str_eng_exp:
  ld de,0
  inc hl
  ld a,(hl)
  cp char_NEG    ;negative exponent?
  push af
  jr nz,$+3
  inc hl
_:
  ld a,(hl)
  sub 3Ah
  add a,10
  jr nc,+_
  inc hl
  push hl
  ld h,d
  ld l,e
  add hl,hl
  add hl,hl
  add hl,de
  add hl,hl
  add a,l
  ld l,a
  ex de,hl
  pop hl
  jp c,eng_overflow
  inc d
  dec d
  jp z,-_
  jp nz,eng_overflow
_:
  ld a,e
  cp 40
  jr nc,eng_overflow
  pop af
  ld a,b
  jr nz,+_
  sub e
  ld b,a
  ret
_:
  add a,e
  ld b,a
  ret
scrap_times_256:
  ld e,8
_:
  or a
  ld hl,scrap
  call +_
  call +_
  rl c
  dec e
  jr nz,-_
  ret
_:
  call scrap_times_sub
scrap_times_sub:
  ld a,(hl)
  rla
  cp d
  jr c,$+3
  sub d
  ld (hl),a
  inc hl
  ccf
  ret
eng_overflow:
  pop af
  jr nz,strToSingle_inf
  pop af
strToSingle_zero:
  ld hl,const_0
  pop de
  jp mov4
strToSingle_inf:
;return inf
  pop af
  ld hl,const_inf
  jr nc,+_
  ld hl,const_NegInf
_:
  pop de
  jp mov4
#endif
