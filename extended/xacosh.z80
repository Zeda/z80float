#ifndef included_xacosh
#define included_xacosh
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xsub.z80"
#include "xsqrt.z80"
#include "xbg.z80"

;sqrt(x^2-1)/BG(x,1)
#define var_x  xOP1+152
xacosh:
;log(x+sqrt(x^2-1))
  call pushpop
  push bc
  ld de,var_x-10
  call mov10
  ld hl,var_x-10
  ld d,h
  ld e,l
  ld bc,var_x-20
  call xmul
  ld h,b
  ld l,c
  ld de,xconst_1
  call xsub
  call xsqrt
  ld de,var_x-10
  call xadd
  pop bc
  jp xln




  ; push bc
  ; push hl
  ; ld d,h
  ; ld e,l
  ; ld bc,xOP1
  ; call xmul
  ; ld de,xconst_1
  ; ld h,b
  ; ld l,c
  ; ld bc,var_x
  ; call xsub
  ; ld h,b
  ; ld l,c
  ; call xsqrt
  ; pop hl
  ; ld bc,xOP1
  ; call xbg
  ; ld h,b
  ; ld l,c
  ; ld de,var_x
  ; pop bc
  ; jp xmul
#endif
