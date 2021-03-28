#ifndef included_xsinh
#define included_xsinh
#include "pushpop.z80"
#include "xexp.z80"
#include "xinv.z80"
#include "xamean.z80"

#define hyper_0 xOP1+72
#define hyper_1 xOP1+82
xsinh:
  call pushpop
  push bc
  ld bc,hyper_0
  call xexp
  ld h,b
  ld l,c
  ld bc,hyper_1
  call xinv
  ld a,(hyper_1+9)
  xor 80h
  ld (hyper_1+9),a
  ld d,b
  ld e,c
  pop bc
  jp xamean

#undefine hyper_0
#undefine hyper_1
#endif
