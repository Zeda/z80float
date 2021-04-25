#ifndef included_f32tof16
#define included_f32tof16

f32tof16:
;convert an IEEE-754 binary32 to an IEEE-754 binary16 format.
;Input: HL points to the input float
;Output: HL is the f16 float
;Destroys: AF, BC, DE

  ld c,(hl)
  inc hl
  ld e,(hl)
  inc hl
  ld a,(hl)
  ld d,a
  add a,a
  inc hl
  ld a,(hl)
  adc a,a
  jr z,f32tof16_return_0_noA
  inc a
  jr z,f32tof16_return_infnan
  rr c    ; save the sign, we no longer need C

  sub 113
  jr c,f32tof16_return_0
  cp 31
  jr nc,f32tof16_return_inf
  ;A is the exponent
  ;(DE>>5)&%0000001111111111 encodes the significand
  ex de,hl
  add hl,hl
  ; rla   ; we want to omit the top bit of the significand
  add hl,hl
  rla
  add hl,hl
  rla
  ; now get the sign
  add a,a
  rl c
  rra
  ; we'll round
  sla l
  ld l,h
  ld h,a
  ret nc
  inc hl
  ret

f32tof16_return_infnan:
  ld a,%11111000
  rra
  ld h,a  ; sign and exponent set
  ld a,d
  add a,a
  or e
  or c
  ld l,a  ; if the input was NaN, this will be non-zero, else zero
  ret

f32tof16_return_inf:
  ld a,c
  or %01111100
  ld l,0
  ld h,a
  ret

f32tof16_return_0:
  xor a
  rl c
f32tof16_return_0_noA:
  ; ld l,a  ; Not necessary, just need the exponent = 0
  rra     ; shift the sign back in
  ld h,a
  ret
#endif
