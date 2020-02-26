#ifndef included_div32_16
#define included_div32_16

#define var_x xOP2   ;output
#define var_b xOP2   ; 4 bytes, result gets copied to bottom anyways
#define var_n xOP3
div32_16:
;HLDE/BC, BC>HL
;770+16{0,10}+{0,20+{0,22+{0,21}}}
;min: 770
;max: 993
;avg: 868.125

  push bc
  ld a,b
  srl a
  cpl
  ld b,a
  ld a,c
  rra
  cpl
  ld c,a
  inc bc
  ld a,d
  add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  ld d,a
  ld a,e
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl \ add hl,bc \ jr c,$+4 \ sbc hl,bc
  rla \ adc hl,hl
  ld e,a
  pop bc
  bit 0,c
  ret z
;HL is the remainder
;r-Q*E = HL-DE
  sbc hl,de
  ret nc
  add hl,bc
  dec de
  ret c
  add hl,bc
  dec de
  ret
#endif
