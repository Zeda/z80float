#ifndef included_f24div
#define included_f24div
#define included_f24inv

f24inv:
  ld c,a
  ex de,hl
  ld a,$3F
  ld hl,0
f24div:
;AHL * CDE ==> AHL
;Destroys BC,DE
;
  ;put the output sign in B
  ld b,a
  xor c
  add a,a
  ld a,b
  rla
  rrca
  ld b,a


;check for special values
;NaN/x ==> NaN
;0/fin ==> 0
;  0/0 ==> NaN
;inf/inf ==> NaN
;inf/x ==> inf
;x/NaN ==> NaN
;x/inf ==> 0
;x/0 ==> NaN

  and $7F
  jp z,f24div_0_x
  inc a
  jp m,f24div_infnan_x

  ld a,c
  and $7F
  jr nz,+_
  dec a
  ld h,a
  ld l,a
  ret
_:
  inc a
  jp m,f24div_x_infnan


;upper bit of B is the output sign
;first approximation of the exponent is
; (B&7F) - (C&7F) + 63
  res 7,c
  ld a,b
  and $7F
  add a,63
  sub c
  jr nc,$+4
  xor a     ;underflowed, so return 0
  ret

  cp $7F
  jr c,+_
f24div_return_inf:
  ld a,b
  or %01111111
  ld hl,0   ;overflow so return inf
  ret
_:


;now compute (1.HL / 1.DE)
; = (1+.HL)/(1+.DE)

; want 1.HL>1.DE, because then result is going to be 1.x
;so we can end up doing (.HL-.DE)/(1.DE) to 16 bits precision
  or a
  ld c,0    ;top bit of 1.HL-1.DE
  sbc hl,de
  jr nc,f24div_ready
  ;if carry is set, then DE was the larger of the two
  ;so we need to decrement the exponent and do
  ;(HL+DE)*2-DE
  dec a     ;decrement exponent
  ret z     ;return 0 if underflowed
  add hl,de
  add hl,hl
  rl c
  inc c
  sbc hl,de
  jr nc,f24div_ready
  dec c
f24div_ready:
;C.HL is the numerator, 1.DE is the denominator
;A is the exponent, B[7] is the sign
;save the exponent and sign
  push bc
  push af

;we can now commence 16  iterations of this division
  call fdiv24_div16

  pop de
  pop bc
  adc a,d
  jp p,+_
f24div_return_NaN:
  dec a
  ld h,a
  ld l,a
_:
  xor b
  and $7F
  xor b
  ret


fdiv24_div16:
;negate the divisior for more efficient division
;(16-bit addition is cheaper than subtraction)
  xor a
  sub e
  ld e,a
  ld a,0
  sbc a,d
  ld d,a
  sbc a,a
  dec a
  ld b,a

  ld a,c
  call fdiv24_div8
  rl c
  push bc
  call fdiv24_div8
  rl c
  ;check if  2*A.HL>1.DE
  add hl,hl
  adc a,a
  add hl,de
  adc a,b

  pop hl
  ld h,l
  ld l,c
  ld bc,0
  ld a,b
  adc hl,bc
  ret

fdiv24_div8:
  call fdiv24_div4
fdiv24_div4:
  call fdiv24_div2
fdiv24_div2:
  call fdiv24_div1
fdiv24_div1:
  rl c
  add hl,hl
  adc a,a
  ret z
  add hl,de
  adc a,b
  ret c
  sbc hl,de
  sbc a,b
  ret


f24div_0_x:
;make sure we aren't trying 0/NaN or 0/0
  ld a,c
  and $7F
  jr z,f24div_return_NaN
  inc a
  jp m,+_
  xor a
  ret
_:
  ld a,d
  or e
  ret z
  ld a,c
  ex de,hl
  ret
f24div_x_infnan:
  ld a,d
  or e
  ret z
  ld a,c
_:
  ex de,hl
  ret

f24div_infnan_x:
  ld a,h
  or l
  ld a,b
  ret nz
  ;make sure x is not inf NaN or 0
  ld a,c
  and $7F
  jr z,f24div_return_NaN
  inc a
  jp m,f24div_return_NaN
  ld a,b
  ret

#endif
