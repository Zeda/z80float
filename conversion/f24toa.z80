#ifndef included_f24toa
#define included_f24toa

; Lot's of #define statements
; This first batch is to make sure char_NEG, TOK_NEG, char_DEC, and TOK_DECIMAL
; are defined. This is because I accidentally used two different standards early
; on, and then I decided to share common routines. Let this be a lesson, because
; now I have to do convoluted trickery for compatibility -__-

#ifndef char_NEG
#ifdef TOK_NEG
#define char_NEG TOK_NEG
#else
#define char_NEG '-'
#endif
#endif

#ifndef char_DEC
#ifdef TOK_DECIMAL
#define char_DEC TOK_DECIMAL
#else
#define char_DEC '.'
#endif
#endif

#ifndef TOK_NEG
#ifdef char_NEG
#define TOK_NEG char_NEG
#else
#define TOK_NEG '-'
#endif
#endif

#ifndef TOK_DECIMAL
#ifdef char_DECIMAL
#define TOK_DECIMAL char_DEC
#else
#define TOK_DECIMAL '.'
#endif
#endif


; Now we'll set some defaults


; Define the absolute maximum number of digits in the result string.
; If FORMAT_LEN is bigger than this value, then it will be reduced.
#ifndef MAX_FORMAT_LEN
#define MAX_FORMAT_LEN 7
#endif

; Define this to use an external reference to get the number of digits used
;#define EXTERNAL_FORMAT_LEN <pointer>
;
; For example, TI-OS has a byte at fmtDigits:
;#define EXTERNAL_FORMAT_LEN fmtDigits

; This is the max number of digits in the output.
; If EXTERNAL_FORMAT_LEN is used and it is 0, then this will be used.
#ifndef FORMAT_LEN
#define FORMAT_LEN 5
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
#define FORMAT_MIN_ENGINEERING  -3  ; causes exponent of -3 to be enginierring
#endif



; Finally, includes
#include "../f24/f24mul.z80"
#include "../f24/f24pow10_LUT.z80"
#include "formatstr.z80"


f24toa:
;converts a 24-bit float to a string
;Inputs:
;   AHL is the float to convert
;   DE points to where to write the string
;Output:
;   HL pointing to the string
;Destroys:
;   A,DE,BC
;Notes:
;   Uses up to 12 bytes to store the string

  ld b,a  ; save the exponent

  ; check if the input is 0
  add a,a
  jr nz,+_
  ex de,hl
  jr nc,$+5
  ld (hl),char_NEG
  inc hl
  ld (hl),'0'
  inc hl
  ld (hl),0
  dec hl
  ret nc
  dec hl
  ret
_:

;check if the input is inf or NaN
  push de
  cp $FE
  jr nz,f24toa_finite
  ld a,h
  or l
  ld hl,s_NaN
  jr nz,+_
  ld hl,s_NEGinf
  bit 7,b
  jr nz,+_
  inc hl
_:
  ldi
  ldi
  ldi
  ldi
  ld a,(hl)
  ld (de),a
  pop hl
  ret
f24toa_finite:

;BHL is the float and it is not a special number
;save the exponent

;write a negative sign if needed
  ld a,b
  add a,a
  jr nc,+_
  ex de,hl
  ld (hl),char_NEG
  inc hl
  ex de,hl
_:

;save the string pointer
  push de

;save the significand
  push hl

;Get an estimate of the power of 10
;multiply A/2 by 77

  ld l,a
  ld h,0
  rrca
  ld e,a
  ld d,h

  add hl,hl ;4
  add hl,hl ;8
  add hl,de ;9
  add hl,hl ;18
  add hl,de ;19
  add hl,hl ;38
  add hl,hl ;76
  add hl,de ;77

;now HL is approximately (exp+63)*log10(2)*256

;first, save H, the power-of-10 guess
;also restore the significand
  ld e,h
  ex (sp),hl

;now multiply by the appropriate power-of-10 to get our input in the [1,10]-ish
;range. Unlike the higher-precision floats, it is actually smaller to store the
;whole table. This will also be slightly more accurate and also faster.
  push hl
  ld hl,f24pow10_LUT
  add hl,de
  sla e
  add hl,de
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld c,(hl)
  ld a,b
  and $7F
  pop hl
  call f24mul

  cp 63
  jr nc,+_
  ;decrement the power of 10 and multiply by 10
  pop de
  dec d
  push de
  ld c,$42
  ld de,$4000
  call f24mul
_:

;now AHL is a float on [1,20]
;let's convert it to an 8.16 unsigned fixed-point number
  sub 63
  ld b,a
  ld a,1
  jr z,+_
  add hl,hl
  rla
  djnz $-2
_:

;for rounding porpoises, add 3 to A:HL
  ld bc,3
  add hl,bc
  adc a,b

  pop bc    ;power-of-10 is in B
  pop de    ;where to write the output


  cp 10
  jr nc,+_
  add a,'0'
  ld (de),a
  inc de
;get a second digit
  push bc
  call f24toa_sub
  jr f24toa_write_digits
_:
  inc b
;save the power-of-10 exponent
  push bc

;for rounding purposes, add another 30 to HL
  ld bc,30
  add hl,bc
  adc a,b

  ;the first digit is either a 1 or a 2
  ex de,hl
  ld (hl),'1'
  sub 20
  jr c,$+4
  inc (hl)
  .db $01
  add a,10
  inc hl
  ex de,hl
  add a,'0'
  ld (de),a
  inc de
f24toa_write_digits:
;get the next three digits
  call f24toa_sub
  call f24toa_sub
  call f24toa_sub
  xor a
  ld (de),a

; need to determine what to do with the power-of-10 exponent
  pop af

  pop hl  ; pointer to the string
  push hl
  sub 19
  ld e,a
  add a,a
  sbc a,a
  ld d,a
  call formatstr
  pop hl
  ret
;
f24toa_sub:
;now need to multiply 0.HL by 10 and add '0'
  xor a
  ld b,h
  ld c,l
  add hl,hl \ rla
  add hl,hl \ rla
  add hl,bc \ adc a,'0'/2
  add hl,hl \ rla
  ld (de),a
  inc de
  ret
#endif
