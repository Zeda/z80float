#ifndef included_f32_mulu8_divpow2
#define included_f32_mulu8_divpow2
#include "pushpop.z80"
#include "C_Times_BDE.z80"

;
; This is a special-purpose routine for multiplying an f32 float (x):
;   x * D*2^-E
; where D is a signed 8-bit integer.
f32_mulu8_divpow2:
; HL points to the float
; D is the multiplier
; E is the (signed) power of 2 to multiply by.
  call pushpop
  push bc
  push de
  ld c,d

  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
  add a,a
  ld b,a
  inc hl
  ld a,(hl)
  adc a,a
  jr z,f32_mulu8_divpow2_zero
  inc a
  jr z,f32_mulu8_divpow2_infnan
  ; check if we are multiplying by 0!
  inc c
  dec c
  jr z,f32_mulu8_divpow2_zero

  pop hl  ;
  push af

  ;extend the sign of L into H
  ld a,l
  add a,a
  sbc a,a
  ld h,a
  push hl

  ; B is shifted over by 2; we still need to shift a 1 back in
  scf
  rr b
  call C_Times_BDE  ;CAHL
  ld b,a
  pop de  ;DE is how much to add to the exponent
  pop af  ; A is the current exponent, carry is sign
  push af ; save carry

;CBHL
  ;need to add E+7 to the exponent, and shift CBHL up
  add a,e
  jr nc,$+3
  inc d

  add a,7
  jr nc,$+3
  inc d

  inc d
  jr z,f32_mulu8_divpow2_zero2
  dec d
  jr nz,f32_mulu8_divpow2_inf2

  ld e,a
  inc c
  dec c
  jr f32_mulu8_divpow2_adjust
f32_mulu8_divpow2_loop:
  dec de
  add hl,hl
  rl b
  rl c
f32_mulu8_divpow2_adjust:
  jp p,f32_mulu8_divpow2_loop
  sla c
  pop af
  ld a,e
  ld e,h
  ld d,b
  ld b,c
  .db $21 ;start of `ld hl,**` to eatt the next 2 bytes (dec a \ pop de)
f32_mulu8_divpow2_infnan:
  dec a
f32_mulu8_divpow2_zero:
  pop de
f32_mulu8_divpow2_return:
; sign is in carry, A is the exponent, (B/2)DE is the significand
  rra
  rr b
  pop hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),b
  inc hl
  ld (hl),a
  ret
f32_mulu8_divpow2_inf2:
  ld a,-1
  .db $FE
f32_mulu8_divpow2_zero2:
  xor a
  ld de,0
  ld b,d
  jr f32_mulu8_divpow2_return

#endif
