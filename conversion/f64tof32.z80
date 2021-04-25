#ifndef included_f64tof32
#define included_f64tof32

#include "routines/rl64.z80"
#include "mov.z80"
#include "pushpop.z80"

f64tof32:
;Inputs:
;   HL points to the input double-precision float
;   BC points to where to output the result
;Outputs:
;   The double-precision float (binary64) is converted to an extended-precision
;   float at BC.
;
  call pushpop
f64tof32_nopush:
; we don't need the bottom 3 bytes except if we need to distinguish between inf
; and NaN.
  push bc     ;save the pointer to the output
  ld a,(hl)
  inc hl
  or (hl)
  inc hl
  or (hl)
  inc hl
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld c,(hl)
  inc hl
  ld b,(hl)
  inc hl
  ld h,(hl)
  ld l,a    ;save the OR of the bottom 3 bytes
;HBCDE is the top 5 bytes of the f64 float
  ld a,h
  add a,a
  jr z,f64tof32_check_0
  add a,2
  jr nz,f64tof32_continue
f64tof32_check_infnan:
  ld a,b
  add a,16
  jr nc,f64tof32_continue
f64tof32_infnan:
  ld a,b
  and %00001111
  or c
  or d
  or e
  or l
  ld d,h
  pop hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  or %10000000
  ld (hl),a
  inc hl
  ld a,d
  or %01111111
  ld (hl),a
  ret
f64tof32_check_0:
  ld a,b
  and %11110000
  jr z,f64tof32_zero
f64tof32_continue:
; We need to scale down the exponent, subtract 1023 and add 127, net -896
  ld a,h
  add a,a
  rrca
  sub 56
  jr c,f64tof32_zero_setA
  cp 16
  jr nc,f64tof32_inf1
  ex de,hl
;DBCHL
  add hl,hl
  rl c
  rl b
  rla

  add hl,hl
  rl c
  rl b
  rla

  add hl,hl
  rl c
  rl b
  rla

  xor d
  and %01111111
  xor d
  ;ABCHL
  ; round befoe writing out
  sla l
  jr nc,f64tof32_rounded
  inc h
  jr nz,f64tof32_rounded
  inc c
  jr nz,f64tof32_rounded
  inc b
  jr nz,f64tof32_rounded
  inc a
  jr z,f64tof32_inf
f64tof32_rounded:
  ld d,h
  pop hl
  ld (hl),d
  inc hl
  ld (hl),c
  inc hl
  ld (hl),b
  inc hl
  ld (hl),a
  ret

f64tof32_zero_setA:
  xor a
f64tof32_zero:
  ld d,h
  pop hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
  ld a,d
  and %10000000
  ld (hl),a
  ret
f64tof32_inf1:
  ld a,h
f64tof32_inf:
  pop hl
  ld (hl),0
  inc hl
  ld (hl),0
  inc hl
  ld (hl),80h
  inc hl
  or %01111111
  ld (hl),a
#endif
