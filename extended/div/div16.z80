#ifndef included_div16
#define included_div16
divide16:
;max: 958cc
;min: 663cc
;avg: 783.25cc
  xor a
  add hl,hl \ jp c,div16_0_2
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_1_2
div16_1_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_2_2
div16_2_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_3_2
div16_3_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_4_2
div16_4_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_5_2
div16_5_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_6_2
div16_6_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_7_2
div16_7_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jp c,div16_8_2
div16_8_1:
  ld d,a
  xor a
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jr c,div16_9_2
div16_9_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jr c,div16_10_2
div16_10_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jr c,div16_11_2
div16_11_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jr c,div16_12_2
div16_12_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jr c,div16_13_2
div16_13_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jr c,div16_14_2
div16_14_1:
  sbc hl,bc \ jr nc,$+3 \ add hl,bc \ rla \ add hl,hl \ jr c,div16_15_2
div16_15_1:
  add a,a
  ld e,a
  sbc hl,bc \ ret nc \ add hl,bc \ inc e \ ret

div16_0_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jp nc,div16_1_1
div16_1_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jp nc,div16_2_1
div16_2_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jp nc,div16_3_1
div16_3_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jp nc,div16_4_1
div16_4_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jp nc,div16_5_1
div16_5_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jp nc,div16_6_1
div16_6_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jp nc,div16_7_1
div16_7_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jr nc,div16_8_1
div16_8_2:

  ld d,a
  xor a \ sbc hl,bc \ add hl,hl \ jr nc,div16_9_1
div16_9_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jr nc,div16_10_1
div16_10_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jr nc,div16_11_1
div16_11_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jr nc,div16_12_1
div16_12_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jr nc,div16_13_1
div16_13_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jr nc,div16_14_1
div16_14_2:
  add a,a \ sbc hl,bc \ add hl,hl \ jr nc,div16_15_1
div16_15_2:
  add a,a \ ld e,a \ sbc hl,bc \ ret
#endif
