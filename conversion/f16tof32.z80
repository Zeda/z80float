#ifndef included_f16tof32
#define included_f16tof32
#include "pushpop.z80"

f16tof32:
;Inputs:
;   HL is the f16 input
;   BC is where to write the f32 float
;Destroys:
;   none
  call pushpop
;check for inf or NaN
  ld a,h
  and %01111100
  jr z,f16tof32_zero
  cp %01111100
  jr z,f16tof32_inf_nan
;it is not a special value

  ; we need to shift in the sign and exponent from HL
  ; We need to make roomfor 3 more bits of exponent, and we need to subtract 15
  ; for the original bias, and add 127 for the new bias, for a net of +112
  ; We'll init A to this so that the RLA instructions will pre-add
  ld a,%01100000
  add hl,hl
  rla               ;A = 1100000s
  rla               ;A = 100000s0
  rla               ;A = 00000s00 + 1
  rla               ;A = 0000s000 + 3
  add hl,hl
  rla               ;A = 000s000e + 6
  inc a             ;A = 000s000e + 7
  add hl,hl
  rla               ;A = 00s000ee + 14
  add hl,hl
  rla               ;A = 0s000eee + 28
  add hl,hl
  rla               ;A = s000eeee + 56

  ex de,hl
  ld h,b
  ld l,c
  ld (hl),0
  inc hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),a
  ret


f16tof32_zero:
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  ld a,h
  and %10000000
  ld (bc),a
  ret

f16tof32_inf_NaN:
  ld a,h
  and %00000011
  or l
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  or %10000000
  ld (bc),a
  inc bc
  ld a,h
  or %01111111
  ld (bc),a
  ret

#endif
