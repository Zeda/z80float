#ifndef included_f24tof32
#define included_f24tof32
#include "pushpop.z80"

f24tof32:
;convert an "f24" float to an IEEE-754 binary32
;Input: AHL is the input float. BC points to where the f32 should be written.
;Destroys: None
  call pushpop
  ex de,hl
  ld h,b
  ld l,c
; Check for special values
  ld c,a  ;save for the sign
  add a,a
  jr z,f24tof32_return_0
  inc a
  inc a
  jr z,f24tof32_return_infnan
  add a,126
  rra
  rl c
  rra
  rr d
  rr e
  ld (hl),0
  rr (hl)
  inc hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),a
  ret
f24tof32_return_0:
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  rra
  inc hl
  ld (hl),a
  ret
f24tof32_return_infnan:
  ld a,d
  or e
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  or %10000000
  ld (hl),a
  inc hl
  ld a,c
  or %01111111
  ld (hl),a
  ret
#endif
