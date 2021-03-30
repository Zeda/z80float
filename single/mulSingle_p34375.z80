#ifndef included_mulSingle_p34375
#define included_mulSingle_p34375
#include "pushpop.z80"
#include "mov4.z80"
#define constmul_tmp scrap
mulSingle_p34375:
;multiply by 11/32, used for bgiSingle
  call pushpop
  push bc
  ld de,constmul_tmp
  call mov4
  ld a,(constmul_tmp+3)
  or a
  jr z,+_
  ld hl,(constmul_tmp)
  ld a,(constmul_tmp+2)
  ld e,a
  or $80
  ld e,a
  ld b,h
  ld c,l
  ld d,0
;DAHL is out, EBC is initial part
  srl e
  rr b
  rr c
  srl e
  rr b
  rr c
  adc hl,bc
  adc a,e
  jr nc,$+3
  inc d
  srl e
  rr b
  rr c
  adc hl,bc
  adc a,e
  jr c,$+5
  dec d
  jr nz,$+8
  rra
  rr h
  rr l
  scf

  ccf
  rla
  ld e,a
  ld a,(constmul_tmp+2)
  add a,a
  ld a,e
  rra
  ld (constmul_tmp+2),a
  ld (constmul_tmp),hl
  ld a,(constmul_tmp+3)
  sbc a,1
  ld (constmul_tmp+3),a
  jr nz,+_
  ld (constmul_tmp+2),a
_:
  ld hl,constmul_tmp
  pop de
  jp mov4
  ret
#endif
