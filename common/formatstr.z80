#ifndef included_formatstr
#define included_formatstr

; This routine for taking a base-10 exponent and a string of digits and (without
; a decimal) and inserting a decimal, any leading zeros, stripping trailing
; zeros, and appending an exponent if needed.



; Define the absolute maximum number of digits in the result string.
; If FORMAT_LEN is bigger than this value, then it will be reduced.
#ifndef MAX_FORMAT_LEN
#define MAX_FORMAT_LEN 19
#endif

; Define this to use an external reference to get the number of digits used
;#define EXTERNAL_FORMAT_LEN <pointer>
;
; For example, TI-OS has a byte at fmtDigits:
;#define EXTERNAL_FORMAT_LEN fmtDigits

; This is the max number of digits in the output.
; If EXTERNAL_FORMAT_LEN is used and it is 0, then this will be used.
#ifndef FORMAT_LEN
#define FORMAT_LEN 18
#endif

; Define this to use an external reference for the max exponent before switching
; to enginieering mode.
;#define EXTERNAL_FORMAT_MAX_ENGINEERING  <pointer>

; Define the max exponent to use before switching to engineering format
; If none is defined, this uses FORMAT_LEN.
; If EXTERNAL_FORMAT_MAX_ENGINEERING is used and is 0 or larger than FORMAT_LEN,
; then this will be used.
;#define FORMAT_MAX_ENGINEERING


; Define this to use an external reference for the min exponent before switching
; to enginieering mode.
;#define EXTERNAL_FORMAT_MIN_ENGINEERING  <pointer>

; Define the largest negative exponent to use engineering format
; If EXTERNAL_FORMAT_MIN_ENGINEERING is used and is 0 or larger than FORMAT_LEN,
; then this will be used.
#ifndef FORMAT_MIN_ENGINEERING
#define FORMAT_MIN_ENGINEERING  -5  ; causes exponent of -5 to be enginierring
#endif

; For formatting, we need to define these three characters
; "Enginieering e" for values like "1.23456e10"
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

formatstr:
;Inputs:
;   HL points to the null-terminated string of digits
;   DE is the signed exponent.
;Outputs:
;   The string has leading and trailing zeros stripped, a decimal is placed
;   (if needed), and an exponent field is appended (if needed).
;Destroys:
;   HL, DE, BC, AF
;Notes:
;   This routine operates in-place. It assumes that there is enough space
;   allocated for the string. At most MAX_FORMAT_LEN+10 bytes is needed,
;   assuming the exponent can be up to 5 digits long.
;
; Skip over the negative sign, if any
  ld a,(hl)
  cp TOK_NEG
  jr nz,$+3
  inc hl
  push de ; save the exponent
  push hl

;Strip leading zeros
  ld d,h
  ld e,l
  ld a,'0'
  cp (hl)                           ;These two lines can be commented-out to save three
  jr nz,formatstr_no_leading_zeros  ;bytes at the expense of redundant processing.
formatstr_strip_leading_zeros:
  cpi
  jr z,formatstr_strip_leading_zeros
  dec hl

; HL points to the first non-'0' digit
; DE points to the first digit
; Copy bytes from HL to DE until 0x00 is reached at HL or FORMAT_LEN digits are copied
#ifdef EXTERNAL_FORMAT_LEN
  ld a,(EXTERNAL_FORMAT_LEN)
  or a
  jr nz,$+4
#endif
  ld a,FORMAT_LEN
#ifdef EXTERNAL_FORMAT_LEN
  cp MAX_FORMAT_LEN
  jr c,$+4
  ld a,MAX_FORMAT_LEN
#endif
  ld c,a

  xor a
  ld b,a
formatstr_copy_digits:
  cp (hl)
  ldi
  jp po,+_
  jr nz,formatstr_copy_digits
_:
  dec hl
  ld (hl),0

formatstr_no_leading_zeros:
; there are no more leading zeros
; Truncate the number of digits if necessary based on FORMAT_LEN

  call formatstr_remove_trailing_zeros
  pop hl  ; points to the first digit
  pop de  ; exponent

; Make sure the first digit isn't 0x00
  ld a,(hl)
  or a
  jr nz,+_
  ld (hl),'0'
  inc hl
  ld (hl),a
  ret
_:

  call formatstr_check_eng
  jr c,formatstr_eng
  inc de
  bit 7,d
  jr nz,formatstr_neg_exp
  ; Otherwise, we need to insert a decimal after DE digits (D is 0, though)
  ld b,d
  ld c,e
  xor a
  cp e
  jr z,formatstr_insert_decimal
  cpir
  ; If we have reached a 0x00, we may need to pad with zeros
  jr z,formatstr_pad_right
  ; otherwise, let's insert the decimal
formatstr_insert_decimal:
  ld a,(hl)
  or a
  ret z
  ld a,TOK_DECIMAL
formatstr_insert_decimal_loop:
  ld c,(hl) ; back up digit
  ld (hl),a
  inc hl
  ld a,c
  or a
  jr nz,formatstr_insert_decimal_loop
  ld (hl),a
  ret

formatstr_neg_exp:
; Need to pad -DE 0s to the left
  xor a
  ld c,a
  cpir
  ld b,a
  sub c
  ld c,a
  ;HL-1 is where to start reading bytes
  ;HL-DE is where to start writing bytes
  xor a
  ld d,a
  sub e     ; A is the number of 0s to write
  ld e,a
  ex de,hl
  add hl,de
  ex de,hl
  dec hl
  ; DE points to where to write the last byte
  ; HL points to where to read it from
  ; BC is the number of bytes to copy (it will be non-zero)
  ; A is the number of zeros to insert
  lddr
  ;now from DE backwards, write A '0's
  ex de,hl
  ld b,a
  ld (hl),'0'
  dec hl
  djnz $-3
  ; finally, write a '.'
  ld (hl),TOK_DECIMAL
  ret

formatstr_pad_right:
  ; append BC+1 0s
  dec hl
  inc bc
_:
  ld (hl),'0'
  cpi
  jp pe,-_
  ld (hl),0
  ret

formatstr_eng:
; need to insert a decimal after the first digit
  inc hl
  call formatstr_insert_decimal
  ld (hl),TOK_ENG
  inc hl
  bit 7,d
  jr z,formatstr_exp_to_str
  ld (hl),TOK_NEG
  inc hl
  xor a
  sub e
  ld e,a
  sbc a,a
  sub d
  ld d,a
formatstr_exp_to_str:
  ex de,hl
  ld a,'0'-1
  ld bc,-10000
_:
  inc a
  add hl,bc
  jr c,-_
  cp '0'
  jr z,$+4
  ld (de),a
  inc de

  ld a,'9'+1
  ld bc,1000
_:
  dec a
  add hl,bc
  jr nc,-_
  cp '0'
  jr z,$+4
  ld (de),a
  inc de

  ld a,'0'-1
  ld bc,-100
_:
  inc a
  add hl,bc
  jr c,-_
  cp '0'
  jr z,$+4
  ld (de),a
  inc de

  ld b,10
  ld a,l
_:
  add a,10
  dec b
  jr nc,-_
  ex de,hl
  jr z,formatstr_eng_last_digit
  set 4,b
  set 5,b
  ld (hl),b
  inc hl
formatstr_eng_last_digit:
  add a,'0'
  ld (hl),a
  inc hl
  ld (hl),0
  ret

formatstr_remove_trailing_zeros:
  ; first, seek the end of the string
  xor a
  ld c,a
  ld b,a
  cpir
  dec hl
  ld a,'0'
_:
  dec hl
  cp (hl)
  jr z,-_
  inc hl
  ld (hl),0
  ret

formatstr_check_eng:
; Return carry flag set if engineering format is required, else nc
;
; If the exponent is greater than FORMAT_MAX_ENGINEERING, then use enginieering
; notation. Note that FORMAT_MAX_ENGINEERING < 256, so check that D = -1 or 0
  ld a,d
  inc a
  jr z,formatstr_check_eng_neg
  add a,254
  ret c   ;the exponent is too big in magnitude, engineering format is required.
; The exponent is positive and less than 256

#ifdef EXTERNAL_FORMAT_MAX_ENGINEERING
  ld a,(EXTERNAL_FORMAT_MAX_ENGINEERING)
  or a
  jr nz,+_
#ifdef FORMAT_MAX_ENGINEERING
  ld a,FORMAT_MAX_ENGINEERING
#else
#ifdef EXTERNAL_FORMAT_LEN
  ld a,(EXTERNAL_FORMAT_LEN)
  or a
  jr nz,$+4
#endif
  ld a,FORMAT_LEN
#endif

_:
#else
#ifdef FORMAT_MAX_ENGINEERING
  ld a,FORMAT_MAX_ENGINEERING
#else
#ifdef EXTERNAL_FORMAT_LEN
  ld a,(EXTERNAL_FORMAT_LEN)
  or a
  jr nz,$+4
#endif
  ld a,FORMAT_LEN
#endif
#endif
  cp e
  ret

formatstr_check_eng_neg:
;The exponent is negative and greater than or equal to -256

#ifdef EXTERNAL_FORMAT_MIN_ENGINEERING
  ld a,(EXTERNAL_FORMAT_MIN_ENGINEERING)
  or a
  jr nz,$+3
  ld a,FORMAT_MIN_ENGINEERING
#else
  ld a,FORMAT_MIN_ENGINEERING
#endif
  cp e
  ccf
  ret
#endif
