#ifndef included_cosSingle
#define included_cosSingle
#include "pushpop.z80"
#include "mulSingle.z80"
#include "addSingle.z80"
#include "subSingle.z80"
#include "rsubSingle.z80"
#include "sinSingle.z80"
#include "mod1Single.z80"
#include "constants.z80"

#define var_x scrap+11
#define var_y scrap+15
#define temp scrap+19
cosSingle:
;cos(-pi/4<=x<pi/4)
;y=x*x
;1-y(.49999887-y(.041655882-y.0013591743))
;1-y(a1-y(a2-y*a3))

  call pushpop
  push bc
;Need to apply range reduction
; We want the input on [-pi/4,pi/4]
; First multiply by 1/(2pi)
  ld de,const_2pi_inv
  ld bc,var_x
  call mulSingle

; Add .5
  ld h,b
  ld l,c
  ld de,const_p5
  call addSingle

;Now grab the xmod1
  call mod1Single

;subtract off the .5
  call subSingle
  jr cosSingle_stepin
cosSingle_readjust:
  push bc
  ld bc,var_x
cosSingle_stepin:
;now x is on [-.5,.5], but we need to evaluate cos(x*2pi) with x on [-.125,.125]
;We need to employ some identities
;  cos(-x)=cos(x)
;    make x positive
;  cos(x-pi)=-cos(x)
;   if our x is now on [.25,.5], then subtract .5 and take the absolute value,
;   and return the negative result.
;  cos(pi/2-x)=sin(x)
;    if our x is now on [.125,.25], subtract .25 and feed it to the sine routine.

; maxe x positive
  ;call absSingle
  ld hl,var_x+2
  res 7,(hl)

;Check if the exponent is -2 or more. If so, return -cos(x-pi)
  inc hl
  ld a,(hl)
  ld h,b
  ld l,c
  sub $7E
  jr c,+_
  ld de,const_p5
  call subSingle
;We don't want to infinite loop if the result is .25-.5 = -.25 !
  ld a,(var_x+3)
  sub $7E
  jr nz,$+7
  ld (var_x+2),a
  jr +_
  pop bc
  call cosSingle_readjust
  ld h,b
  ld l,c
  inc hl
  inc hl
  ld a,(hl)
  xor $80
  ld (hl),a
  ret
_:
;Check if the exponent is -3. If so, return sin(pi/2-x)
  inc a
  jr nz,+_
  ld de,const_p25
  call rsubSingle
  jp sin_subroutine
_:
  ld de,const_2pi
  ld b,h
  ld c,l
  call mulSingle

  ld d,h
  ld e,l
  ld bc,var_y
  call mulSingle
  ld h,b
  ld l,c
  ld de,cos_a3
  ld bc,temp
  call mulSingle
  ld hl,cos_a2
  ld d,b
  ld e,c
  call subSingle
  ld hl,var_y
  call mulSingle
  ld hl,cos_a1
  call subSingle
  ld hl,var_y
  call mulSingle
  ld hl,const_1
  pop bc
  jp subSingle
#undefine var_x
#undefine var_y
#undefine temp
#endif
