#ifndef included_f24tof16
#define included_f24tof16

f24tof16:
;convert an f24 float to an IEEE-754 binary16 format.
;Input: AHL is the input float
;Output: HL is the f16 float
;Destroys: AF, C

  ; check for special values
  add a,a
  jr z,f24tof16_return_0_noA
  inc a
  inc a
  jr z,f24tof16_return_infnan
  rr c    ; save the sign
; subtract 63 and add 15 to the sign, net -48
; Note that exponent is currently doubled plus two
  sub 98
  jr c,f24tof16_return_0
  rra
  cp 31
  jr nc,f24tof16_return_inf
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

f24tof16_return_infnan:
  ld a,%11111000
  rra
  ld c,a  ; sign and exponent set
  ld a,h
  or l
  ld l,a  ; if the input was NaN, this will be non-zero, else zero
  ld h,c
  ret

f24tof16_return_inf:
  rl c
  ld a,%11111000
  rra
  ld h,a
  ld l,0
  ret

f24tof16_return_0:
  xor a
  rl c
f24tof16_return_0_noA:
  ld l,a
  rra     ; shift the sign back in
  ld h,a
  ret
#endif
