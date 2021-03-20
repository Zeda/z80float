#ifndef included_div32
#define included_div32
#include "div/div32_16.z80"
#include "mul16.z80"

#define var_x xOP2   ;output
#define var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#define var_n xOP3
div32_32:
;228+{0,115}+2*div32_16+mul16
;min: 1982cc
;max: 2952cc
;avg: 2560.887cc
;HLDE/(var_x+4)
  ld bc,(var_x+6)
  call div32_16
  ld (var_b+2),de   ;top 16-bit digit
;Need to adjust the remainder
;(HL:00-DE*(var_x+4))
  push hl
  ld bc,(var_x+4)
  call mul16

  ;DEHL
  ld b,d
  ld c,e
  ex de,hl
  pop hl
  ;BCDE
  xor a
  sub e
  ld e,a
  ld a,0
  sbc a,d
  ld d,a
  sbc hl,bc
  jr nc,div32_32_final
_:
  ld bc,(var_b+2)
  dec bc
  ld (var_b+2),bc
  ld bc,(var_x+4)
  ex de,hl
  add hl,bc
  ld bc,(var_x+6)
  ex de,hl
  adc hl,bc
  jr nc,-_
  or a
div32_32_final:
;HLDE is the new remainder
  ld bc,(var_x+6)
  sbc hl,bc
  jr z,+_
  add hl,bc
  call div32_16
  ld (var_b),de   ;low 16-bits
  ret
_:
  dec hl
  ld (var_b),hl
  ret
#endif
