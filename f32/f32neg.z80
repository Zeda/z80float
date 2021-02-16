#ifndef included_f32neg
#define included_f32neg

f32neg:
;-x ==> z
  push hl
  push de
  push bc
  push af
  ld d,b
  ld e,c
  ldi
  ldi
  ldi
  ld a,(hl)
  xor 80h
  ld (de),a
  pop af
  pop bc
  pop de
  pop hl
  ret
#endif
