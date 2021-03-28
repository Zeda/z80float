#ifndef included_f32cmp
#define included_f32cmp
#include "pushpop.z80"
#include "f32sub.z80"

f32cmp:
;   HL >= DE ==> nc
;   HL < DE ==>  c
;   HL == DE ==> z (and nc)
;
;Note:
;   This allows some wiggle room in the bottom two bits. For example, if the two
;   exponents are the same and the two significands differ by at most 3, they are
;   considered equal.
;
;Note:
;   NaN is a special case. This routine returns that NaN<x for all x.
;   This gives the weird property NaN<NaN, and when sorting, NaN will be the
;   smallest element.
;

;check for inf and NaN
  push bc
  push hl
  push de
  inc hl
  inc hl
  ld a,(hl)
  add a,a
  inc hl
  ld a,h
  rla
  dec hl
  dec hl
  dec hl
  push af ;save the exponent
  ld bc,scrap
  call f32sub
  ld a,(scrap+2)
  add a,a
  ld a,(scrap+3)
  adc a,a
  pop bc
  pop de
  pop hl
  jr z,f32cmp_equal
  inc a
  jr nz,+_
  ; return NaN, possibly
  ld bc,(scrap)
  ld a,(scrap+2)
  add a,a
  or b
  or c
  jr z,f32cmp_notequal
  ld a,-1
  add a,a
  pop bc
  ret
_:
  sub b
  add a,2
  jr c,f32cmp_equal
f32cmp_notequal:
  pop bc
;now the sign bit indicates the output carry flag
  ld a,(scrap+3)
  or $7F    ;want to make sure the result is non-zero :)
  add a,a
  ret

f32cmp_equal:
  pop bc
  xor a
  ret
#endif
