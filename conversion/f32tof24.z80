#ifndef included_f32tof24
#define included_f32tof24

f32tof24:
;convert an IEEE-754 binary32 to this library's "f24" format.
;Input: HL points to the input float
;Output: AHL is the f24 float
;Destroys: DE,BC

  ld a,(hl)
  ld c,a
  add a,a
  inc hl
  ld a,(hl)
  rla
  ld e,a
  inc hl
  ld a,(hl)
  rla
  ld d,a
; DE is the significand of the output
  inc hl
  ld a,(hl)
  adc a,a
  jr z,f32tof24_return_0_noA
  inc a
  jr z,f32tof24_return_infnan
  rr c    ; save the sign
  sub 65
  jr c,f32tof24_return_0
  cp 127
  jr nc,f32tof24_return_inf
  add a,a
  rl c
  rra
  ex de,hl

; round
  bit 6,c
  ret z
  inc l
  ret z
  inc h
  ret z
  inc a
  ret

f32tof24_return_infnan:
  dec a
  rra
  ld b,a  ; save exponent/sign
  ld a,c
  or d
  or e
  ld d,a
  ld a,b
  ex de,hl
  ret

f32tof24_return_inf:
  ld a,c
  or %01111111
  ld hl,0
  ret

f32tof24_return_0:
  xor a
  rl c
f32tof24_return_0_noA:
  ld h,a
  ld l,a
  rra     ; shift the sign back in
  ret
#endif
