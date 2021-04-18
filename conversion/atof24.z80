#ifndef included_atof24
#define included_atof24
#include "f24mul.z80"
#include "ascii_to_uint8.z80"
#include "f24pow10_LUT.z80"


#ifndef TOK_ENG
#define TOK_ENG 'e'
#endif

; Negative sign
#ifndef TOK_NEG
#define TOK_NEG '-'
#endif

; Decimal point
#ifndef TOK_DECIMAL
#define TOK_DECIMAL '.'
#endif




#define ptr_sto scrap+9
atof24:
;Inputs:
;  HL points to the string
;Output:
;  AHL is the f24 float
;  scrap is the pointer to the end of the string
;Destroys:
;  BC, DE
;  4 bytes at scrap
;
;Check if there is a negative sign.
;   Save for later
;   Advance ptr
  ld a,(hl)
  sub TOK_NEG
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
;Check if the next char is TOK_DECIMAL
  sub TOK_DECIMAL
  or a      ;to reset the carry flag
  jr nz,atof24_skip_1
  .db $FE   ;start of cp *
;Get rid of zeroes
  dec b
  inc hl
  ld a,(hl)
  cp '0'
  jr z,$-5      ;jumps back to the `dec b`
  scf
atof24_skip_1:
; at this point, we ought to pointing at our first non-zero digit, unless all
; digits were 0, in which case we might be pointing to TOK_ENG
  rl c
  ld a,(hl)
  sub '0'
  cp 10
  jp nc,atof24_zero_check_eng
  srl c

;Now we read in the next 6 digits
  ld de,scrap+2
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
;Now `scrap` holds the 3-digit base-100 number.
;b is the exponent
;if carry flag is set, just need to get rid of remaining digits
;Otherwise, need to get rid of remaining digits, while incrementing the exponent

  sbc a,a
  ld c,a
atof24_loop_1:
  ld a,(hl)
  cp TOK_DECIMAL
  jr nz,$+8
  dec c
  jp pe,atof24_skip_7
  jr atof24_skip_2  ; else C was already FF, then a decimal was already encountered

  sub '0'
  cp 10
  jr nc,atof24_skip_6
atof24_skip_7:
; carry flag is set
  inc hl
  ld a,b
  adc a,c
  ; if carry flag is set, then we added 0
  jr c,atof24_loop_1
  jp z,atof24_inf
  ld b,a
  jr atof24_loop_1

atof24_skip_6:
  ld a,(hl)
;Now check for engineering `E` to modify the exponent
  cp TOK_ENG
  call z,atof24_str_eng_exp
atof24_skip_2:
  ex de,hl  ; DE points to the end of the string

;Gotta multiply the number at (scrap) by 2^17
  ld hl,(scrap)
  ld a,(scrap+2)
  ld (ptr_sto),de ; save the pointer to the end of the string
  ld e,a
  ld d,-100
  call atof24_scrap_times_256
  push bc
  call atof24_scrap_times_256
  push bc
  call atof24_scrap_times_256
  pop hl
  pop de
  ld h,e

;HLC holds the 3-digit significand, need to normalize it
; make sure it isn't zero
  ld a,c
  or h
  or l
  jp z,atof24_zero

  pop af
  ld a,c
  ld c,$7E  ;0x3F * 2 because we'll be shifting down later
  rr c

atof24_loop_3:
  dec c
  add a,a
  adc hl,hl
  jr nc,atof24_loop_3
; round
  add a,a
  jr nc,+_
  inc l
  jr nz,+_
  inc h
  jr nz,+_
  inc c
_:
  ex de,hl
;CDE * 10^B

  xor a
  sub b
  jp p,atof24_small
  ld a,b
  cp 20
  jr c,$+9
  ld a,c
  or %01111111
  ld hl,0
  ret

  cp 10
  jr c,atof24_mul
  sub 10
  push af
  ld a,$60
  ld hl,$2A06
  jr atof24_continue

atof24_small:
  cp 20
  jr c,$+6
  xor a
  ld h,a
  ld l,a
  ret

  cp 10
  jr c,atof24_mul
  ld a,b
  add a,10
  push af
  ld a,$1D
  ld hl,$B7CE
atof24_continue:
  call f24mul
  ex de,hl
  pop bc
  ld c,a
atof24_mul:
  ld a,b
  neg
  add a,19

  ld b,a
  add a,a
  add a,b
  add a,(f24pow10_LUT+2)&255
  ld l,a
  adc a,(f24pow10_LUT+2)>>8
  sub l
  ld h,a
  ld a,(hl)
  dec hl
  ld b,(hl)
  dec hl
  ld l,(hl)
  ld h,b
;AHL * CDE
  jp f24mul




atof24_str_eng_exp:
; HL points to the string, B is the current exponent, returns adjusted exponent in B
  ld e,0
  inc hl
  ld a,(hl)
  sub TOK_NEG   ;negative exponent?
  ld c,a        ;backup result
  jr nz,atof24_skip_5
  jr atof24_skip_3
atof24_loop_2:
  ld d,a  ; save the digit to add

; make sure E doesn't exceed 2
  ld a,e
  cp 3
  jr nc,atof24_eng_overflow

  add a,a
  add a,a
  add a,e
  add a,a ; E*10
  add a,d ; E*10+D
  ld e,a

atof24_skip_3:
  inc hl
atof24_skip_5:
  ld a,(hl)
  sub '0'
  cp 10
  jr c,atof24_loop_2

  ld a,e
  cp 20
  jr nc,atof24_eng_overflow
  ld a,c
  or a
  ld a,b
  jr nz,atof24_skip_4
  sub e
  .db $FE  ; start of `cp *` to skip the next byte
atof24_skip_4:
  add a,e
  ld b,a
  ret

atof24_scrap_times_256:
  call atof24_scrap_times_16
atof24_scrap_times_16:
  call atof24_scrap_times_4
atof24_scrap_times_4:
  call atof24_scrap_times_2
atof24_scrap_times_2:
;EHL is a 3-digit base-100 number that needs to be multiplied by 256

; multiply the bottom 2 digits by 2
  add hl,hl

; check for overflow
  ld a,l
  add a,d
  jr nc,$+4
  ld l,a
  inc h

  ld a,h
  add a,d
  jr nc,$+3
  ld h,a

  ld a,e
  adc a,a
  add a,d
  jr c,$+3
  sub d
  ld e,a

  rl c
  ret

atof24_eng_overflow:
  pop af  ; pop off the return address for the call
  ld a,c
  or a
  jr z,atof24_zero
atof24_inf:
;return inf
  pop af
  ld hl,0
  ld a,-1
  rra
  ret

atof24_zero_check_eng:
  cp TOK_ENG-'0'
  jr nz,atof24_zero_write_hl
  ; otherwise, we need to read through the engineering exponent
  inc hl
  ld a,(hl)
  cp TOK_NEG
  jr nz,$+3
  inc hl
  ld a,(hl)
  sub '0'
  cp 10
  jr c,$-6  ; jumps back to the `inc hl`
atof24_zero_write_hl:
  ld (ptr_sto),hl ; save the pointer to the end of the string
atof24_zero:
  pop af
  xor a
  ld h,a
  ld l,a
  ret

#endif
