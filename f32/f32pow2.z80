#ifndef included_f32pow2
#define included_f32pow2
#include "pushpop.z80"
#include "mov4.z80"
#include "f32constants.z80"
#include "f32horner_step.z80"
#include "f32add.z80"

#define f32pow2_x scrap

f32pow2:
;if x is on [0,1):
;  2^x = 1.000000001752 + x * (0.693146989552 + x * (0.2402298085906 + x * (5.54833215071e-2 + x * (9.67907584392e-3 + x * (1.243632065103e-3 + x * 2.171671843714e-4)))))
;Please note that usually I like to reduce to [-.5,.5] as the extra overhead is usually worth it.
;In this case, our polynomial is the same degree, with error different by less than 1 bit, so it's just a waste to range-reduce in this way.
  call pushpop
  push bc
  ld de,f32pow2_x
  ldi
  ldi
  ld a,(hl)
  add a,a
  ldi
  ld a,(hl)
  ld c,a
  res 7,a
  ld (de),a
  ld a,c
  adc a,a
  pop de
  ; carry is the sign, A is the exponent
  jp z,f32pow2_return_1
  inc a
  jp z,f32pow2_return_infnan
;A-1 is the exponent, carry is the sign
; if the exponent >= 7 and carry is set, return 0
; if the exponent >= 7 and carry is reset, return +inf
  rl b  ;save the carry
  cp 135
  jp nc,f32pow2_overflow
  cp 121
  jp c,f32pow2_return_0
;

; now we need to extract the integer part from x while performing mod1 on it
; extract into C
  ld c,0
  sub 128
  jr c,f32pow2_int_extracted
  push bc ; save the sign
  ld b,a
  ld hl,(f32pow2_x)
  ld a,(f32pow2_x+2)
  or %10000000
  inc b
f32pow2_int_extract_loop:
  add hl,hl
  adc a,a
  rl c
  djnz f32pow2_int_extract_loop
; Now normalize the significand
; make sure the significand isn't zero
  ld b,a
  or h
  or l
  jr z,f32pow2_int_extract_0
  ld a,b
; shift the significand up until there is a 1 in the top bit
  ld b,$7E  ; exponent of the fractional portion
  or a
  jr f32pow2_int_extract_norm
f32pow2_int_extract_norm_loop:
  dec b
  add hl,hl
  adc a,a
f32pow2_int_extract_norm:
  jp p,f32pow2_int_extract_norm_loop
f32pow2_int_extract_0:
  ld (f32pow2_x),hl
  add a,a
  srl b
  rra
  ld l,a
  ld h,b
  ld (f32pow2_x+2),hl
  pop af  ; LSB is sign
  ld b,a
f32pow2_int_extracted:

; if the sign is negative, then perform 1-X and -c-1 ==> c
  rr b
  jr nc,+_
  ld a,c
  cpl
  push af
  push de
  ld hl,f32_const_1
  ld de,f32pow2_x
  ld b,d
  ld c,e
  call f32sub
  pop de
  pop af
  ld c,a
_:
  ; sign-extend the exponent
  ld a,c
  add a,a
  sbc a,a
  ld b,a
  push bc ; save the exponent

;x is now on [0, 1)

;for 0 <= x <= 1
;2^x = 1 + x * (0.69314706325531005859375 + x * (0.240229070186614990234375 + x * (5.54862879216670989990234375e-2 + x * (9.67352092266082763671875e-3 + x * (1.248489017598330974578857421875e-3 + x * 2.15564403333701193332672119140625e-4)))))

; DE points to our output (accumulator)
  ld hl,f32pow2_a7
  push de
  ldi
  ldi
  ldi
  ld a,(hl)
  ld (de),a
  pop bc          ; points to accumulator
  ld de,f32pow2_x ; points to x

  ld hl,f32pow2_a6
  call f32horner_step
  ld hl,f32pow2_a5
  call f32horner_step
  ld hl,f32pow2_a4
  call f32horner_step
  ld hl,f32pow2_a3
  call f32horner_step
  ld hl,f32pow2_a2
  call f32horner_step
  ld hl,f32pow2_a1
  call f32horner_step
  ld h,b
  ld l,c
  pop bc
  ; need to add BC to the exponent
  inc hl
  inc hl
  ld a,(hl)
  add a,a
  ld (hl),a
  inc hl
  ld a,(hl)
  adc a,a
  add a,c
  jr nc,$+4
  or a  ; reset the carry flag if it is set
  inc b
  ;if b is -1, then underflow
  ;elsif b is 0, then good
  ;else overflow
  inc b
  jr z,f32pow2_exp_overflow
  djnz f32pow2_exp_underflow
  .db $06 ; start of `ld b,*` to eat the next byte
f32pow2_exp_underflow:
  xor a
  rra
  ld (hl),a
  dec hl
  rr (hl)
  ret

f32pow2_exp_overflow:
  ld (hl),%01111111
  dec hl
  ld (hl),%10000000
  xor a
  dec hl
  ld (hl),a
  dec hl
  ld (hl),a
  ret

f32pow2_overflow:
  rr b
  jr c,f32pow2_return_0
f32pow2_return_inf:
  ld hl,f32_const_inf
  jr f32pow2_return
f32pow2_return_0:
  ld hl,f32_const_0
  jr f32pow2_return
f32pow2_return_1:
;2^0 ==> 1
  ld hl,f32_const_1
f32pow2_return:
  jp mov4

f32pow2_return_infnan:
;2^inf ==> inf
;2^-inf ==> 0
;2^NaN ==> NaN

  ld hl,f32pow2_x
  ;if carry is reset, return OP1
  jp nc,mov4
  ;else if OP1 is NaN, return Nan
  ;else return 0
  ld a,(hl)
  ldi
  or (hl)
  ldi
  ld c,a
  ld a,(hl)
  add a,a
  or c
  ; if zero, return 0, else top bit needs to be set
  add a,255
  sbc a,a
  ld (de),a
  inc de
  ld (de),a
  ret

f32pow2_a1 = f32_const_1
; .db $00,$00,$80,$3F  ;1.000000001752
f32pow2_a2:
.db $16,$72,$31,$3F  ;0.69314706325531005859375
f32pow2_a3:
.db $9C,$FE,$75,$3E  ;0.240229070186614990234375
f32pow2_a4:
.db $97,$45,$63,$3D  ;5.54862879216670989990234375e-2
f32pow2_a5:
.db $B0,$7D,$1E,$3C  ;9.67352092266082763671875e-3
f32pow2_a6:
.db $57,$A4,$A3,$3A  ;1.248489017598330974578857421875e-3
f32pow2_a7:
.db $21,$09,$62,$39  ;2.15564403333701193332672119140625e-4



#endif
