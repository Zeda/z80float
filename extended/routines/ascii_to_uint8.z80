#ifndef included_ascii_to_uint8
#define included_ascii_to_uint8
ascii_to_uint8:
;c flag means don't increment the exponent
  ld c,0
  ld a,(hl)
  jr c,ascii_to_uint8_noexp
  cp char_DEC
  jr z,ascii_to_uint8_noexp-2
_:
  sub 3Ah
  add a,10
  jr nc,ascii_to_uint8_noexp_end
  inc b
  ld c,a
  add a,a
  add a,a
  add a,c
  add a,a
  ld c,a
  inc hl
_:
  ld a,(hl)
  cp char_DEC
  jr z,ascii_to_uint8_noexp_2nd
_:
  sub 3Ah
  add a,10
  jr nc,ascii_to_uint8_noexp_end
  inc b
  add a,c
  inc hl
  ld (de),a
  dec de
  or a
  ret

  inc hl
  ld a,(hl)
ascii_to_uint8_noexp:
  sub 3Ah
  add a,10
  jr nc,ascii_to_uint8_noexp_end
  ld c,a
  add a,a
  add a,a
  add a,c
  add a,a
  ld c,a
ascii_to_uint8_noexp_2nd:
  inc hl
  ld a,(hl)
  sub 3Ah
  add a,10
  jr nc,ascii_to_uint8_noexp_end
  add a,c
  inc hl
  .db $FE   ;start of `cp **`, saves 1cc
ascii_to_uint8_noexp_end:
  ld a,c
  ld (de),a
  dec de
  scf
  ret
#endif
