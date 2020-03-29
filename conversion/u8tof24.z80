#ifndef included_u8tof24
#define included_u8tof24

u8tof24:
;Inputs:
;   A holds a 8-bit unsigned integer, (0 to 255)
;Outputs:
;   Converts to an f24 float in AHL
;   returns z flag set if zero, nz otherwise :)

;Check if A is 0, if so return AHL == 0x00yyyy
  or a
  ret z

  ld b,$3F+8    ;Initial exponent and sign

; A is non-zero
; shift A left until there is an overflow (the implicit bit)
; meanwhile, decrement B, the exponent each iteration
  dec b
  add a,a
  jr nc,$-2
  ld h,a
  ld l,0
  ld a,b
  ret
#endif
