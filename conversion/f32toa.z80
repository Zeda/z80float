#ifndef included_f32toa
#define included_f32toa
#include "pushpop.z80"
#include "f32_pow10_LUT.z80"
#include "f32mul.z80"
#include "mov4.z80"
#include "common_str.z80"

;#define EXTERNAL_FORMAT_LEN                  ;Uses an external reference to get the format length
;#define EXTERNAL_FORMAT_LEN fmtDigits    ;Use for TI-OS

; Set a hard upper limit to the number of digits used
; This routine uses at most MAX_FORMAT_LEN+8 bytes of space
#ifndef MAX_FORMAT_LEN
#define MAX_FORMAT_LEN 8
#endif

; Set the default number of digits used. If EXTERNAL_FORMAT_LEN is defined and
; that value is 0 or greater than MAX_FORMAT_LEN, then FORMAT_LEN is used.
#ifndef FORMAT_LEN
#define FORMAT_LEN 6
#endif

; set the char to use for `e` notation
#ifndef TOK_ENG
#define TOK_ENG 'e'
#endif

; set the char to use for negatives
#ifndef TOK_NEG
#define TOK_NEG '-'
#endif

; set the char to use for decimal points
#ifndef TOK_DECIMAL
#define TOK_DECIMAL '.'
#endif


#define f32toa_x    scrap

f32toa:
;Inputs:
;   HL points to the input float
;   BC points to where the string gets written.
  call pushpop
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld (f32toa_x),de
  ld a,(hl)
  ld e,a
  add a,a
  inc hl
  ld a,(hl)
  ld d,a
  adc a,a
  ld h,b
  ld l,c
  inc a
  jp z,f32toa_return_infnan
  res 7,d
  ld (f32toa_x+2),de
  jr nc,+_
  ld (hl),TOK_NEG    ;negative sign
  inc hl
_:
;DEBC is the float, A is a copy of the exponent, HL points to the next byte to write
  dec a
  jp z,f32toa_return_0

  push hl

  ld (hl),'0' ; pad one more '0' to make room for rounding (i.e. 9.999999=>10.000000)
  inc hl

  push hl

; approximate the base-10 exponent as floor((A-127)*log10(2))
; which is approximately floor((A-127)*77/256)
  ld h,0
  ld l,a
  ld b,h
  ld c,a
  add hl,hl ;2
  add hl,hl ;4
  add hl,hl ;8
  add hl,bc ;9
  add hl,hl ;18
  add hl,bc ;19
  add hl,hl ;38
  add hl,hl ;76
  add hl,bc ;77
  ; now subtract 127*77 from HL and keep the upper 8 bits of the result
  ld a,205
  add a,l
  ld a,217
  adc a,h
  ; A is the approximate base-10 exponent
;f32toa_x needs to be multipled by 10^-A
  push af ; save the exponent
  call nz,f32toa_adjust
;the float is now on [1, 20)
;Let's no work on the float as a 0.24 fixed-point value
;we'll first need to extract the integer component
  ld hl,(f32toa_x)
  ld de,(f32toa_x+2)
  ld a,e
  rlca
  scf
  rra
  ld e,a
  ld a,d
  adc a,a
  sub 126
; A is how many bits to shift out of HLE
  ld b,a
  xor a
f32toa_first_digit_loop:
  add hl,hl
  rl e
  rla
  djnz f32toa_first_digit_loop

; A is the first digit
  pop bc  ; B is the base-10 exponent
  ex (sp),hl
  ld d,0
  cp 10
  jr c,f32toa_first_digit_fixed
  inc d
  dec hl
  ld (hl),'1'
  inc hl
  sub 10
f32toa_first_digit_fixed:
  add a,'0'
  ld (hl),a

  ld a,b
  ex (sp),hl
  pop bc
;A is the base-10 exponent
;BC is where to write the digits
;EHL is the 0.24 fixed-point number
;D is 1 if we have 2 digits already, else D is 0
  push af
  call f32toa_digits

;BC points to the last digit. We'll want to round!
  ld h,b
  ld l,c
  ld a,(hl)
  ld (hl),0
  add a,5
  jr f32toa_round_start
f32toa_round_loop:
  dec hl
  inc (hl)
  ld a,(hl)
f32toa_round_start:
  cp '9'+1
  jr nc,f32toa_round_loop
; the string is rounded
  inc hl
  ld (hl),0

  ; pop the exponent off the stack and sign-extend
  pop af
  ld e,a
  add a,a
  sbc a,a
  ld d,a
  pop hl
  ; check if rounding caused overflow; increment exponent if so
  ld a,(hl)
  cp '0'
  jp z,formatstr
  inc de
  jp formatstr


f32toa_digits:
; How many digits do we need?
#ifdef EXTERNAL_FORMAT_LEN
  ; we define the number of digits externally
  ld a,(EXTERNAL_FORMAT_LEN)

  ; if A is 0, use FORMAT_LEN
  or a
  jr nz,$+4
  ld a,FORMAT_LEN

  ; if A > MAX_FORMAT_LEN, set A to MAX_FORMAT_LEN
  cp MAX_FORMAT_LEN
  jr c,$+4
  ld a,MAX_FORMAT_LEN

  ; the first digit is written.
  ; if we only wanted 1 digit, then A is 0 and we should stop
  or a
  ret z
#else
  ; the number of digits is not declared externally
  ; the first digit is written.
  ; if we only wanted 1 digit, then A is 0 and we should stop
#if FORMAT_LEN < 2
  ret
#else
  ld a,FORMAT_LEN
#endif
#endif

; we want D more digits (an extra one for rounding)
f32toa_digits_loop:
  push af
  call f32toa_next_digit
  pop af
f32toa_digits_start:
  dec a
  jr nz,f32toa_digits_loop
  ret

f32toa_next_digit:
; multiply 0.EBC by 10
  push bc
  ld b,h
  ld c,l
  ld a,e
  ld d,6  ;overflow digit. We shift d 3 times, that 6 turns into a 0x30 == '0'

  add hl,hl
  adc a,a
  rl d

  add hl,hl
  adc a,a
  rl d

  add hl,bc
  adc a,e
  jr nc,$+3
  inc d

  add hl,hl
  adc a,a
  ld e,a
  ld a,d
  adc a,a

  pop bc
  inc bc
  ld (bc),a
  ret


f32toa_adjust:
  ld hl,f32_pown10_LUT-4
  jr c,f32toa_pow10LUT_mul
  neg
  ld hl,f32_pow10_LUT-4
f32toa_pow10LUT_mul:
;HL points to the first entry of the LUT
;(f32toa_x) is the accumulator
;bottom 6 bits of A control which terms to multiply by
  ld de,f32toa_x
  ld b,d
  ld c,e
; process f32toa_pow10LUT_mul_sub 6 times
  call f32toa_pow10LUT_mul_sub3
f32toa_pow10LUT_mul_sub3:
  call f32toa_pow10LUT_mul_sub
  call f32toa_pow10LUT_mul_sub
f32toa_pow10LUT_mul_sub:
  inc hl
  inc hl
  inc hl
  inc hl
  rra
  jp c,f32mul
  ret

f32toa_return_0:
  ld (hl),'0'
  inc hl
  ld (hl),0
  ret

f32toa_return_infnan:
  rl b  ; save the sign
  ld a,e
  add a,a
  ld de,(f32toa_x)
  or d
  or e
  ex de,hl
  ld hl,str_NaN
  jr nz,f32toa_return
  ld hl,str_inf
  rr b
  jr nc,f32toa_return
  ld a,'-'
  ld (de),a
  inc de
f32toa_return:
  jp mov4

#include "formatstr.z80"
#endif
