#ifndef included_xdiv2
#define included_xdiv2

xdiv2:
  call pushpop
  ld d,b
  ld e,c
  call mov10
  ex de,hl
  dec hl
  ld a,(hl)
  dec hl
  and $7F
  or (hl)
  ret z   ;0/2->0, inf/2->inf, NaN/2->NaN,
  ld a,(hl)
  sub 1
  ld (hl),a
  ret nc
  inc hl
  dec (hl)
  ret
#endif
