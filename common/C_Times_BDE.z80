#ifndef included_C_times_BDE
#define included_C_times_BDE

C_times_BDE:
;C*BDE => CAHL
;C>=128    155+6*(20+{0,21+{0,1}}) + {0,20+{0,8}}
;C>=64     155+5*(20+{0,21+{0,1}}) + {0,20+{0,8}}
;C>=32     155+4*(20+{0,21+{0,1}}) + {0,20+{0,8}}
;C>=16     155+3*(20+{0,21+{0,1}}) + {0,20+{0,8}}
;C>=8      155+2*(20+{0,21+{0,1}}) + {0,20+{0,8}}
;C>=4      155+1*(20+{0,21+{0,1}}) + {0,20+{0,8}}
;C>=2      155+0*(20+{0,21+{0,1}}) + {0,20+{0,8}}
;C==1      136
;C==0      152
;max: 435cc
;min: 136cc
;avg: ~320.87cc (320+223/256)
;114 bytes
;
  ld a,b
  ld h,d
  ld l,e
  sla c \ jr c,mul8_24_1
  sla c \ jr c,mul8_24_2
  sla c \ jr c,mul8_24_3
  sla c \ jr c,mul8_24_4
  sla c \ jr c,mul8_24_5
  sla c \ jr c,mul8_24_6
  sla c \ jr c,mul8_24_7
  sla c \ ret c
  ld a,c
  ld h,c
  ld l,c
  ret
mul8_24_1:
    add hl,hl \ rla \ rl c \ jr nc,$+7 \ add hl,de \ adc a,b \ jr nc,$+3 \ inc c
mul8_24_2:
    add hl,hl \ rla \ rl c \ jr nc,$+7 \ add hl,de \ adc a,b \ jr nc,$+3 \ inc c
mul8_24_3:
    add hl,hl \ rla \ rl c \ jr nc,$+7 \ add hl,de \ adc a,b \ jr nc,$+3 \ inc c
mul8_24_4:
    add hl,hl \ rla \ rl c \ jr nc,$+7 \ add hl,de \ adc a,b \ jr nc,$+3 \ inc c
mul8_24_5:
    add hl,hl \ rla \ rl c \ jr nc,$+7 \ add hl,de \ adc a,b \ jr nc,$+3 \ inc c
mul8_24_6:
    add hl,hl \ rla \ rl c \ jr nc,$+7 \ add hl,de \ adc a,b \ jr nc,$+3 \ inc c
mul8_24_7:
    add hl,hl \ rla \ rl c \ ret nc \ add hl,de \ adc a,b \ ret nc \ inc c \ ret
#endif
