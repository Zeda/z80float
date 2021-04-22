#ifndef included_i8tof32
#define included_i8tof32

i8tof32:
;Inputs:
;   A holds a 8-bit signed integer, (-128 to 127)
;   BC points to where to write the float
;Outputs:
;   Converts A to an f32 float at BC
;
  push hl
  push af

  or a
  jp p,$+6
  neg
  scf

; #ifndef included_u8tof32
; ##define included_u8tof32
;   .db $21   ; start of `ld hl,*` to skip the next byte
; u8tof32:
;   push hl
;   push af
; #else
; .echo "Hint: it looks like you are using u8tof32 as well as i8tof32. i8tof32 already has code for u8tof32, so you can save bytes by including it first."
; #endif
;
  ; Begin writing the float
  ld h,b
  ld l,c
  ld (hl),0
  inc hl
  ld (hl),0
  inc hl

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
