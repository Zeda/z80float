#ifndef included_f24div_pow2
#define included_f24div_pow2

f24div_pow2:
;AHL/2^B ==> AHL
  ld c,a
  and $7F
  sub b
  jr nc,$+4
  xor a
  ret
  ld a,c
  sub b
  ret
#endif
