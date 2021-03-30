#ifndef included_xln
#define included_xln
#include "pushpop.z80"
#include "mov.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xamean.z80"
#include "xsub.z80"
#include "xbg.z80"
#include "../conversion/i16tox.z80"


;NOTE! Doesn't yet check for special numbers!
;Not accurate on x<1, or some large x.
;
;We are going to compute ln(x) using the B-G algo.
;(x-1)/BG(.5(1+x), sqrt(x))
#define var_x  xOP1+152
xln:
  call pushpop
  push bc
  ld de,var_x
  call mov10

;ln(-x) == NaN
  ld hl,(var_x+8)
  ld a,h
  add a,a
  jr c,xln_return_NaN

;ln(0), ln(NaN), ln(inf)
  or l
  jr z,xln_return_special

;save the exponent
  push hl

;set exponent to 0
  ld hl,$4000
  ld (var_x+8),hl

  ld hl,var_x
  ld bc,xOP5
  call xsqrt
  ld de,xconst_1
  ld bc,xOP4
  call xamean
  ld b,h
  ld c,l
  call xsub
  ld hl,xOP4
  ld de,xOP5
  ld b,h
  ld c,l
  call xbg
  ld hl,var_x
  ld d,b
  ld e,c
  ld b,h
  ld c,l
  call xmul

  pop hl
  ld a,h
  sub $40
  ld h,a
  ;need to do HL*ln(2)+var_x ==> BC
  ld bc,xOP1
  call i16tox
  ld h,b
  ld l,c
  ld de,xconst_ln_2
  call xmul
  ld de,var_x
  pop bc
  jp xadd
xln_return_special:
;ln(0) == -inf
;ln(inf) == inf; ln(NaN) == NaN
  ld a,(var_x+7)
  and $C0
  jr nz,$+7
  ld hl,xconst_nINF
  jr +_
  jp m,xln_return_inf
xln_return_NaN:
  ld hl,xconst_NaN
  jr +_
xln_return_inf:
  ld hl,xconst_inf
_:
  pop de
  jp mov10
#endif
