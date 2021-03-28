#ifndef included_xatan
#define included_xatan
#include "pushpop.z80"
#include "constantsx.z80"
#include "xmul.z80"
#include "xadd.z80"
#include "xsqrt.z80"
#include "xbg.z80"

;x/BG(1,sqrt(1+x^2))
#define var_x  xOP1+152
xatan:
  call pushpop
  push bc
  ld de,var_x
  call mov10

  ld de,(var_x+8)
  ld a,d
  and $7F
  or e
  jr z,xatan_special

; ;If x>=1.0, calculate as pi/2-atan(1/x)
  ld hl,var_x
;   ld a,(var_x+9)
;   and $7F
;   cp $40
;   jr c,+_
;   ld b,h
;   ld c,l
;   call xinv
;   call +_+1
;   pop bc
;   ld de,xconst_pi_div_2
;   jp xrsub
; _:
;   .db $FE
;   push bc
  ld d,h
  ld e,l
  ld bc,xOP2
  call xmul
  ld h,b
  ld l,c
  ld de,xconst_1
  call xadd
  call xsqrt
  ex de,hl
  call xbg
  ld hl,var_x
  pop bc
  jp xmul
xatan_special:
  ld hl,var_x
  ld a,(var_x+7)
  and $C0
  jr z,xatan_return
  jp p,xatan_return
  ld hl,xconst_pi_div_2
xatan_return:
  sla d
  pop de
  call mov9
  ld a,(hl)
  rla
  rrca
  ld (de),a
  ret

#endif
