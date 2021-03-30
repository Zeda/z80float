#ifndef included_bg2iSingle
#define included_bg2iSingle
#include "pushpop.z80"
#include "mov4.z80"
#include "addSingle.z80"
#include "mulSingle_p375.z80"
#include "ameanSingle.z80"
#include "geomeanSingle.z80"
#include "divSingle.z80"
#include "constants.z80"

;Uses 23 bytes
#define var_a scrap+11
#define var_g var_a+4
#define var_b var_g+4
;This algorithm is insired by the one outlined here:
;http://www.ams.org/journals/mcom/1972-26-118/S0025-5718-1972-0307438-2/S0025-5718-1972-0307438-2.pdf
;It offers quadratic convergence, instead of linear convergence for only a little more work each iteration.
;So only TWO iterations are needed for single precision instead of ten.
bg2iSingle:
;HL points to 'A'
;DE points to 'G'
;BC points to output.
;Computes the reciprocal of the Borchard-Gauss mean algorithm.
;The entire single-precision algorithm:
;   b=a*.03125
;   a=amean(a,g)
;   g=geomean(a,g)
;   a*=.375
;   a+=g
;   a+=b
;   return 1.40625/a
  call pushpop
  push bc
  push de
  ld de,var_a
  call mov4
  pop hl
  call mov4
;b=a*.03125
  ld hl,var_a
  call mov4
  ld a,(var_b+3)
  sub 5
  ld (var_b+3),a
  jr z,$+4
  jr nc,+_
  ;need to set var_b to zero
  ld hl,0
  ld (var_b+2),hl
_:
;a=amean(a,g)
  ld hl,var_a
  ld de,var_g
  ld b,h
  ld c,l
  call ameanSingle
;g=geomean(a,g)
  ld b,d
  ld c,e
  call geomeanSingle

;   a*=.375
  ld hl,var_a
  ld b,h
  ld c,l
  call mulSingle_p375

;a+=g
  ld hl,var_a
  ld b,h
  ld c,l
  call addSingle
;a+=b
  ld de,var_b
  call addSingle
  ex de,hl
  ld hl,const_1p40625
  pop bc
  jp divSingle
;return 1.40625/a

#undefine var_a
#undefine var_g
#undefine var_b
#endif
