#ifndef included_f32mul
#define included_f32mul
#include "pushpop.z80"
#include "mul24_stack_based.z80"

f32mul:
;x * y ==> z
;
  call pushpop
  push bc
  push de
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld b,(hl)
  ld a,b
  add a,a
  inc hl
  ld a,(hl)
  ld c,a
  adc a,a
  pop hl
  jp z,f32mul_0_op2
  inc a
  jp z,f32mul_infnan_op2
  dec a
  push af   ;exponent of the first operand

  push de
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld c,(hl)
  ld a,c
  add a,a
  inc hl
  ld a,(hl)
  adc a,a
  jr z,f32mul_op1_0
  inc a
  jr z,f32mul_op1_infnan
  pop hl
  ex de,hl
  push af   ;exponent of the second operand
;BDE*CHL
  set 7,b
  set 7,c

  call mul24
;BHLDEA
  pop af
  rr e
  bit 7,b
  jr nz,+_
  dec a
  sla d
  adc hl,hl
  rl b
_:

  sla d
  ex de,hl
  jr nc,+_
  inc e
  jr nz,+_
  inc d
  jr nz,+_
  inc b
  jr nz,+_
  inc a
_:
  ld h,a  ; first exponent
  pop af  ; A is the second exponent
  rr l    ; top 2 bits are the signs
  ; ultimately need H+A-0x7F
  add a,h
  ld h,0
  rl h
  sub $7E
  dec a
  jr nc,$+3
  dec h

  ; If H is 1, we have an inf, -1 we have 0
  dec h
  jp z,f32mul_inf_l
  inc h
  jr z,$+3
  xor a

  sla b

  ld c,a  ;the exponent
  ld a,l
  and %11000000
  jp pe,$+4
  scf

f32mul_return2:
  rr c
  rr b

f32mul_return:
  pop hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),b
  inc hl
  ld (hl),c
  ret

f32mul_op1_0:
  pop bc
  rra
  ld c,a
  pop af
  rra
  xor c
  and %10000000
  ld c,a
  ld b,0
  jr f32mul_return

f32mul_op1_infnan:
  pop hl
  rra
  ld b,a
  pop af
  rra
  xor b ;top bit is sign
  ld h,a

  ld a,c
  add a,a
  or d
  or e
  ld b,a
  add hl,hl
  ld c,-1
  jr f32mul_return2

f32mul_0_op2:
;if OP2 is inf or NaN, retun NaN, else return 0
  rra
  ld b,a     ;save the sign
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
  add a,a
  ld c,a
  inc hl
  ld a,(hl)
  ld h,a
  adc a,a
  inc a
  jr z,f32mul_return_NaN
  rra
  xor b
  and %10000000
  ld c,a
  ld b,0
  jr f32mul_return
f32mul_return_NaN:
  ld bc,$FF7F
  jr f32mul_return

f32mul_infnan_op2:
;if OP2 is 0 or NaN, return NaN, else return OP1 with adjusted sign
  rra
  ld c,a  ;save the sign
  ld a,b
  add a,a
  or d
  or e
  jr nz,f32mul_return_NaN
f32mul_inf_op2:
  inc hl
  inc hl
  ld a,(hl)
  inc hl
  add a,a
  ld a,(hl)
  adc a,a
  jr z,f32mul_return_NaN
  inc a
  jr z,f32mul_check_NaN
  rra
  xor c
  and %10000000
  or %01111111
  ld c,a
  jr f32mul_return
f32mul_check_NaN:
  rra
  xor c
  and %10000000
  or %01111111
  ld c,a
  dec hl
  ld a,(hl)
  add a,a
  dec hl
  or (hl)
  dec hl
  or (hl)
  jr nz,f32mul_return_NaN
  jr f32mul_return



f32mul_inf_l:
  ld a,l
  and %11000000
  jp pe,$+4
  scf
f32mul_inf:
;carry is sign
  pop hl
  ld (hl),0
  inc hl
  ld (hl),0
  inc hl
  ld (hl),%10000000
  inc hl
  ld a,-1
  rra
  ld (hl),a
  ret
#endif
