#ifndef included_f32sqrt
#define included_f32sqrt

#include "pushpop.z80"
#include "routines/sqrt24_mant.z80"

f32sqrt:
;sqrt(x) ==> z

;return NaN if the input is negative, except:
;"IEEE 754 defines sqrt(-0.) as -0."
;   - https://stackoverflow.com/a/19232238/3303651

  call pushpop
  push bc
  ld b,(hl)
  inc hl
  ld e,(hl)
  inc hl
  ld d,(hl)
  ld a,d
  add a,a
  inc hl
  ld a,(hl)
  adc a,a
  jr c,f32sqrt_neg
  jr z,f32sqrt_zero
  inc a
  jr z,f32sqrt_infnan

;Now adjust the significand for our square-root routine
  set 7,d

;if the exponent is odd, need to shift right again
;also need to compute the new exponent as (A-1)>>1 + 0x3E
  ld c,0
  rra
  jr c,+_
  srl d
  rr e
  rr b
  rr c
  ; dec a
_:
  add a,3Fh

;save the exponent
  push af

  call sqrt24_mant

;DEL is the significand
  ld b,l
  pop af
  sla d
  srl a
  rr d
f32sqrt_zero:
  pop hl
  ld (hl),b
  inc hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),a
  ret
f32sqrt_neg:
  jr z,f32sqrt_neg0
  ld a,-1
f32sqrt_neg0:
  ; either writing a
  pop hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ;If A is FF, then upper bit is fine either way as we wrote NaN, but if it is
  ;00, we need to set the top bit to 1 so that sqrt(-0) => -0
  xor %10000000
  ld (hl),a
  ret

f32sqrt_infnan:
  pop hl
  ;If inf, then the significand is 0, else it is NaN
  ld a,d
  and %01111111 ;mask out the exponent bit
  or e
  or b
;If A is 0, then write +inf (significand is 0), else write non-zero for NaN
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  or %10000000
  ld (hl),a
  inc hl
  ld (hl), %01111111
  ret
#endif
