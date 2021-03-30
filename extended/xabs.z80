#ifndef included_xabs
#define included_xabs
#include "pushpop.z80"
#include "mov.z80"

xabs:
  call pushpop
  ld d,b
  ld e,c
  call mov9
  ld a,(hl)
  and $7F
  ld (de),a
  ret
#endif
