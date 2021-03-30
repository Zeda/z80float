#ifndef included_atanhSingle
#define included_atanhSingle
#include "pushpop.z80"
#include "mov4.z80"
#include "constants.z80"
#include "mulSingle.z80"
#include "rsubSingle.z80"
#include "sqrtSingle.z80"
#include "bgiSingle.z80"

#define var_a scrap+11
#define var_g var_a+4
#define var_b var_g+4
#define var_c var_b+4
#define var_x var_c+4
atanhSingle:
;return x*bgi(1,sqrt(1-x*x))
  call pushpop
  push bc
  ld de,var_x
  call mov4
  ld de,var_x
  ld h,d
  ld l,e
  ld bc,var_g
  call mulSingle
  ld de,const_1
  ld h,b
  ld l,c
  call rsubSingle
  call sqrtSingle
  ex de,hl
  call bgiSingle
  ld hl,var_x
  pop bc
  jp mulSingle
#endif
