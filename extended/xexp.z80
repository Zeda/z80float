#ifndef included_xexp
#define included_xexp
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xpow2.z80"

#define xexp_x xOP3+42
xexp:
  call pushpop
  push bc
  ld de,xconst_lg_e
  ld bc,xexp_x
  call xmul
  ld hl,xexp_x
  pop bc
  jp xpow2
#endif
