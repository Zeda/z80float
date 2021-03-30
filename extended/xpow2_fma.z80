#ifndef included_xpow2
#define included_xpow2
#include "pushpop.z80"
#include "mov.z80"
#include "routines/sla64.z80"
#include "routines/normalizexOP1.z80"
#include "constantsx.z80"
#include "xfma.z80"

;This is just the same algorithm as the other pow2 routine, but using the FMA routine.
;It's three-bytes larger, probably slower, and isn't giving better accuracy, so not worth it.

#define xexp_x xOP3+42
;use range reduction to get x on [0,1]
;Then use the formula:
;2^x ~ 1+x(p1+x(p2+...+x(p11+x*p12)...))
xpow2:
  call pushpop
  push bc
  ld de,xOP1
  call mov10
  ld hl,(xOP1+8)
  res 7,h
  ld a,h
  or l
  jp z,caseexp
  ;If HL<3FF3 or HL>=400E, then magnitudes are too high
  ld bc,-$3EF3
  add hl,bc
  dec h
  jp nz,exp_too_big
  ld a,l
  cp 27
  jp nc,exp_too_big
;Now we know the exponent isn't too big
;
;Range Reduction phase
;e=int(x+.5)
;x-=e
;now we compute 2^e*2^x, where e is an integer
  ld de,0
  sub 13
  inc a
  jr c,xexp_ipart0
  ld b,a
  ;now we need to shift bits in from the mantissa!
_:
  call sla64_xOP1
  rl e \ rl d
  djnz -_
  ld a,(xOP1+9)
  add a,a
  ld hl,$3FFF
  jr nc,+_
  xor a \ sub e \ ld e,a
  sbc a,a \ sub d \ ld d,a
  ld h,$BF
_:
  ld (xOP1+8),hl
  call normalizexOP1
xexp_ipart0:
;!!!! Future Zeda, investigate! I think this should actually be fine on (-1,1) :O
;!!!! If not, we'll need to check if the input is negative, add 1, decrement DE
  push de
  ld hl,xOP1
  ld de,xexp_x
  call mov10

  ld hl,xOP1 \ ld b,h \ ld c,l \ ld de,xexp_p12 \ ld ix,xexp_p11 \ call xfma
  ld de,xexp_x \ ld ix,xexp_p10 \ call xfma
  ld ix,xexp_p9 \ call xfma
  ld ix,xexp_p8 \ call xfma
  ld ix,xexp_p7 \ call xfma
  ld ix,xexp_p6 \ call xfma
  ld ix,xexp_p5\ call xfma
  ld ix,xexp_p4 \ call xfma
  ld ix,xexp_p3 \ call xfma
  ld ix,xexp_p2 \ call xfma
  ld ix,xexp_p1 \ call xfma
  ld ix,xconst_1 \ call xfma

  pop de
  ;now I need to add DE as a signed integer to the exponent
  ld hl,(xOP1+8)
  add hl,de
  ld (xOP1+8),hl
  pop de
  ld h,b
  ld l,c
  jp mov10
caseexp:
  pop de
  ret
exp_too_big:
  pop de
  ret
xexp_p1:
xexp_p2 = xexp_p1+10
xexp_p3 = xexp_p1+20
xexp_p4 = xexp_p1+30
xexp_p5 = xexp_p1+40
xexp_p6 = xexp_p1+50
xexp_p7 = xexp_p1+60
xexp_p8 = xexp_p1+70
xexp_p9 = xexp_p1+80
xexp_p10= xexp_p1+90
xexp_p11= xexp_p1+100
xexp_p12= xexp_p1+110
.db $A2,$78,$CF,$D1,$F7,$17,$72,$B1,$FF,$3F    ;0.6931471805599452949907356518859092751897692718065
.db $99,$67,$2D,$16,$FC,$EF,$FD,$F5,$FD,$3F    ;0.240226506959101553103846007431060297021429734606215
.db $10,$CD,$AF,$24,$B8,$46,$58,$E3,$FB,$3F    ;5.55041086648024431020190322727610690536837023045e-2
.db $F8,$78,$4B,$E2,$7D,$5B,$95,$9D,$F9,$3F    ;9.6181291078536164406046473880520178751949899000523e-3
.db $5B,$9D,$F3,$DF,$38,$FF,$C3,$AE,$F6,$3F    ;1.33335581307383609544222238286864444825050937393667e-3
.db $A4,$71,$3C,$26,$F7,$89,$84,$A1,$F3,$3F    ;1.540353109220040892607797490525175686435054921034e-4
.db $BC,$AB,$25,$27,$57,$E7,$E5,$FF,$EF,$3F    ;1.5252713038026820986694573437398168701085442050318e-5
.db $66,$AE,$E1,$25,$E7,$82,$61,$B1,$EC,$3F    ;1.32159071914904607697946887057043728604916889120466e-6
.db $FA,$40,$26,$7A,$19,$AD,$72,$DA,$E8,$3F    ;1.01722755371157108831058054858407530634720014307972e-7
.db $5F,$A3,$56,$C8,$B3,$E2,$40,$F4,$E4,$3F    ;7.1087112650916814301740895279260149232576576809875e-9
.db $8C,$EE,$B8,$06,$1D,$21,$F6,$E2,$E0,$3F    ;4.1284045941236206883307640217911126100813512882446e-10
.db $3E,$73,$CA,$31,$87,$36,$5F,$9F,$DD,$3F    ;3.6236980527707885031220529305671221862606493025011e-11

#undefine xexp_x
#endif
