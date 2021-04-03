#ifndef included_xtof64
#define included_xtof64

#include "routines/rr64.z80"
#include "mov.z80"
#include "pushpop.z80"

xtof64:
;Inputs:
;   HL points to the input extended-precision float
;   BC points to where to output the result
;Outputs:
;   The extended-precision float is converted to a double (binary64) at BC.
;

;bias is 1023, so 0x03FF is exponent of 0
;sign is 1 bit
;exponent is 11 bits
;mantissa is 53 bits (top bit is implicit)
;

  call pushpop
xtof64_nopush:

  ; The extended precision float has a 64-bit mantissa, so drop the bottom byte.
  inc hl

  ; Move the remaining 7 bytes to our output
  ld d,b
  ld e,c
  call mov6
  ld a,(hl)
  ld (de),a

  ; the next two bytes are the exponent and sign
  inc hl
  ld c,(hl)
  inc hl
  ld b,(hl)

  ; Check if the input is a special number
  ld a,b
  add a,a
  or c
  jr z,xtof64_special

  ;save the sign
  ld a,b
  res 7,b

  ; make sure the exponent is not too small
  ld hl,-15362
  add hl,bc
  jr nc,xtof64_zero

  ; make sure the exponent is not too big
  ld bc,-2045
  add hl,bc
  jr c,xtof64_inf

  ; now we need to adjust the exponent
  ld bc,2046
  add hl,bc

  ;now we shift the exponent down into the top bit of the mantissa
  ex de,hl
  rl (hl)
  rr d
  rr e
  rr (hl)

;now shift DE down 3 more bits into the old mantissa
;final shift, shift the sign into E
  ld bc,6
  rr d \ rr e \ call rr56 \ add hl,bc
  rr d \ rr e \ call rr56 \ add hl,bc
  rla \ rr e \  call rr56
  ;need to potentially round up!
  jr nc,+_
  dec c
  jr z,$+7
  inc (hl)
  inc hl
  jr z,$-5
  .db $FE
  inc e
_:
  inc c \ add hl,bc

;now write the top 7 bits of the exponent and the sign to the output
  ld (hl),e
  ret

xtof64_special:
  ld a,(de)
  add a,a
  jr c,xtof64_inf
  jp p,xtof64_zero
xtof64_nan:
;mantissa needs to be non-zero to encode NaN
  ld a,-1
  ex de,hl
  ld (hl),a
  inc hl
  ld (hl),a
  inc hl
;  rl b
;  rra
  ld (hl),a
  ret

xtof64_inf:
;carry is always set here
xtof64_zero:
;carry is always reset here
  sbc a,a
  ex de,hl

  inc hl
  and $F0
  ld (hl),a
  add a,a
  sbc a,a
  inc hl
  rl b
  rra
  ld (hl),a

; need to set mantissa to 0
  dec hl
  ld bc,$0600
_:
  dec hl
  ld (hl),c
  djnz -_
  ret
#endif
