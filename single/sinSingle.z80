#ifndef included_sinSingle
#define included_sinSingle
#include "pushpop.z80"
#include "mulSingle.z80"
#include "addSingle.z80"
#include "subSingle.z80"
#include "rsubSingle.z80"
#include "cosSingle.z80"
#include "mod1Single.z80"
#include "constants.z80"

#define var_x scrap+11
#define var_y scrap+15
#define temp scrap+19
sinSingle:
;sine(-pi/4<=x<pi/4)
;y=x*x
;a1=2^-3 * 11184804/2^23
;a2=2^-7 * 8946604/2^23
;a3=2^-13 * 13408017/2^23
;x(1-y(a1-y(a2-y*a3)))
;
  call pushpop
  push bc
;Need to apply range reduction
; We want the input on [-pi/4,pi/4]
; First multiply by 1/(2pi)
  ld de,const_2pi_inv
  ld bc,var_x
  call mulSingle

;Now add .25
  ld h,b
  ld l,c
  ld de,const_p25
  call addSingle

;Now grab the xmod1
  call mod1Single

;Let's convert this to a cosine problem
  ld de,const_p5
  call rsubSingle
  jp cosSingle_stepin

sin_subroutine:
;Multiply by 2pi
  ld de,const_2pi
  call mulSingle

  ld d,h
  ld e,l
  ld bc,var_y
  call mulSingle
  ld h,b
  ld l,c
  ld de,sin_a3
  ld bc,temp
  call mulSingle
  ld hl,sin_a2
  ld d,b
  ld e,c
  call subSingle
  ld hl,var_y
  call mulSingle
  ld hl,sin_a1
  call subSingle
  ld hl,var_y
  call mulSingle
  ld hl,const_1
  call subSingle
  ld hl,var_x
  pop bc
  jp mulSingle

#undefine var_x
#undefine var_y
#undefine temp
#endif
