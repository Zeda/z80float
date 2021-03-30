#ifndef included_xsqrt
#define included_xsqrt
#include "mov.z80"
#include "routines/srl64.z80"
#include "sqrt/sqrt64.z80"
#include "constantsx.z80"

#define var_c xOP1   ;input
#define var_y var_c+4 ;  used for sqrt32
#define var_x xOP2   ;output
#define var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#define var_a xOP2   ;   2 bytes
#define var_z0 xOP2+8;used in sqr32

xsqrt:
;HL points to x
;BC points to the output
;computes x^.5, if x>=0
;speed: 388+mov8+mov10+sqrt64+{0,7+srlxOP1_mantissa}
;min: 5456cc
;max: 7432cc
;avg: 6498.542cc

  push hl
  push de
  push bc
  push af
  push ix
  push bc
  call +_
  ld hl,var_x
  pop de
  call mov8
  ld hl,(xOP1+8)
  ex de,hl
  ld (hl),e
  inc hl
  ld (hl),d
  pop ix
  pop af
  pop bc
  pop de
  pop hl
  ret
_:
  ld de,xOP1
  call mov10
  ex de,hl
  dec hl
  ld a,(hl)
  or a
  jp m,sqrtNAN
  ld d,a
  dec hl
  ld e,(hl)
  or e
  jp z,sqrt_special
  ld a,d
  add a,$40
  rra
  ld h,a
  ld a,e
  rra
  ld l,a
  ld (xOP1+8),hl
  call nc,srlxOP1_mantissa
  jp sqrt64   ;#include "../extended/sqrt/sqrt64.z80"
sqrt_special:
;special case: 0 -> 0, NaN -> NaN, +inf -> +inf, so output=input
  ld de,xOP1
  ld hl,var_x
  jp mov10
sqrtNAN:
  ld hl,xconst_NaN
  ld de,xOP1
  jp mov10
#undefine var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#undefine var_a xOP2   ;   2 bytes
#undefine var_c xOP2+8 ;input
#undefine var_y var_c+4 ;  used for sqrt32
#undefine var_z0 xOP2+16
#endif
