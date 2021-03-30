#ifndef included_xOP1mul10
#define included_xOP1mul10
#include "mov.z80"
#include "routines/add64.z80"
xOP1mul10:
;Note! Does not check for special numbers! Does not check overflow!
  ld hl,xOP1
  ld de,xOP2
  call mov8
  ; ld hl,xOP1+8 ; useless thanks to the 8x LDI's just before...
  ld a,3
  add a,(hl)
  ld (hl),a
  jr nc,+_
  inc_hl_opt(xOP1+8)
  inc (hl)
_:
#if ((xOP2+7)>>8)==((xOP1+8)>>8)
  ld l,255&(xOP2+7)
#else
  ld hl,xOP2+7
#endif

  srl (hl) \ dec_hl_opt(xOP2+7)
  rr (hl) \ dec_hl_opt(xOP2+6)
  rr (hl) \ dec_hl_opt(xOP2+5)
  rr (hl) \ dec_hl_opt(xOP2+4)
  rr (hl) \ dec_hl_opt(xOP2+3)
  rr (hl) \ dec_hl_opt(xOP2+2)
  rr (hl) \ dec_hl_opt(xOP2+1)
  rr (hl)
#if ((xOP2+7)>>8)==(xOP2>>8)
  ld l,255&(xOP2+7)
#else
  ld hl,xOP2+7
#endif
  srl (hl) \ dec_hl_opt(xOP2+7)
  rr (hl) \ dec_hl_opt(xOP2+6)
  rr (hl) \ dec_hl_opt(xOP2+5)
  rr (hl) \ dec_hl_opt(xOP2+4)
  rr (hl) \ dec_hl_opt(xOP2+3)
  rr (hl) \ dec_hl_opt(xOP2+2)
  rr (hl) \ dec_hl_opt(xOP2+1)
  rr (hl)
  ld de,xOP1
  call adc64
  ret nc
#if ((xOP1+8)>>8)==(xOP2>>8)
  ld l,255&(xOP1+8)
#else
  ld hl,xOP1+8
#endif
  inc (hl)
  jr nz,+_
  inc l
  inc (hl)
_:
  ex de,hl
  rr (hl) \ dec_hl_opt(xOP1+7)
  rr (hl) \ dec_hl_opt(xOP1+6)
  rr (hl) \ dec_hl_opt(xOP1+5)
  rr (hl) \ dec_hl_opt(xOP1+4)
  rr (hl) \ dec_hl_opt(xOP1+3)
  rr (hl) \ dec_hl_opt(xOP1+2)
  rr (hl) \ dec_hl_opt(xOP1+1)
  rr (hl)
  ret
#endif
