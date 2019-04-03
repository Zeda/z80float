#ifndef included_xconst
#define included_xconst
#include "constantsx.z80"

xconsti:
    ex (sp),hl
    ld a,(hl)
    inc hl
    ex (sp),hl
xconst:
;A is the constant ID#
;returns nc if failed, c otherwise
;HL points to the constant
  cp (end_xconst-start_xconst)/10
  ret nc
  ;multiply A by 10
  ld l,a
  add a,a
  add a,a
  add a,l
  add a,a
  add a,start_xconst&255
  ld l,a
  ld h,start_xconst>>8
  ret nc
  inc h
  ret
#endif
