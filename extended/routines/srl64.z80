#ifndef included_srl64
#define included_srl64

srlxOP2:
  ld hl,xOP2+7
  jp srl64
srlxOP1_mantissa:
;182cc
  ld hl,xOP1+7
srl64:
;172cc
  srl (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl) \ dec hl
  rr (hl)
  ret
#endif
