#ifndef included_ascii_to_BCD
#define included_ascii_to_BCD

#ifndef TOK_DECIMAL
#ifdef TOK_DECIMAL
#define TOK_DECIMAL TOK_DECIMAL
#else
#define TOK_DECIMAL '.'
#endif
#endif

ascii_to_BCD:
;Inputs:
;   HL points to the next digit to read in
;   B is the base-10 exponent
;   carry flag is set if we shouldn't increment the exponent
;Outputs:
;   HL is advanced as needed (not necessarily by 2)
;   A is the next BCD byte
;   carry is set if it was already set initially, or if a decimal was reached,
;   or if a non-numeric character was reached, otherwise, carry remains reset.
;Destroys:
;   C
  jr c,ascii_to_BCD_noexp
  ld a,(hl)
  cp TOK_DECIMAL
  jr z,ascii_to_BCD_decimal_found1
  cp '0'
  jr c,ascii_to_BCD_done1
  cp '9'+1
  jr nc,ascii_to_BCD_done1
  inc hl
  inc b
  add a,a
  add a,a
  add a,a
  add a,a
  ld c,a

  ld a,(hl)
  cp TOK_DECIMAL
  jr z,ascii_to_BCD_decimal_found2
  cp '0'
  jr c,ascii_to_BCD_done2
  cp '9'+1
  jr nc,ascii_to_BCD_done2
  inc hl
  inc b
  and %00001111
  or c
  ret

ascii_to_BCD_done1:
  xor a
  scf
  ret
ascii_to_BCD_done2:
  ld a,c
  scf
  ret

ascii_to_BCD_decimal_found1:
  inc hl
ascii_to_BCD_noexp:
  ld a,(hl)
  cp '0'
  jr c,ascii_to_BCD_done1
  cp '9'+1
  jr nc,ascii_to_BCD_done1
  add a,a
  add a,a
  add a,a
  add a,a
  ld c,a

ascii_to_BCD_decimal_found2:
  inc hl
  ld a,(hl)
  cp '0'
  jr c,ascii_to_BCD_done2
  cp '9'+1
  jr nc,ascii_to_BCD_done2
  inc hl
  and %00001111
  or c
  scf
  ret
#endif
