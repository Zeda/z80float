#ifndef included_sqrt32
#define included_sqrt32
#include "sqrtHLIX.z80"
#include "mul16.z80"
#include "div/div32_16.z80"


#define var_c xOP1   ;input
#define var_y var_c+4 ;  used for sqrt32
#define var_x xOP2   ;output
#define var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#define var_a xOP2   ;   2 bytes
#define var_z0 xOP2+8;used in sqr32
;NOTE!
;This expects the top two bits to be non-zero

sqrt32:
;Speed: 358+sqrtHLIX+div32_16+mul16
;min: 2472      ;might be faster now, need to re-analyze
;max: 3262      ;+37cc slower, need to re-analyze
;avg: 2958.637  ;~37cc slower, need to re-analyze
;Step one is to generate 16 accurate bits
  ld hl,(var_y+2)
  ld ix,(var_y)
  call sqrtHLIX
  ld (var_x+6),de
  ld b,d
  ld c,e
;now AHL is the remainder with A at most 1.
;Fetch the next 16 bits and put them in DE
  ld de,(var_c+2)

;AHLDE is the new remainder
;Need to divide by 2, then divide by the 16-bit (var_x+4)
  rra
  rr h
  rr l
  rr d
  rr e
  ld ixh,d
  ld ixl,e

  or a
  sbc hl,bc
  jr z,sqrt32_higher_prec
  add hl,bc

  call div32_16   ;returns DE=quotient, HL is remainder
;Need to compute remainder
;(HL*2+(var_c+2)&1)*65536+(var_c))-DE*DE


  ld (var_x+4),de
  push hl
  ld b,d
  ld c,e
  call mul16
  ld b,h
  ld c,l
  ;DEBC
  ld hl,(var_c)
  ld a,(var_c+2)
  and 1
  sbc hl,bc
  ld b,h
  ld c,l

  rra
  pop hl
  adc hl,hl
  rla
  sbc hl,de
  sbc a,0
  ret

sqrt32_higher_prec:
;so we know the output is FFFF
  add hl,bc
  ld de,(var_c+2)
  ld a,d
  and $80
  add a,a
  adc hl,hl
  adc a,a
  ex de,hl
  ld bc,$0001
  ;or a
  sbc hl,bc
  ex de,hl
  ld bc,$FFFE
  sbc hl,bc
  sbc a,0

;AHLDE is the remainder
  inc c
  ld (var_x+4),bc
  ld b,d
  ld c,e
  ret




#undefine var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#undefine var_a xOP2   ;   2 bytes
#undefine var_c xOP2+8 ;input
#undefine var_y var_c+4 ;  used for sqrt32
#undefine var_z0 xOP2+16
#endif
