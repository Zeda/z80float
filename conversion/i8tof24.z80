#ifndef included_i8tof24
#define included_i8tof24

i8tof24:
;Inputs:
;   A holds a 8-bit signed integer, (-128 to 127)
;Outputs:
;   Converts to an f24 float in AHL
;   returns z flag set if zero, nz otherwise :)

  or a
  jp p,+_
  neg
  ld b,$BF+8    ;Initial exponent and sign
  .db $11       ;start of instruction `ld de,**`
_:
#ifndef included_u8tof24
#define included_u8tof24
u8tof24:
#else
.echo "Tip: i8tof24 already has a subroutine for u8tof24. Save space by including i8tof24.z80 first"
#endif
  ld b,$3F+8    ;Initial exponent and sign

;Check if A is 0, if so return AHL == 0x00yyyy
  or a
  ret z


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
