#ifndef included_f24logy
#define included_f24logy

#include "f24log.z80"
#include "f24div.z80"

f24logy:
;log_y(x) ==> AHL

;save x
  push hl
  push af

;compute the log of y
  ex de,hl
  ld a,c
  call f24log
;save log(y) and pop x
  pop bc
  ex (sp),hl
  push af
  ld a,b

;compute log x
  call f24log

;log(x)/log(y)
  pop bc
  pop de
  ld c,b
  jp f24div
#endif
