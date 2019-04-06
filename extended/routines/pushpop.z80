#ifndef included_pushpop
#define included_pushpop
#ifdef SMC
pushpop:
;(used to be) 26 bytes, adds 118cc to the traditional routine
  ld (pushpopSaveHL+1),hl
  ex (sp),hl
  ld (pushpopBackJP+1),hl
  push de
  push bc
  push af
  ld hl,pushpopret
  push hl
pushpopSaveHL:
  ld hl,0
pushpopBackJP
  jp 0
#else
pushpop:
;26 bytes, adds 118cc to the traditional routine
  ex (sp),hl
  push de
  push bc
  push af
  push hl
  ld hl,pushpopret
  ex (sp),hl
  push hl
  push af
  ld hl,12
  add hl,sp
  ld a,(hl)
  inc hl
  ld h,(hl)
  ld l,a
  pop af
  ret
#endif
pushpopret:
  pop af
  pop bc
  pop de
  pop hl
  ret
#endif
