#ifndef included_randinit
#define included_randinit

randinit:
; need to make sure seed1 is non-zero
  ld hl,seed1
  ld a,(hl)
  inc hl
  or (hl)
  inc hl
  or (hl)
  inc hl
  or (hl)
  ret nz
  dec (hl)
  ret
#endif
