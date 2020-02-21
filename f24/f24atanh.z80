#ifndef included_f24atanh
#define included_f24atanh

#include "f24sub.z80"
#include "f24div.z80"
#include "f24log.z80"

f24atanh:
;atanh(AHL) ==> AHL
;Computed as log((1+x)/(1-x))/2
;

;save x
  push hl
  push af

;1-x
  ld c,$3F \ ld de,0
  call f24rsub
  pop bc
  ex (sp),hl
  push af
  ld a,b

;1+x
  ld c,$3F \ ld de,0
  call f24add

;(1+x)/(1-x)
  pop bc
  pop de
  ld c,b
  call f24div

;log((1+x)/(1-x))/2
  call f24log
  jp f24div2

#endif
