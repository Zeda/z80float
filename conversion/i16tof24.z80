#ifndef included_i16tof24
#define included_i16tof24

i16tof24:
;Inputs:
;   HL holds a 16-bit signed integer, (-32768 to 32767)
;Outputs:
;   Converts to an f24 float in AHL
;   returns z flag set if zero, nz otherwise :)

  bit 7,h
  jr z,i16tof24_pos
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  ld b,$BF+16
  .db $11     ;start of `ld de,**`, eats the next two bytes
#ifndef included_u16tof24
#define included_u16tof24
u16tof24:
#else
.echo "Tip: i16tof24 already has a subroutine for u16tof24. Save space by including i16tof24.z80 first"
#endif
i16tof24_pos:
  ld b,$3F+16    ;Initial exponent and sign

;Check if HL is 0, if so return AHL == 0x000000
  ld a,h
  or l
  ret z

; HL is non-zero
; shift HL left until there is an overflow (the implicit bit)
; meanwhile, decrement B, the exponent each iteration
  dec b
  add hl,hl
  jr nc,$-2
  ld a,b
  ret
#endif
