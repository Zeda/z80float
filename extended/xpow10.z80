#ifndef included_xpow10
#define included_xpow10
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xpow2.z80"

#define xexp_x xOP3+42
xpow10:
  call pushpop
  push bc
  ld de,xconst_lg_10
  ld bc,xexp_x
  call xmul
  ld hl,xexp_x
  pop bc
  jp xpow2
#undefine xexp_x
#endif
