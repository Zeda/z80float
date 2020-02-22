#ifndef included_f24amean
#define included_f24amean

f24amean:
;(AHL+CDE) ==> AHL

;Make sure x+y won't overflow
;save A
  ld b,a
  and $7F
  jr z,f24amean_nooverflow
  cp $7E
  jr z,f24amean_overflow

  ld a,c
  and $7F
  jr z,f24amean_nooverflow
  cp $7E
  jr z,f24amean_overflow

f24amean_nooverflow:
  ld a,b
  call f24add
#ifdef included_f24div2
  jp f24div2
#else
#define included_f24div2
f24div2:
  ld b,a
  and $7F
  ld a,b
  ret z

  ld b,a
  and $7F
  inc a
  ld a,b
  ret m
  dec a
  ret
#endif

f24amean_overflow:
;need to decrement the exponents first
  ld a,b
  push de
  push bc
  call f24div2
  pop bc
  ex (sp),hl
  push af
  ld a,c
  call f24div2
  pop bc
  pop de
  ld c,b
  jp f24add

#endif
