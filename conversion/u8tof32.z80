#ifndef included_u8tof32
#define included_u8tof32

u8tof32:
;Inputs:
;   A holds a 8-bit unsigned integer, (0 to 255)
;   BC points to where to write the float
;Outputs:
;   Converts A to an f32 float at BC
;
  push hl
  push af

  ; Begin writing the float
  ld h,b
  ld l,c
  ld (hl),0
  inc hl
  ld (hl),0
  inc hl

  or a
  jr nz,$+8
  ld (hl),a
  inc hl
  ld (hl),a
  pop af
  pop hl
  ret

  push bc
  rl c        ; save the sign
  ld b,$7F+8  ;Initial exponent

  dec b
  add a,a
  jr nc,$-2

  rr c  ; shift in a 1 and shift out the sign
  rr b  ; shift the exponent down, shifting in the sign
  rra   ; shift the lsb of the exponent into the significand
  ld (hl),a
  inc hl
  ld (hl),b

  pop bc
  pop af
  pop hl
  ret
#endif
