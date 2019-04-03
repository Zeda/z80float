#ifndef included_div64
#define included_div64
#include "div/div64_32.z80"
#include "mul/mul32.z80"
#include "routines/add64.z80"
#include "routines/sub64.z80"

#define var_x xOP2   ;output
div64:
;var_n / var_x
;304+2*div64_32+mul32+sub64+{0,72+add64+{0,19+{0,19+{0,3
;304+2*div64_32+mul32+sub64+169.0607843
;2*div64_32+3128.7937843
;
;304+2*div64_32+mul32+sub64+{0,72+add64+{0,19+{0,19+{0,3
;min: 6683cc
;max: 11469cc
;avg: 9759.520cc
  call div64_32
  ld (var_q+4),ix
  ld (var_q+6),bc
;Need to adjust the remainder
  ld (var_n+6),hl
  ld (var_n+4),de
  ld hl,(var_x)
  ld de,(var_x+2)
  call mul32  ;DEHL * BCIX
  ;var_z0 holds the 64-bit result
  ;need var_n-z0_32
  ld hl,0
  ld (var_n),hl
  ld (var_n+2),hl
  ld de,var_n
  ld hl,z0_32
  call sub64
  jr nc,div64_end
div64_recarry:
  ld de,var_n
  ld hl,var_x
  call add64
  push af
  ld hl,var_q+4
  ld a,-1
  dec (hl) \ cp (hl) \ jr nz,+_
  inc hl \ dec (hl) \ cp (hl) \ jr nz,+_
  inc hl \ dec (hl) \ cp (hl) \ jr nz,+_
  inc hl \ dec (hl)
_:
  pop af
  jr nc,div64_recarry
div64_end:
  call div64_32
  ld (var_q),ix
  ld (var_q+2),bc
  ret
#endif
