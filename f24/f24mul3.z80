#ifndef included_f24mul3
#define included_f24mul3

f24mul3:
;AHL*3 ==> AHL
;0*3 ==> 0
  ld c,a
  add a,a
  ld a,c
  ret z

;inf*3 ==> inf, NaN*3 ==> NaN
  ld c,a
  and $7F
  inc a
  ld a,c
  ret m

  inc c
  ld a,c
  add a,a
  add a,2
  jr nz,$+6
  ld hl,0
  ret

  ld d,h
  ld e,l
  scf
  rr h
  rr l
  add hl,de
  ld a,c
  ret nc
  srl h
  rr l
  inc a
  ret

#endif
