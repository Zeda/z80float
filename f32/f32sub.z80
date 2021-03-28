#ifndef included_f32sub
#define included_f32sub
#include "pushpop.z80"
f32sub:
;x - y ==> z
;
  call pushpop
  ;save the location of the output
  push bc
  ex de,hl

  ; read and save the bottom 2 bytes of the first operand
  ld c,(hl)
  inc hl
  ld b,(hl)
  inc hl
  push bc

  ; read and save upper 2 bytes of the first operand
  ld c,(hl)
  inc hl
  ld a,(hl)
  xor 80h
  ld b,a
  jp f32add_part2
#include "f32add.z80"
#endif
