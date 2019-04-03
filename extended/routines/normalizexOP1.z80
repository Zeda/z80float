#ifndef included_normalizexOP1
#define included_normalizexOP1
normalizexOP1:
  ld a,(xOP1+7)
  add a,a
  ret c
_:
  ld hl,xOP1
  sla (hl) \ inc_hl_opt(xOP1)
  rl (hl) \ inc_hl_opt(xOP1+1)
  rl (hl) \ inc_hl_opt(xOP1+2)
  rl (hl) \ inc_hl_opt(xOP1+3)
  rl (hl) \ inc_hl_opt(xOP1+4)
  rl (hl) \ inc_hl_opt(xOP1+5)
  rl (hl) \ inc_hl_opt(xOP1+6)
  rl (hl)
  ld hl,(xOP1+8)
  dec hl
  ld (xOP1+8),hl
  jp p,-_
  ret
#endif
