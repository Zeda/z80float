#ifndef included_f32mul2
#define included_f32mul2
#include "pushpop.z80"

f32mul2:
;x*2 ==> z
;
  call pushpop
; BC points to the output, put that in DE instead
  ld d,b
  ld e,c
; The first two bytes are unchanged, so copy
  ldi
  ldi
; The next byte's top bit is the start of the exponent
  ld a,(hl)
  add a,a
  ld c,a    ; save for later
  inc hl
  ld a,(hl)
  adc a,a
  ex de,hl
; A is the exponent, carry is the sign. If A is 0, then we are multiplying 0*2.
  jr z,f32mul2_done
; If A is 0xFF, then we have either +inf, -inf, or NaN. Multiplying by 2 gives
; the same result.
  inc a
  jr nz,f32mul2_done
  dec a
f32mul2_done:
  rra
  inc hl
  ld (hl),a
  ld a,c
  rra
  dec hl
  ld (hl),a
  ret
#endif
