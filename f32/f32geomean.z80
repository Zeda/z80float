#ifndef included_f32geomean
#define included_f32geomean

#include "f32mul.z80"
#include "f32sqrt.z80"

f32geomean:
;sqrt(x*y) ==> AHL
  push hl
  call f32mul
  ld h,b
  ld l,c
  call f32sqrt
  pop hl
  ret


; ;return NaN if the product is negative
;   xor c
;   jp p,+_
;   ld a,$7F
;   ld h,a
;   ret
; _:
;
; ;the product is positive, so we can just set the inputs to positive
;   xor c
;   and $7F
;   ret z   ;may as well exit if the input is 0
;   cp $7F
;   jr z,f32geomean_sub
;   ld b,a
;
;   ld a,c
;   and $7F
;   ret z
;   cp $7F
;   jr z,f32geomean_sub
;
; ;now calculate the output exponent
;   add a,b
;   rra
;   push af
;
;   ld a,63
;   ld c,a
;   adc a,0
;   call f32geomean_sub
;   pop bc
;   add a,b
;   sub 63
;   ret
;
; f32geomean_sub:
;   call f32mul
;   jp f32sqrt
#endif
