#ifndef included_f32tof64
#define included_f32tof64
#include "pushpop.z80"

;bias is 1023, so 0x03FF is exponent of 0
;sign is 1 bit
;exponent is 11 bits
;mantissa is 53 bits (top bit is implicit)


f32tof64:
;convert an IEEE-754 binary32 to an IEEE-754 binary64 float.
;Input: HL points to the input float, BC points to where to output
;Destroys: None
  call pushpop
  xor a
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc

  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld a,(hl)
  inc hl
  ld h,(hl)
  ld l,a
  ex de,hl
; The float is in DEHL
  ld a,e
  add a,a
  ld a,d
  adc a,a
  jr z,f32tof64_zero
  inc a
  jr z,f32tof64_infnan

  ; to the exponent, substract 127 and add 1023 for a net of +896
  ld a,%01100000
  add hl,hl
  rl e
  rl d
  rla           ;1110000s + 0
  rla           ;110000s0 + 0
  rla           ;10000s00 + 1
  rla           ;0000s000 + 3
  add hl,hl
  rl e
  rl d
  rla           ;000s000e + 6
  inc a         ;000s000e + 7
  add hl,hl
  rl e
  rl d
  rla           ;00s000ee + 14
  add hl,hl
  rl e
  rl d
  rla           ;0s000eee + 28
  add hl,hl
  rl e
  rl d
  rla           ;s000eeee + 56


  push hl
  ld h,b
  ld l,c
  pop bc
  ld (hl),c
  inc hl
  ld (hl),b
  inc hl
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),a
  ret

f32tof64_zero:
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  rra
  ld (bc),a
  ret

f32tof64_infnan:
  xor a
  ld (bc),a
  inc bc
  ld (bc),a
  inc bc
  ld a,e
  add a,a
  or h
  or l
  ld (bc),a
  inc bc
  or %11110000
  ld (bc),a
  inc bc
  ld a,d
  or %01111111
  ld (bc),a
  ret
#endif
