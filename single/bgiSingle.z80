#ifndef included_bgSingle
#define included_bgSingle
#include "pushpop.z80"
#include "mov4.z80"
#include "addSingle.z80"
#include "mulSingle_p34375.z80"
#include "ameanSingle.z80"
#include "subSingle.z80"
#include "divSingle.z80"
#include "geomeanSingle.z80"
#include "constants.z80"
#include "mulSingle_p041015625.z80"

#define var_a scrap+11
#define var_g var_a+4
#define var_b var_g+4
#define var_c var_b+4

bgiSingle:
;Computes 1/BG(a,g)
;Inputs:
;  HL points to `a`
;  DE points to `g`
;  BC is where to write the result
;
;The algorithm
;  b=a/2048
;  a=.5*(a+g)
;  c=21*a/512
;  c-=b
;  g=sqrt(a*g)
;  a=.5*(a+g)
;  g=sqrt(a*g)
;  a*=11/32
;  a+=c
;  a+=g
;  return 1.38427734375/a
;
  call pushpop
  push bc
  push de
  ld de,var_a
  call mov4
  pop hl
  call mov4
;b=a/2048
  ld hl,var_a
  call mov4
  ld a,(var_b+3)
  sub 11
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
;  c=21*a/512
  ld hl,var_a
  ld bc,var_c
  call mulSingle_p041015625
;  c-=b
  ld h,b
  ld l,c
  ld de,var_b
  call subSingle
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
;  a*=11/32
  ld b,h
  ld c,l
  call mulSingle_p34375
;  a+=c
  ld de,var_c
  call addSingle
;  a+=g
  ld de,var_g
  call addSingle
;  return 1.38427734375/a
  ex de,hl
  ld hl,const_1p38427734375
  pop bc
  jp divSingle
const_1p38427734375: .db $00,$30,$31,$80  ;1.38427734375
#undefine var_a
#undefine var_g
#undefine var_b
#undefine var_c
#endif
