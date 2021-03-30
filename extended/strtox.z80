#ifndef included_strtox
#define included_strtox
#include "mov.z80"
#include "pushpop.z80"
#include "routines/sla64.z80"
#include "routines/ascii_to_uint8.z80"
#include "tables.z80"
#include "constantsx.z80"
#include "xmul.z80"

#ifndef char_TI_TOK
#define char_NEG  $1A
#define char_ENG  $1B
#define char_DEC  '.'
#else
;otherwise, char_TI_CHR
#define char_NEG  $B0
#define char_ENG  $3B
#define char_DEC  $3A
#endif

#ifndef strtox_ptr
#define strtox_ptr xOP1+25
#endif
strtox:
;;#Routines/Extended Precision
;;Inputs:
;;  HL points to the string
;;  BC points to where the float is output
;;Output:
;;  xOP1+25 is the pointer to the end of the string
;;Destroys:
;;  25 bytes at xOP1 ?
  call pushpop
  push bc

;Check if there is a negative sign.
;   Save for later
;   Advance ptr
  ld a,(hl)
  sub char_NEG
  sub 1
  push af
  jr nc,+_
  inc hl
_:
  call strtox_sub0
TItox_stepin:
;Gotta multiply the number at (xOP1) by 2^64

;Save the location of the ending byte of the string
  ld (strtox_ptr),hl
  ld d,100
  call xOP1_xtimes_256
  ld (xOP1+17),a
  call xOP1_xtimes_256
  ld (xOP1+16),a
  call xOP1_xtimes_256
  ld (xOP1+15),a
  call xOP1_xtimes_256
  ld (xOP1+14),a
  call xOP1_xtimes_256
  ld (xOP1+13),a
  call xOP1_xtimes_256
  ld (xOP1+12),a
  call xOP1_xtimes_256
  ld (xOP1+11),a
  call xOP1_xtimes_256
  ld (xOP1+10),a
  call xOP1_xtimes_256
  ld (xOP1+9),a

;Now xOP1+9 is a 9-byte mantissa that needs to be normalized
;
  ld hl,(xOP1+10)
  or h
  or l
  ld hl,(xOP1+12)
  or l
  or h
  ld hl,(xOP1+14)
  or h
  or l
  ld hl,(xOP1+16)
  or l
  or h
  jp z,strtox_zero-1
  pop af
  push bc
  ld bc,$7FFF
  rr b
  ld a,h
  or a
  jp m,strtox_normed
  ;Will need to iterate at most three times
_:
  dec bc
  ld hl,xOP1+9
  call sla64
  adc a,a
  jp p,-_
strtox_normed:
;Move the number to xOP1
  ld hl,(xOP1+10)
  ld (xOP1),hl
  ld hl,(xOP1+12)
  ld (xOP1+2),hl
  ld hl,(xOP1+14)
  ld (xOP1+4),hl
  ld hl,(xOP1+16)
  ld h,a
  ld (xOP1+6),hl
  ld (xOP1+8),bc
  pop bc
;now (xOP1) is our number, need to multiply by power of 10!
;Power of 10 is stored in B, need to put in A first
  xor a
  sub b
  ld de,pow10table+120
  jp p,+_
  xor a \ sub c \ ld c,a
  sbc a,a \ sub b \ ld b,a
  ld de,pown10table+120
_:
  ld hl,xOP1
_:
  srl b
  rr c
  call +_
  ld a,b
  or c
  jr nz,-_
  pop de
  jp mov10
_:
  push bc
  ld b,h
  ld c,l
  call c,xmul
  pop bc
  ld a,e
  sub 10
  ld e,a
  ret nc
  dec d
  ret

_:
  inc hl
strtox_sub0:
;Skip all leading zeroes
  ld a,(hl)
  cp '0'
  jr z,-_

;Set exponent to 0
  ld bc,0
;Check if the next char is char_DEC
  sub char_DEC
  or a
  jr nz,+_
  inc c
;Get rid of zeroes
  ld a,'0'
  cpi
  jr z,$-2
  scf
_:
;Now we read in the next 20 digits
  ld de,xOP1+9
  push bc
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  call ascii_to_uint8
  ld a,b
  pop bc
  push af
  add a,c
  ld c,a
  jr nc,$+3
  inc b
  pop af
;Now `xOP1` holds the 10-digit base-100 number.
;BC is the exponent
;if carry flag is set, just need to get rid of remaining digits
;Otherwise, need to get rid of remaining digits, while incrementing the exponent
  call skipdigits
;Now check for engineering `E` to modify the exponent
  cp char_ENG-'0'
  ret nz
str_xeng_exp:
  ld de,0
  inc hl
  ld a,(hl)
  cp char_NEG    ;negative exponent?
  push af
  jr nz,$+3
  inc hl
_:
  ld a,(hl)
  sub 3Ah
  add a,10
  jr nc,+_
  inc hl
  push hl
  ld h,d
  ld l,e
  add hl,hl
  add hl,hl
  add hl,de
  add hl,hl
  add a,l
  ld l,a
  ex de,hl
  pop hl
  jr -_
_:
  ld a,d
  cp 20
  jp nc,xeng_overflow
  pop af
  ld a,c
  jr nz,+_
  sub e
  ld c,a
  ld a,b
  sbc a,d
  ld b,a
  ret
_:

  add a,e
  ld c,a
  ld a,d
  adc a,b
  ld b,a
  ret
xOP1_xtimes_256:
  push bc
  ld e,8
_:
  or a
  ld hl,xOP1
  call +_
  call +_
  rl c
  dec e
  jr nz,-_
  ld a,c
  pop bc
  ret
_:
  call xOP1_xtimes_sub
  call xOP1_xtimes_sub
  call xOP1_xtimes_sub
  call xOP1_xtimes_sub
xOP1_xtimes_sub:
  ld a,(hl)
  rla
  cp d
  jr c,+_
  sub d
_:
  ld (hl),a
  inc hl
  ccf
  ret
xeng_overflow:
  pop af
  jr nz,strtox_inf
  pop af
strtox_zero:
  ld hl,xconst_0
  pop de
  jp mov10
strtox_inf:
;return inf
  pop af
  ld hl,xconst_inf
  jr nc,+_
  ld hl,xconst_nINF
_:
  pop de
  jp mov10


skipdigits:
  jr nc,skipdigits_nodec
  .db $FE     ; start of `cp *` to skip the `inc hl`
_:
  inc hl
  ld a,(hl)
  sub '0'
  cp 10
  jr c,-_
  ret

_:
  inc hl
  inc bc
skipdigits_nodec:
  ld a,(hl)
  sub '0'
  cp 10
  jr c,-_
  ret
#endif
