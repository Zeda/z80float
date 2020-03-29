#ifndef included_u16tof24
#define included_u16tof24

u16tof24:
;Inputs:
;   HL holds a 16-bit unsigned integer, (0 to 65535)
;Outputs:
;   Converts to an f24 float in AHL
;   returns z flag set if zero, nz otherwise :)


;Check if HL is 0, if so return AHL == 0x000000
  ld a,h
  or l
  ret z

  ld a,$3F+16    ;Initial exponent and sign

; HL is non-zero
; shift HL left until there is an overflow (the implicit bit)
; meanwhile, decrement A, the exponent each iteration
  dec a
  add hl,hl
  jr nc,$-2
  ret
#endif
