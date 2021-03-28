#ifndef included_xcos
#define included_xcos
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xadd.z80"
#include "xsub.z80"
#include "xrsub.z80"
#include "xmod1.z80"
#include "xsin.z80"

#define cos_x xOP1+60
#define cos_y xOP1+70
#define temp xOP1+80

xcos:
;cos(-pi/4<=x<pi/4)
;y=x*x
;1-y(.49999887-y(.041655882-y.0013591743))
;1-y(a1-y(a2-y*a3))
  call pushpop
  push bc
;Need to apply range reduction
; We want the input on [-pi/4,pi/4]
; First multiply by 1/(2pi)
  ld de,xconst_2pi_inv
  ld bc,cos_x
  call xmul

; Add .5
  ld h,b
  ld l,c
  ld de,xconst_p5
  call xadd

;Now grab mod 1
  call xmod1

;subtract off the .5
  call xsub
  jr xcos_stepin
xcos_readjust:
  push bc
  ld bc,cos_x
xcos_stepin:
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
  ld hl,cos_x+9
  res 7,(hl)

;Check if the exponent is -2 or more. If so, return -cos(x-pi)
  dec hl
  ld a,(hl)
  ld h,b
  ld l,c
  sub $FE
  jr c,+_
  ld de,xconst_p5
  call xsub
;We don't want to infinite loop if the result is .25-.5 = -.25 !
  ld a,(cos_x+8)
  sub $FE
  jr nz,$+9
  ld a,80h
  ld (cos_x+8),a
  jr +_
  pop bc
  call xcos_readjust
  ld h,b
  ld a,9
  add a,c
  ld l,a
  jr nc,$+3
  inc h
  ld a,(hl)
  xor $80
  ld (hl),a
  ret
_:
;Check if the exponent is -3. If so, return sin(pi/2-x)
  inc a
  jr nz,+_
  ld de,xconst_p25
  call xrsub
  jp xsin_subroutine
_:
  ld de,xconst_2pi
  ld b,h
  ld c,l
  call xmul

  ld d,h
  ld e,l
  ld bc,cos_y
  call xmul
  ld h,b
  ld l,c
  ld de,xcos_p7
  ld bc,temp
  call xmul
  ld hl,xcos_p6
  ld d,b
  ld e,c
  call xadd
  ld hl,cos_y
  call xmul
  ld hl,xcos_p5
  call xadd
  ld hl,cos_y
  call xmul

  ld hl,xcos_p4
  call xadd
  ld hl,cos_y
  call xmul

  ld hl,xcos_p3
  call xadd
  ld hl,cos_y
  call xmul

  ld hl,xcos_p2
  call xadd
  ld hl,cos_y
  call xmul

  ld hl,xcos_p1
  call xadd
  ld hl,cos_y
  call xmul

  ld hl,xcos_p0
  pop bc
  jp xadd
#undefine cos_x
#undefine cos_y
#undefine temp

xcos_p0:
.db $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$3F    ;0.999999999999999999964159204834411193
xcos_p1:
.db $F8,$FE,$FF,$FF,$FF,$FF,$FF,$FF,$FE,$BF    ;-0.4999999999999999928435986970121455617
xcos_p2:
.db $1B,$9A,$A9,$AA,$AA,$AA,$AA,$AA,$FB,$3F    ;.0416666666666664302574180075687333186
xcos_p3:
.db $8C,$65,$B1,$09,$B6,$60,$0B,$B6,$F6,$BF    ;-.001388888888885896043735590722592072382
xcos_p4:
.db $CB,$EF,$B3,$6B,$CD,$00,$0D,$D0,$F0,$3F    ;.00002480158728289946428496138594581111543
xcos_p5:
.db $B4,$48,$CE,$10,$7F,$7B,$F2,$93,$EA,$BF    ;-.000000275573128656963777686502398712343692
xcos_p6:
.db $C8,$97,$56,$CF,$3C,$AA,$74,$8F,$E3,$3F    ;.000000002087555514571344400405482331559490482
xcos_p7:
.db $90,$5C,$F1,$0F,$F8,$6A,$B5,$C7,$DB,$BF    ;-.00000000001135212320760413752073800267975510526
#endif
