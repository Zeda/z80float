#ifndef included_asinhSingle
#define included_asinhSingle
#include "pushpop.z80"
#include "mov4.z80"
#include "constants.z80"
#include "mulSingle.z80"
#include "addSingle.z80"
#include "sqrtSingle.z80"
#include "bgiSingle.z80"

#define var_a scrap+11
#define var_g var_a+4
#define var_b var_g+4
#define var_c var_b+4
#define var_x var_c+4
asinhSingle:
;return x/bgc((1+x*x)**.5,1.0)
;needs to be reduced to |x|>=1
  call pushpop
  push bc
  ld de,var_x
  call mov4
  ld de,var_x
  ld h,d
  ld l,e
  ld bc,var_a
  call mulSingle
  ld de,const_1
  ld h,b
  ld l,c
  call addSingle
  call sqrtSingle
  call bgiSingle
  ld de,var_x
  pop bc
  jp mulSingle
#endif
