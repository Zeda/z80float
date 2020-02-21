#ifndef included_f24mul2
#define included_f24mul2

f24mul2:
;AHL * 2.0 ==> AHL
;Destroys B
;
  ld b,a
  ;check for special values
  and $7F
  jr nz,$+4
  ld a,b
  ret
  inc a
  ld a,b
  ret m
  inc a
  ret
#endif
