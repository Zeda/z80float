#ifndef included_acoshSingle
#define included_acoshSingle
#include "pushpop.z80"
#include "mov4.z80"
#include "constants.z80"
#include "mulSingle.z80"
#include "subSingle.z80"
#include "sqrtSingle.z80"
#include "bgiSingle.z80"

#define var_a scrap+11
#define var_g var_a+4
#define var_b var_g+4
#define var_c var_b+4
#define var_x var_c+4
acoshSingle:
;sqrt(x*x-1)*bgi(x,1)
  call pushpop
  push bc
  ld de,var_a
  call mov4
  ld de,var_a
  ld h,d
  ld l,e
  ld bc,var_x
  call mulSingle
  ld de,const_1
  ld h,b
  ld l,c
  call subSingle
  call sqrtSingle
  ld hl,var_a
  ld b,h
  ld c,l
  call bgiSingle
  ld de,var_x
  pop bc
  jp mulSingle
#undefine var_a
#undefine var_g
#undefine var_b
#undefine var_c
#undefine var_x
#endif
