#ifndef included_f24sqrt
#define included_f24sqrt

#include "sqrt16.z80"

f24sqrt:
;sqrt(AHL) ==> AHL


;return NaN if the input is negative, except:
;"IEEE 754 defines sqrt(-0.) as -0."
;   - https://stackoverflow.com/a/19232238/3303651

  add a,a
  jr nc,+_
  rra
  ret z
  ld a,$7F
  ld h,a
  ret
_:
  ret z

;so 0 and negative numbers are taken care of
;check if input is NaN or inf
;sqrt(NaN) ==> NaN
;sqrt(inf) ==> inf
  rra
  cp $7F
  ret z

;Now adjust the significand for our square-root routine
  ;scf
  ld c,0
  rr h
  rr l
  rr c

;if the exponent is odd, need to shift right again
;also need to compute the new exponent as (A-1)>>1 + 32
  dec a
  rra
  jr c,+_
  rr h
  rr l
  rr c
_:
  add a,32

;save the exponent
  push af
  call f24sqrt_sqrt

;need to generate one more bit and a rounding bit
;this can be done by doing (AHL/2)/DE for two iterations
;Note that A is either 0 or 1
  or a
  ld bc,0
  sbc hl,de
  sbc a,b
  jr nc,$+5
  add hl,de
  adc a,b
  inc c
  add hl,hl
  adc a,a
  sbc hl,de
  sbc a,b
;bottom bit in C is the inverse of what needs to be shifted in to DE
;meanwhile, carry flag is going to be used for rounding
  ld a,c
  rra
  ccf
  ex de,hl
  adc hl,hl
  add a,a   ;now A is 0
  ld c,a
  ccf
  adc hl,bc
  pop de
  adc a,d
  ret

f24sqrt_sqrt:
;returns HL as the 9.7 fixed-point square-root of the upper 18 bits of HLC

  call sqrtHL   ;expects returns A as sqrt, HL as remainder, D = 0
  add a,a
  ld e,a
  rl d

  ld a,c
  sll e \ rl d
  add a,a \ adc hl,hl
  add a,a \ adc hl,hl
;A is now 0
  sbc hl,de
  jr nc,+_
  add hl,de
  dec e
  .db $FE     ;start of `cp *`
_:
  inc e


  sll e \ rl d
  add hl,hl
  add hl,hl
  sbc hl,de
  jr nc,+_
  add hl,de
  dec e
  .db $FE     ;start of `cp *`
_:
  inc e

  sll e \ rl d
  add hl,hl
  add hl,hl
  sbc hl,de
  jr nc,+_
  add hl,de
  dec e
  .db $FE     ;start of `cp *`
_:
  inc e

  sll e \ rl d
  add hl,hl
  add hl,hl
  sbc hl,de
  jr nc,+_
  add hl,de
  dec e
  .db $FE     ;start of `cp *`
_:
  inc e

;Now we have four more iterations
;The first two are no problem
  sll e \ rl d
  add hl,hl
  add hl,hl
  sbc hl,de
  jr nc,+_
  add hl,de
  dec e
  .db $FE     ;start of `cp *`
_:
  inc e

  sll e \ rl d
  add hl,hl
  add hl,hl
  sbc hl,de
  jr nc,+_
  add hl,de
  dec e
  .db $FE     ;start of `cp *`
_:
  inc e

sqrt32_iter15:
;On the next iteration, HL might temporarily overflow by 1 bit
  sll e \ rl d      ;sla e \ rl d \ inc e
  add hl,hl
  add hl,hl       ;This might overflow!
  jr c,sqrt32_iter15_br0
;
  sbc hl,de
  jr nc,+_
  add hl,de
  dec e
  jr sqrt32_iter16
sqrt32_iter15_br0:
  or a
  sbc hl,de
_:
  inc e

;On the next iteration, HL is allowed to overflow, DE could overflow with our current routine, but it needs to be shifted right at the end, anyways
sqrt32_iter16:
  ld c,a        ;0x00
  add hl,hl
  rla
  add hl,hl
  rla
;AHL - (DE+DE+1)
  sbc hl,de \ sbc a,c
  inc e
  or a
  sbc hl,de \ sbc a,c
  ret p
  add hl,de
  adc a,c
  dec e
  add hl,de
  adc a,c
  ret

#endif
