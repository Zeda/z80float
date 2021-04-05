#ifndef included_f32randnorm
#define included_f32randnorm
#include "pushpop.z80"
#include "f32log.z80"
#include "f32rand.z80"
#include "f32mul2.z80"
#include "f32mul.z80"
#include "f32sub.z80"
#include "f32add.z80"
#include "f32div.z80"
#include "f32sqrt.z80"


; This is based on https://en.wikipedia.org/wiki/Marsaglia_polar_method

#define f32randnorm_x f32log_x+4
#define f32randnorm_y f32randnorm_x+4
#define f32randnorm_s f32randnorm_y+4
#define f32randnorm_t f32randnorm_s+4

f32randnorm:
  call pushpop
  push bc

f32randnorm_gen_xy:
; We need to generate two random numbers, X and Y
  ld bc,f32randnorm_x
  call f32rand
; square our number, storing in T for now
  ld h,b
  ld l,c
  ld d,b
  ld e,c
  ld bc,f32randnorm_t
  call f32mul

  ld bc,f32randnorm_y
  call f32rand
; square it, storing to S for now
  ld h,b
  ld l,c
  ld d,b
  ld e,c
  ld bc,f32randnorm_s
  call f32mul

; sum of the squares
  ld h,b
  ld l,c
  ld de,f32randnorm_t
  call f32add

; If the sum is >= 1, re-generate x and y
  ld a,(f32randnorm_s+2)
  add a,a
  ld a,(f32randnorm_s+3)
  adc a,a
  cp $7F
  jr nc,f32randnorm_gen_xy

; calculate the natural log of s, storing to t
  ld b,d
  ld c,e      ;HL=S, DE=T, BC=T
  call f32log

; set T positive
  ld a,(f32randnorm_t+3)
  and %01111111
  ld (f32randnorm_t+3),a

;multiply by 2
  ex de,hl
  call f32mul2

; divide t by s. Helpfully, HL=T, DE=S, BC=T
  call f32div
; square root
  call f32sqrt

; multiply X (and/or Y) by T
  ld de,f32randnorm_x
  pop bc
f32randnorm_mul_rand_sign:
  call f32mul
; Finally, assign a random sign to the output
; Assign a random sign to X and Y
  push bc
  call rand
  sla h   ; random bit
  pop hl
  ret nc
  inc hl
  inc hl
  inc hl
  set 7,(hl)
  ret
#endif
