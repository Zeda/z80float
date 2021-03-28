#ifndef included_tanSingle
#define included_tanSingle
#include "pushpop.z80"
#include "cosSingle.z80"
#include "sinSingle.z80"
#include "divSingle.z80"

#define var_x scrap+11
#define var_y scrap+15
#define temp scrap+19
#define var_z scrap+23
tanSingle:
  call pushpop
  push bc
  ;HL points to input
  ld bc,var_z
  ld d,b
  ld e,c
  call cosSingle
  ld bc,var_x
  call sinSingle
  ld h,b
  ld l,c
  pop bc
  jp divSingle
#undefine var_x
#undefine var_y
#undefine var_z
#undefine temp
#endif
