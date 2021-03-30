#ifndef included_xbg
#define included_xbg
#include "pushpop.z80"
#include "mov.z80"
#include "mul/xmul11.z80"
#include "mul/xmul13.z80"
#include "mul/xmul31.z80"
#include "mul/xmul7.z80"
#include "mul/xmul17.z80"
#include "mul/xmul15.z80"
#include "mul/xmul5.z80"

#include "xsub.z80"
#include "xdiv.z80"
#include "xamean.z80"
#include "xgeomean.z80"

#define var_a xOP3+42
#define var_g var_a+10
#define var_a0 var_a+20
#define var_a1 var_a+30
#define var_a2 var_a+40
#define var_a3 var_a+50
#define var_a4 var_a+60
#define var_a5 var_a+70

;This is an accelerated Borchardt-Gauss algorithm
;It is used in computing inverse trancendentals and the like.
;This implmenetation actually computes 1/BG(a,g) since this is useful.
;
;Basic outline:
;  a0 is the initial a
;  g0 is the initial g
;  compute a_(n+1) = (a_n+g_n)/2
;  compute a_(g+1) = (a_(n+1)+g_n)/2
;
;a1<<=2
;a2<<=6
;a3<<=12
;a4<<=20
;a5<<=30
;a6<<=42
;a3*=85
;a1+=a5
;a1*=105
;a2+=a4
;a2*=21
;a2-=a3
;a2*=341
;a2-=a1
;a2*=13
;a2+=a0
;a2+=a6
;return 3028466566125/a2
;
xbg:
;1510+9*mov10+6*xamean+5*xgeomean+4*xadd+2*xsub+xdiv+xmul3+xmul5+2*xmul7+xmul11+xmul13+xmul15+xmul17+xmul31
;+{0,9}*(if pow>255-{2,6,12,20,30,42} choose 9*{1,2,3,4,5,6})
;min: 13329+5*xgeomean+12*xadd+xmul3+xmul5+2*xmul7+xmul11+xmul13+xmul15+xmul17+xmul31
;max: 18584+5*xgeomean+12*xadd+xmul3+xmul5+2*xmul7+xmul11+xmul13+xmul15+xmul17+xmul31
;avg: 99383.979+12*xadd+xmul3+xmul5+2*xmul7+xmul11+xmul13+xmul15+xmul17+xmul31
  push hl
  push de
  push bc
  push af
  push bc
  call +_
  pop de
  ld hl,var_a
  call mov10
  pop af
  pop bc
  pop de
  pop hl
  ret
_:
  push de
  ld de,var_a
  call mov10
  pop hl
  call mov10
	ld hl,(var_a+8)
	ld de,(var_g+8)
	ld a,h
	or d
  jp m,bg_NaN
	ld a,h \ or l \ jp z,casebg
	ld a,d \ or e \ jp z,casebg2
  ld hl,var_a
  ld de,var_a0
  call mov10

  ld de,var_a \ ld b,d \ ld c,e \ call xamean
  ld b,h \ ld c,l \ call xgeomean
  ld hl,var_a1 \ ex de,hl \ call mov10

  ld de,var_a \ ld b,d \ ld c,e \ call xamean
  ld b,h \ ld c,l \ call xgeomean
  ld hl,var_a2 \ ex de,hl \ call mov10

  ld de,var_a \ ld b,d \ ld c,e \ call xamean
  ld b,h \ ld c,l \ call xgeomean
  ld hl,var_a3 \ ex de,hl \ call mov10

  ld de,var_a \ ld b,d \ ld c,e \ call xamean
  ld b,h \ ld c,l \ call xgeomean
  ld hl,var_a4 \ ex de,hl \ call mov10

  ld de,var_a \ ld b,d \ ld c,e \ call xamean
  ld b,h \ ld c,l \ call xgeomean
  ld hl,var_a5 \ ex de,hl \ call mov10

  ld de,var_a \ ld b,d \ ld c,e \ call xamean   ;a7

;Now we are going to adjust the exponents
  ld hl,(var_a1+8)
  ld a,l
  add a,2
  ld l,a
  jr nc,+_
  inc h
  jp m,bg_Zero
_:
  ld (var_a1+8),hl
  ld hl,(var_a2+8)
  ld a,l
  add a,6
  ld l,a
  jr nc,+_
  inc h
  jp m,bg_Zero
_:
  ld (var_a2+8),hl
  ld hl,(var_a3+8)
  ld a,l
  add a,12
  ld l,a
  jr nc,+_
  inc h
  jp m,bg_Zero
_:
  ld (var_a3+8),hl
  ld hl,(var_a4+8)
  ld a,l
  add a,20
  ld l,a
  jr nc,+_
  inc h
  jp m,bg_Zero
_:
  ld (var_a4+8),hl
  ld hl,(var_a5+8)
  ld a,l
  add a,30
  ld l,a
  jr nc,+_
  inc h
  jp m,bg_Zero
_:
  ld (var_a5+8),hl
  ld hl,(var_a+8)
  ld a,l
  add a,42
  ld l,a
  jr nc,+_
  inc h
  jp m,bg_Zero
_:
  ld (var_a+8),hl
;NOTE: I have verified that this is working up to here
;Accuracy is lost in the bottom two bits by the time a6 is computed.
;Next, multiply a3 by 85
  ld hl,var_a3
  ld b,h
  ld c,l
  call xmul5
  call xmul17

  ld hl,var_a1
  ld de,var_a5
  ld b,h
  ld c,l
  call xadd
  call xmul15
  call xmul7

  ld hl,var_a2
  ld de,var_a4
  ld b,h
  ld c,l
  call xadd
  call xmul3
  call xmul7

  ld de,var_a3
  call xsub
  call xmul11
  call xmul31

  ld de,var_a1
  call xsub
  call xmul13

  ld de,var_a0
  call xadd
  ld h,b
  ld l,c
  ld de,var_a
  ld b,d
  ld c,e
  call xadd
  ld hl,xconst_3028466566125
  jp xdiv
casebg:
;1/bg(0,x)    -> is actually permissable
;1/bg(inf,x)  -> 0
;1/bg(inf,inf)-> 0
;1/bg(0,inf)  -> 0 *** Not NaN, even though bg(inf,0)==NaN
;1/bg(0,0)    -> NaN
;1/bg(NaN,*)  -> NaN
;1/bg(inf,NaN)-> NaN
;1/bg(inf,0)  -> NaN
;1/bg(0,NaN)  -> NaN

  ret
casebg2:
;1/bg(x,NaN)  -> NaN
;1/bg(x,0)    -> NaN
;1/bg(x,inf)  -> 0
  ld a,(var_g+7)
  add a,a
  jr nc,bg_NaN
  add a,a
  jr nc,bg_NaN
bg_Zero:
  xor a
  ld h,a
  ld l,a
  ld (xOP1+8),hl
  ld (xOP1+7),a
  ret
bg_NaN:
  ld hl,0
  ld (xOP1+8),hl
  ld a,$40
  ld (xOP1+7),a
  ret
#undefine var_a
#undefine var_g
#undefine var_a0
#undefine var_a1
#undefine var_a2
#undefine var_a3
#undefine var_a4
#undefine var_a5
#endif
