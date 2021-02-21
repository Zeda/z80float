#ifndef included_div24_24
#define included_div24_24

div24_24:
;BHL/CDE
;BHL<CDE
;return result as 0.BDE, with carry set to 1 if rounding should round up
;speed: 167+3*div24_24_sub_8 + div24_24_sub_1
;min: 1924
;max: 2499
;avg: 2167.75
; negate BDE
  xor a
  sub e
  ld e,a

  ld a,0
  sbc a,d
  ld d,a

  sbc a,a
  sub a,c
  ld c,a

;
  ld a,b
  call div24_24_sub_1 ; we need an extra iteration for rounding
  call div24_24_sub_8
  push bc
  call div24_24_sub_8
  push bc
  call div24_24_sub_8
  ;carry is for rounding
  pop de
  ld e,b
  pop bc
  ret


div24_24_sub_8:
; speed: 567+8*{8,{0,23}}
; min: 567
; max: 751
; avg: 645
  call div24_24_sub_4
div24_24_sub_4:
  call div24_24_sub_2
div24_24_sub_2:
  call div24_24_sub_1
div24_24_sub_1:
;56+{8,{0,23}}
  rl b
  add hl,hl
  adc a,a
  jr c,div24_24_sub_overflow
  add hl,de
  adc a,c
  ret c
  sbc hl,de
  sbc a,c
  ret
div24_24_sub_overflow:
  add hl,de
  adc a,c
  scf
  ret
#endif
