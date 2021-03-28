#ifndef included_xsin
#define included_xsin
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xadd.z80"
#include "xrsub.z80"
#include "xmod1.z80"
#include "xcos.z80"

#define sin_x xOP1+60
#define sin_y xOP1+70
#define temp xOP1+80

xsin:
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
  ld de,xconst_2pi_inv
  ld bc,sin_x
  call xmul

;Now add .25
  ld h,b
  ld l,c
  ld de,xconst_p25
  call xadd

;Now grab the xmod1
  call xmod1

;Let's convert this to a cosine problem
  ld de,xconst_p5
  call xrsub
  jp xcos_stepin

xsin_subroutine:
;Multiply by 2pi
  ld de,xconst_2pi
  ld b,h
  ld c,l
  call xmul

  ld d,h
  ld e,l
  ld bc,sin_y
  call xmul
  ld h,b
  ld l,c
  ld de,xsin_p7
  ld bc,temp
  call xmul
  ld hl,xsin_p6
  ld d,b
  ld e,c
  call xadd
  ld hl,sin_y
  call xmul
  ld hl,xsin_p5
  call xadd
  ld hl,sin_y
  call xmul

  ld hl,xsin_p4
  call xadd
  ld hl,sin_y
  call xmul

  ld hl,xsin_p3
  call xadd
  ld hl,sin_y
  call xmul

  ld hl,xsin_p2
  call xadd
  ld hl,sin_y
  call xmul

  ld hl,xsin_p1
  call xadd
  ld hl,sin_y
  call xmul


  ld hl,xsin_p0
  call xadd
  ld hl,sin_x
  pop bc
  jp xmul

xsin_p0:
.db $00,$00,$00,$00,$00,$00,$00,$80,$00,$40    ;0.9999999999999999999981204044115315796
xsin_p1:
.db $8E,$AA,$AA,$AA,$AA,$AA,$AA,$AA,$FD,$BF    ;-0.1666666666666666662812878964544520249
xsin_p2:
.db $96,$4C,$88,$88,$88,$88,$88,$88,$F9,$3F    ;.00833333333333332033458286248185347141
xsin_p3:
.db $37,$DF,$3F,$0C,$D0,$00,$0D,$D0,$F3,$BF    ;-.0001984126984125310632612418861238238148
xsin_p4:
.db $12,$C0,$D4,$84,$29,$1D,$EF,$B8,$ED,$3F    ;.000002755731921339040823259154579822644652
xsin_p5:
.db $B9,$1F,$70,$0F,$32,$29,$32,$D7,$E6,$BF    ;-.00000002505210473832886631551463640646870413
xsin_p6:
.db $80,$CC,$9B,$F1,$F1,$3A,$90,$B0,$DF,$3F    ;.0000000001605834763092742825428205943594730752
xsin_p7:
.db $D3,$82,$8D,$7D,$A3,$4B,$4C,$D5,$D7,$BF    ;-.000000000000757786825836494841305422527105351555

#undefine sin_x
#undefine sin_y
#undefine temp
#endif
