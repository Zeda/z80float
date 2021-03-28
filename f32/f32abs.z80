#ifndef included_f32abs
#define included_f32abs
#include "pushpop.z80"

f32abs:
;abs(x) ==> z
  call pushpop
  ld d,b
  ld e,c
  ldi
  ldi
  ldi
  ld a,(hl)
  and $7F
  ld (de),a
  ret
#endif
