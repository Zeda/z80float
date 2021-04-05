#ifndef included_f32randnorm2
#define included_f32randnorm2
#include "f32randnorm.z80"

; The algorithm used in f32randnorm generates pairs of "normal random numbers",
; but the f32randnorm routine only calculates one of them. In order to generate
; the second value, all it costs is an additional multiplication, and that is
; what this extension of f32randnorm does :)
;
; This is particularly useful for statisitical applications that need to
; generate a lot of normal random numbers as this can eliminate the cost of:
;     2 rands
;     2 subtractions
;     2 multiplications
;     1 addition
;     1 logarithm
;     1 division
;     1 square root
;

#define f32randnorm_x f32log_x+4
#define f32randnorm_y f32randnorm_x+4
#define f32randnorm_s f32randnorm_y+4
#define f32randnorm_t f32randnorm_s+4

f32randnorm2:
; Note: This copies a pair of numbers to BC instead of a single number.
  call f32randnorm

  ; we already multipled X by T, now multiply Y by T
  push hl
  push de
  push bc
  ld hl,f32randnorm_y
  ld de,f32randnorm_t
  inc bc
  inc bc
  inc bc
  inc bc
  call f32randnorm_mul_rand_sign
  pop bc
  pop de
  pop hl
  ret
#endif
