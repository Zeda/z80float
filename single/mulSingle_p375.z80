#ifndef included_mulSingle_p375
#define included_mulSingle_p375
#include "pushpop.z80"
#include "mov4.z80"

#define p375_tmp scrap
mulSingle_p375:
  call pushpop
  push bc
  ld de,p375_tmp
  call mov4
  ld a,(p375_tmp+3)
  or a
  jr z,p375_end
  ld hl,(p375_tmp)
  ld a,(p375_tmp+2)
  ld e,a
  or $80
  ld e,a
  ld b,h
  ld c,l
;HLA0 is out, EBC is other part
  srl e
  rr b
  rr c
  adc hl,bc
  adc a,e
  jr nc,+_
  rra
  rr h
  rr l
  scf
_:
  ccf
  rla
  ld e,a
  ld a,(p375_tmp+2)
  add a,a
  ld a,e
  rra
  ld (p375_tmp+2),a
  ld (p375_tmp),hl
  ld a,(p375_tmp+3)
  sbc a,1
  ld (p375_tmp+3),a
  jr nz,p375_end
  ld (p375_tmp+2),a
p375_end:
  ld hl,p375_tmp
  pop de
  jp mov4
#endif
