#ifndef included_xinv
#define included_xinv
#include "xdiv.z80"
#include "constantsx.z80"

#define var_q xOP1
#define var_x xOP2
#define var_n xOP3
xinv:
;speed: 66cc+xdiv
;663+{0,220+{0,6}}+{0,3}+div64+cmp64+mov8+2*mov10
;1141+{0,220+{0,6}}+{0,3}+div64+cmp64
;min: 1141+div64+cmp64
;     7887cc
;max: 1597+div64
;     13088cc
;avg: 1141+{0,220+{0,6}}+{0,3}+div64+cmp64
;     11058.151cc
  push de
  ld de,xconst_1
  ex de,hl
  call xdiv
  ex de,hl
  pop de
  ret

#endif
