#ifndef included_f32logy
#define included_f32logy
#include "pushpop.z80"
#include "f32log.z80"
#include "f32div.z80"

#define f32logy_x f32log_x+4

f32logy:
;log_y(x)
  call pushpop
  push bc
  ld bc,f32logy_x
  call f32log
  ex de,hl
  ld bc,f32log_x
  call f32log
  ld d,b
  ld e,c
  ld hl,f32logy_x
  pop bc
  jp f32div
#endif
