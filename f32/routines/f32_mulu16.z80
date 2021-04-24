#ifndef included_f32_mulu16
#define included_f32_mulu16
#include "pushpop.z80"
#include "C_Times_BDE.z80"

;
; This is a special-purpose routine for multiplying an f32 float (x):
;   x * DE
; where DE is an unsigned 16-bit integer.
f32_mulu16:
;Inputs:
;   HL points to the float
;   DE is the (unsigned) multiplier
;   BC points to the output
;Destroys:
;   None
  call pushpop
  push bc
  push de   ; multiplier
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld b,(hl)
  inc hl
  ld c,(hl)
  pop hl
  ld a,b
  add a,a
  ld a,c
  adc a,a
  jr z,f32_mulu16_return_pop1
  inc a
  jr z,f32_mulu16_infnan
  ld a,h
  or l
  jr z,f32_mulu16_zero

  ; uint16(HL) * f32(CBDE)
  push bc
  set 7,b
  ld c,h
  push hl

  call C_Times_BDE  ;CAHL
  ex (sp),hl
  ; need to push CA, preserving BDE, and put L in C
  ld h,c
  ld c,l
  ld l,a
  push hl
  call C_Times_BDE  ;CAHL
  pop de
  pop ix
; 0CAHL
;+DEIX0
  ld b,a
  ld a,c
  ld c,h
  add ix,bc
  adc a,e
  ld e,a
  adc a,d
  sub e
  push ix
  pop bc
  ld h,c
  ld d,e
  ld e,b
  pop bc
  sla b
  rl c    ; C is the exponent
  push af ; save the sign, also A
; add 16+1 to the sign. Later we check for overflow, the +1 makes it so we don't
; need to check for 0xFF, we just need to decrement later
  ld a,17
  add a,c
  ld c,a
  ld a,0
  rla
  ld b,a
  pop af    ; restore A
  push af   ; but save the sign
;ADEHL is the denormalized significand, need to normalize it. BC is the exponent
  or a
  jr f32_mulu16_norm_loop_start
f32_mulu16_norm_loop:
  dec bc
  add hl,hl
  rl e
  rl d
  adc a,a
f32_mulu16_norm_loop_start:
  jp p,f32_mulu16_norm_loop
; C is the exponent, ADEHL is the significand
  sla h
  jr nc,f32_mulu16_rounded
  inc e
  jr nz,f32_mulu16_rounded
  inc d
  jr nz,f32_mulu16_rounded
  inc a
  jr nz,f32_mulu16_rounded
  inc bc
f32_mulu16_rounded:
  ld h,a
  pop af
  dec b
  jr z,f32_mulu16_inf
  dec c
  ld a,h
  rr c
  rla
  rrca
  ld b,a
  jr f32_mulu16_return_pop1

f32_mulu16_infnan:
  ld a,h
  or l
  jr nz,f32_mulu16_return_pop1
  ld b,-1
  jr f32_mulu16_return_pop1
f32_mulu16_zero:
  ld b,a
  ld c,a
  ld d,a
  ld e,a
f32_mulu16_return_pop1:
  pop hl
f32_mulu16_return:
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),b
  inc hl
  ld (hl),c
  ret
f32_mulu16_inf:
  ld d,b
  ld e,b
  ld bc,%1000000011111110
  rr c
  jr f32_mulu16_return_pop1
#endif
