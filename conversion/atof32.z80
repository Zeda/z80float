#ifndef included_atof32
#define included_atof32
#include "f32mul.z80"
#include "ascii_to_BCD.z80"
#include "ascii_to_BCD.z80"
#include "f32_pow10_LUT.z80"


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




#define ptr_sto scrap
atof32:
;Inputs:
;  HL points to the string
;  BC points to where to write the float
;Output:
;  AHL is the f32 float
;  scrap is the pointer to the end of the string
;Destroys:
;  BC, DE
;  2 bytes at scrap
;
;
  call pushpop
  push bc ; save the pointer to the output
;Check for a negative sign, save for later, and advance the pointer if so.
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
  jr nz,atof32_skip_1
  .db $FE   ;start of cp *
;Get rid of zeroes
  dec b
  inc hl
  ld a,(hl)
  cp '0'
  jr z,$-5      ;jumps back to the `dec b`
  scf
atof32_skip_1:
; at this point, we ought to pointing at our first non-zero digit, unless all
; digits were 0, in which case we might be pointing to TOK_ENG
  rl c
  ld a,(hl)
  sub '0'
  cp 10
  jp nc,atof32_zero_check_eng
  srl c

;Now we read in the next 8 digits. Ideally, we want 27 bits worth, but 8 digits
; gives us about 26.5 bits
  call ascii_to_BCD
  ld d,a
  call ascii_to_BCD
  ld e,a
  push de
  call ascii_to_BCD
  ld d,a
  call ascii_to_BCD
  ld e,a

;Now `scrap` holds the 4-digit base-100 number (little-endian)
;b is the exponent
;if carry flag is set, just need to get rid of remaining digits
;Otherwise, need to get rid of remaining digits, while incrementing the exponent

  sbc a,a
  ld c,a
atof32_loop_1:
  ld a,(hl)
  cp TOK_DECIMAL
  jr nz,$+8
  dec c
  jp pe,atof32_skip_7 ; we've reached our first decimal
  jr atof32_skip_2    ; else C was already FF, then a decimal was already encountered

  sub '0'
  cp 10
  jr nc,atof32_skip_6
; carry flag is set
atof32_skip_7:
  inc hl
  ld a,b
  adc a,c
  ; if carry flag is set, then we added 0
  jr c,atof32_loop_1
  jp z,atof32_inf2
  ld b,a
  jr atof32_loop_1

atof32_skip_6:
  ld a,(hl)
;Now check for engineering `E` to modify the exponent
  cp TOK_ENG
  call z,atof32_str_eng_exp

atof32_skip_2:
  ld (ptr_sto),hl ; save the pointer to the end of the string
  pop hl
  ex de,hl        ; DEHL is the number

  push bc         ; B is the base-10 exponent
  call atof32_scrap_times_256
  ld b,c
  call atof32_scrap_times_256
  push bc         ; BC is the upper 16 bis of the result
  call atof32_scrap_times_256
  ld b,c
  call atof32_scrap_times_256
  pop de
  ld h,b
  ld l,c
  ; DEHL is 32 bits of the significand
  pop bc  ; B is the base-10 exponent

;HLC holds the 3-digit significand, need to normalize it
; make sure it isn't zero
  ld a,e
  or d
  or l
  or h
  jp z,atof32_zero


  ld c,$7E
  ld a,d
  or a
  jr atof32_loop_3_start
atof32_loop_3:
  dec c
  add hl,hl
  rl e
  adc a,a
atof32_loop_3_start:
  jp p,atof32_loop_3

  add a,a
  ld d,a
  pop af
  rr c
  rr d

; round
  sla l
  jr nc,+_
  inc h
  jr nz,+_
  inc e
  jr nz,+_
  inc d
  jr nz,+_
  inc c
_:
;CDEH * 10^B

; write the float in CDEH to the output
  ld a,h
  pop hl
  ld (hl),a
  inc hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),c
  dec hl
  dec hl
  dec hl

; now multiply the float at HL by 10^B
  xor a
  sub b
  ld de,f32_pown10_LUT
  jp p,$+7
  ld a,b
  ld de,f32_pow10_LUT

  cp 38
  jr c,$+4
  ld a,-1

  ld b,h
  ld c,l
  call atof32_mul_first
  call atof32_mul_twice
atof32_mul_twice:
  call atof32_mul_once
atof32_mul_once:
  inc de
  inc de
  inc de
  inc de
atof32_mul_first:
  rra
  call c,f32mul
  ret

atof32_str_eng_exp:
; HL points to the string, B is the current exponent, returns adjusted exponent in B
  push de   ; save lower digits of input
  ld e,0
  inc hl
  ld a,(hl)
  sub TOK_NEG   ;negative exponent?
  ld c,a        ;backup result
  jr nz,atof32_skip_5
  jr atof32_skip_3
atof32_loop_2:
  ld d,a  ; save the digit to add

; make sure E doesn't exceed 3 (else the exponent is over 40)
  ld a,e
  cp 4
  jr nc,atof32_eng_overflow

  add a,a
  add a,a
  add a,e
  add a,a ; E*10
  add a,d ; E*10+D
  ld e,a

atof32_skip_3:
  inc hl
atof32_skip_5:
  ld a,(hl)
  sub '0'
  cp 10
  jr c,atof32_loop_2

  ld a,e
  cp 60
  jr nc,atof32_eng_overflow
  ld a,c
  or a
  ld a,b
  jr nz,atof32_skip_4
  sub e
  .db $FE  ; start of `cp *` to skip the next byte
atof32_skip_4:
  add a,e
  ld b,a
  pop de
  ret

atof32_scrap_times_256:
  call atof32_scrap_times_16
atof32_scrap_times_16:
  call atof32_scrap_times_4
atof32_scrap_times_4:
  call atof32_scrap_times_2
atof32_scrap_times_2:
;DEHL 8 BCD digits, need to multiply by 2
  ld a,l
  add a,a
  daa
  ld l,a

  ld a,h
  adc a,a
  daa
  ld h,a

  ld a,e
  adc a,a
  daa
  ld e,a

  ld a,d
  adc a,a
  daa
  ld d,a

  rl c
  ret

atof32_inf2:
  ld c,-1
atof32_eng_overflow:
  pop de  ; pop off saved digits
  pop af  ; pop off the return address for the call
  pop hl  ; pop off the other saved digits
  ld a,c
  or a
  jr z,atof32_zero
atof32_inf:
;return inf
  pop af
  pop hl
  ld a,0
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  dec a
  rra
  rr (hl)
  inc hl
  ld (hl),a
  ret

atof32_zero_check_eng:
  cp TOK_ENG-'0'
  jr nz,atof32_zero_write_hl
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
atof32_zero_write_hl:
  ld (ptr_sto),hl ; save the pointer to the end of the string
atof32_zero:
  pop af
  pop hl
  ld a,0
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  rra
  ld (hl),a
  ret
#endif
