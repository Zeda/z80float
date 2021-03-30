#ifndef included_ti2Single
#define included_ti2Single
#include "pushpop.z80"
#include "mov4.z80"
#include "mulSingle.z80"
#include "str2single.z80"
ti2single:
;converts a TI-float to a single precision float.
  call pushpop
  push bc

;Save the sign !
  ld a,(hl)
  add a,a
  push af

;Save the base 10 exponent
  inc hl
  ld a,(hl)
  push af

;Convert four bytes of the mantissa (BCD) to an 8-bit integer on [0,99].
;TI's is big-endian and we want little endian copied to scrap
  ld de,scrap+3
  ld b,4
_:
  inc hl
  ld a,(hl)
  and $F0
  rra
  ld c,a
  rra
  rra
  sub c
  add a,(hl)
  ld (de),a
  dec de
  djnz -_

;Now get 4 bytes of the binary float's mantissa
  ld d,100
  call scrap_times_256
  ld a,c
  push af
  call scrap_times_256
  push bc
  call scrap_times_256
  push bc
  call scrap_times_256
  ld l,c
  pop bc
  ld h,c
  pop bc
  pop af

;Now let's normalize our mantissa, ACHL
  ld b,$7F
  or a
  jp m,ti2single_normalized
_:
  dec b
  add hl,hl
  rl c
  adc a,a
  jp p,-_
ti2single_normalized:
;Our float is BACH.
  ld l,h
  ld h,c
  add a,a
  ld c,a

;Pop off the exponent.
  pop de

;Pop off the sign
  pop af
  rr c

  ld (scrap),hl
  ld (scrap+2),bc



  ld a,d
  sub 7Fh
  ld de,pow10LUT
  jr nc,+_
  neg
  ld de,pown10LUT
  cp 40
  jp nc,strToSingle_zero
_:
  cp 40
  jp nc,strToSingle_inf+1

;
  ld hl,scrap
  ld b,h
  ld c,l
  call +_
  call +_
  call +_
  call +_
  call +_
  call +_
  pop de
  jp mov4
_:
  rra
  call c,mulSingle
  inc de
  inc de
  inc de
  inc de
  ret
#endif
