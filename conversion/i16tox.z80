#ifndef included_i16tox
#define included_i16tox

i16tox:
; Converts the 16-bit signed integer in HL to an extended precision float at BC
;so extended-precision routines expect variables left unchanged, we'll pushpop
  call pushpop
  ex de,hl
  ld h,b
  ld l,c
  xor a
  ld b,6
_:
  ld (hl),a
  inc hl
  djnz -_
  or d
  or e
  jr nz,+_
  ld b,4
  ld (hl),a
  inc hl
  djnz $-2
  ret
_:

;HL points to where the bottom byte should be written
;DE is the value to convert

;set up the exponent
  ld bc,$400E

;get the sign
  ld a,d
  sla e
  adc a,a
  jr nc,+_
  ld b,$C0    ;it is negative
  ld d,a
  xor a
  sub e
  ld e,a
  sbc a,a
  sub d
_:
  jp m,i16tox_norm_done
i16tox_norm_loop:
  dec c
  sla e
  adc a,a
  jp p,i16tox_norm_loop
i16tox_norm_done:
  ld (hl),e
  inc hl
  ld (hl),a
  inc hl
  ld (hl),c
  inc hl
  ld (hl),b
  ret
#endif
