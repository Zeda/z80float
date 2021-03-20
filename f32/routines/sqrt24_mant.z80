#ifndef included_sqrt24_mant
#define included_sqrt24_mant

#include "sqrtHLIX.z80"

sqrt24_mant:
;DEB.C is the 24-bit mantissa with C as any extra bits used for rounding.
;Output: DEL
  push bc
  pop ix
  ex de,hl
;HLIX
  call sqrtHLIX
;AHL is the new remainder
;Need to divide by 2, then divide by DE
  rra
  ld a,h
;HL/DE to 8 bits
;We are just going to approximate it
  res 0,l \     jr c,$+5 \ cp d \ jr c,$+4 \ sub d \ inc l
  sla l \ rla \ jr c,$+5 \ cp d \ jr c,$+4 \ sub d \ inc l
  sla l \ rla \ jr c,$+5 \ cp d \ jr c,$+4 \ sub d \ inc l
  sla l \ rla \ jr c,$+5 \ cp d \ jr c,$+4 \ sub d \ inc l
  sla l \ rla \ jr c,$+5 \ cp d \ jr c,$+4 \ sub d \ inc l
  sla l \ rla \ jr c,$+5 \ cp d \ jr c,$+4 \ sub d \ inc l
  sla l \ rla \ jr c,$+5 \ cp d \ jr c,$+4 \ sub d \ inc l
  sla l \ rla \ jr c,$+5 \ cp d \ ret c    \ sub d \ inc l
  ret

#endif
