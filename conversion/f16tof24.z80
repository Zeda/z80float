#ifndef included_f16tof24
#define included_f16tof24

f16tof24:
;HL is the f16 input
;AHL is the f24 output

;check for inf or NaN
  ld a,h
  and %01111100
  jr z,f16tof24_zero
  cp %01111100
  jr z,f16tof24_inf_nan

  ; subtract 15 and add 63 to the exponent, net +48
;it is not a special value
  add hl,hl
  rla        ;A = xxxxxxxs
  add a,a    ;A = xxxxxxs0
  add a,a    ;A = xxxxxs00
  add hl,hl
  rla        ;A = xxxxs00e
  add hl,hl
  rla        ;A = xxxs00ee
  add hl,hl
  rla        ;A = xxs00eee
  add hl,hl
  rla        ;A = xs00eeee
  add hl,hl
  rla        ;A = s00eeeee
  ; Finally, subtract 15 and add 63 to the exponent
  add a,48
  ret

f16tof24_zero:
  sla h
  rra
  ret

f16tof24_inf_NaN:
  ld a,h
  and 3
  or l
  ld l,a
  ld a,h
  or $7F
  ld h,l
  ret
#endif
