#ifndef included_f32mod1
#define included_f32mod1
#include "pushpop.z80"
#include "mov4.z80"
#include "f32rsub.z80"

f32mod1:
;x%1
  call pushpop
  push bc
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
  rlca
  scf
  rra
  ld c,a
  inc hl
  ld a,(hl)
  adc a,a
  pop hl
  ;0%1 ==> 0
  jr z,f32mod1_return_0
  ; NaN%1 ==> NaN, inf%1 ==> NaN
  inc a
  jr z,f32mod1_return_NaN
  jr nc,f32mod1_pos
  ; here, x < 0
  call f32mod1_pos
  ; if ans>0, need to return 1-ans instead
  ; note that z flag is set if ans is 0
  ret z
  dec hl
  dec hl
  dec hl
  ld b,h
  ld c,l
  ld de,f32_const_1
  jp f32rsub

f32mod1_pos:
; x is positive
; if  x < 1, return x
  sub 128
  jr c,f32mod1_modded
;shift out A+1 bits
  sub 7
  jr c,f32mod1_shift_bits
  ld c,d
  ld d,e
  ld e,0
  sub 8
  jr c,f32mod1_shift_bits
  ld c,d
  ld d,e
  sub 8
  jr nc,f32mod1_return_0
f32mod1_shift_bits:
  add a,8
  ld b,a
  ex de,hl
  ld a,c
  jr z,f32mod1_shift_bits_done
f32mod1_loop:
  add hl,hl
  adc a,a
  djnz f32mod1_loop
f32mod1_shift_bits_done:
  dec b
  ld c,a
  or h
  or l
  ex de,hl
  jr z,f32mod1_return_0
  ex de,hl
  ld a,c
  or a
  jr f32mod1_norm_start
f32mod1_norm_loop:
  dec b
  add hl,hl
  adc a,a
f32mod1_norm_start:
  jp p,f32mod1_norm_loop

; B is the exponent
  ex de,hl
  ld c,a
  ld a,b
f32mod1_modded:
; return A as the exponent, CDE is the modded significand
  add a,127
  ld (hl),e
  inc hl
  ld (hl),d
  srl a
  rl c
  rrc c
  inc hl
  ld (hl),c
  inc hl
  ld (hl),a
  or a
  ret



f32mod1_return_NaN:
  dec a
  .db $FE ; start of `cp *`, to skip the next byte
f32mod1_return_0:
  xor a
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  ret
#endif
