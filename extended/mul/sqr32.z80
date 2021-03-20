#ifndef included_sqr32
#define included_sqr32
#include "mul16.z80"

#define var_c xOP1   ;input
#define var_y var_c+4 ;  used for sqrt32
#define var_x xOP2   ;output
#define var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#define var_a xOP2   ;   2 bytes
#define var_z0 xOP2+8;used in sqr32
sqr32:
;avg: 2057.39cc
;HLDE --> var_z0
  push hl
  ld b,d
  ld c,e
  call mul16  ; -> DEHL
  ld (var_z0),hl
  ld (var_z0+2),de
  pop de
  push bc
  ld b,d
  ld c,e
  call mul16
  ld (var_z0+4),hl
  ld (var_z0+6),de
  pop de
  call mul16
  xor a
  add hl,hl
  rl e
  rl d
  rla
  ld bc,(var_z0+2)
  add hl,bc
  ld (var_z0+2),hl
  ex de,hl
  ld bc,(var_z0+4)
  adc hl,bc
  ld (var_z0+4),hl
  ld hl,var_z0+6
  adc a,(hl)
  ld (hl),a
  ret nc
  inc hl
  inc (hl)
  ret
#undefine var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#undefine var_a xOP2   ;   2 bytes
#undefine var_c xOP2+8 ;input
#undefine var_y var_c+4 ;  used for sqrt32
#undefine var_z0 xOP2+16
#endif
