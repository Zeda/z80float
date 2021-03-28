#ifndef included_singletof32
#define included_singletof32
#include "pushpop.z80"

singletof32:
;convert a "single" to an IEEE-754 binary32
;HL points to the input, BC is where to output
  call pushpop
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
  inc hl
  ld h,(hl)
;HADE is the single

;first, check for special values
  inc h
  dec h
  jr z,singletof32_special

;now decrement the exponent
;note: "single" here allows for an exponent as small as -127, but binary32 only
;      allows as small as -126. So this could mean an underflow. Lucky for us,
;      this would set the exponent to logical 0x00, which encodes 0 for binary32
singletof32_return_inf_nan:
  dec h

; Now we need to rotate HA right
;This puts the sign in the top bit, and moves one bit of the exponent to the top
;of the significand
singletof32_return:
  add a,a
  rr h
  rra

;now write the float
  ld l,c
  ld c,h
  ld h,b

;CADE holds the result
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),a
  inc hl
  ld (hl),c
  ret

singletof32_special:
;H is 0
;set DE to 0 as well
  ld d,h
  ld e,h

;A encodes whether the value is 0, inf, or NaN. We'll want to return A with the
;bottom 7 bits as 0
  ld l,a
  and $80

;if bit 6 is 1, then we have inf, so we keep DE==0
  bit 6,l
  jr nz,singletof32_return_inf_nan

;if bit 5 is 0, then we have 0
  bit 5,l
  jr z,singletof32_return

;Otherwise it is NaN, so we need to set DE to be non-zero
  inc e
  jr singletof32_return_inf_nan

#endif
