#ifndef included_addmantissa0102
#define included_addmantissa0102
#include "routines/add64.z80"
#include "routines/rr64.z80"
#include "mul/xmul3.z80"

addmantissa0102:
  ld hl,xOP2
  ld de,xOP1
  call adc64
  ret nc
  ex de,hl
  call rr64
  ex de,hl
  call srl64
#if ((xOP1+8)>>8)==(xOP1>>8)
  ld l,(xOP1+8)&255
#else
  ld hl,xOP1+8
#endif
  inc (hl)
  ret nz
  inc_hl_opt(xOP1+8)
  ld a,(hl)
  inc (hl)
  xor (hl)
  ret p
  jp constmul_overflow
#endif
