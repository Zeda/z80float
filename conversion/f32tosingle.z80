#ifndef included_f32tosingle
#define included_f32tosingle
#include "pushpop.z80"

f32tosingle:
;convert an IEEE-754 binary32 to this library's "single" format.
;HL points to the input, BC is where to output
  call pushpop

;no matter what, the bottom 16 bits can be the same
  ld d,b
  ld e,c
  ld a,(hl)
  ldi
  or (hl)
  ldi
  ld c,a    ;the OR of the bottom two bytes. Needed for NaN vs. Inf
  ld a,(hl)
  inc hl
  ld h,(hl)

;first, check for special values
  add a,a
  ld l,a
  ld a,h
  adc a,a
  jr z,f32tosingle_return_0
  inc a
  jr z,f32tosingle_inf_NaN
;carry is the new sign
  rr l

;AL needs to be written to DE
  ex de,hl
  ld (hl),e
  inc hl
  ld (hl),a
  ret

f32tosingle_inf_NaN:
;if C is 0 and L is 0, then it is inf, else NaN
  rr h
  cp c
  jr nz,+_
  cp l
  jr nz,+_
;  add a,$40
  .db $F6     ;\  this branch becomes:
_:            ; |    or $C6   ;set's bit 7, which is what we want
  add a,$40   ;/     ld b,b   ;might cause issues on eZ80
  sla h

f32tosingle_return_0:
  rra
  ld (de),a
  inc de
  xor a
  ld (de),a
  ret


#endif
