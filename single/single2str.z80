#ifndef included_single2str
#define included_single2str
#include "pushpop.z80"
#include "mov4.z80"
#include "mulSingle.z80"
#include "constants.z80"
#include "lut.z80"
#include "data.z80"

#define pow10exp_single  scrap+9
#define strout_single pow10exp_single+2

single2str:
  call pushpop
  push bc
  call +_
  pop de
  xor a
  cp (hl)
  ldi
  jr nz,$-3
  ret
_:
; Move the float to scrap
  ld de,scrap
  call mov4

; Make the float negative, write a '-' if already negative
  ld de,strout_single
  ld hl,scrap+2
  ld a,(hl)
  rlca
  scf
  rra
  ld (hl),a
  jr nc,+_
  ld a,$1A
  ld (de),a
  inc de
_:

; Check if the exponent field is 0 (a special value)
  inc hl
  ld a,(hl)
  or a
  jp z,strcase_single


; We should write '0' next. When rounding 9.999999... for example, not padding with a 0 will return '.' instead of '1.'
  ex de,hl
  ld (hl),'0'
  inc hl

; Save the pointer
  push hl

; Now we need to perform signed (A-128)*77 (approximation of exponent*log10(2))
  ld de,77
  ld h,a
  ld l,d
  call mul8_preset
  ld de,-77*128
  add hl,de
  ld a,h
  ld (pow10exp_single),a    ;The base-10 exponent
  ld de,pown10LUT
  jr c,+_
  neg
  ld de,pow10LUT   ;get the table of 10^-(2^k)
_:
  ld bc,scrap
  call singletostr_mul
  call singletostr_mul
  call singletostr_mul
  call singletostr_mul
  call singletostr_mul
  call singletostr_mul
;now the number is pretty close to a nice value

; If it is less than 1, multiply by 10
  ld a,(scrap+3)
  sub 128
  jr nc,+_
  ld de,const_10
  ;ld hl,scrap    ;Since singletostr_mul returns BC = scrap, can do this cheaper
  ;ld b,h
  ;ld c,l
  ld h,b
  ld l,c
  call mulSingle
  ld hl,pow10exp_single
  dec (hl)
  ld a,(scrap+3)
  sub 128
_:

; Convert to a fixed-point number !
  inc a
  ld b,a
  xor a
_:
  ld hl,scrap
  sla (hl)
  inc hl \ rl (hl)
  inc hl \ rl (hl)
  rla
  djnz -_

;We need to get 7 digits
  ld b,6
  pop hl    ;Points to the string

;The first digit can be as large as 20, so it'll actually be two digits
  cp 10
  jr c,+_
  dec b
;Increment the exponent :)
  ld de,(pow10exp_single-1)
  inc d
  ld (pow10exp_single-1),de
;
  ld (hl),'0'-1
  inc (hl) \ sub 10 \ jr nc,$-3
  add a,10
  inc hl
_:
; Get the remaining digits.
_:
  add a,'0'
  ld (hl),a
  inc hl
  push hl
  push bc
  call singletostrmul10
  pop bc
  pop hl
  djnz -_

;Save the pointer to the end of the string
  ld d,h
  ld e,l

;Now let's round!
  cp 5
  jr c,rounding_done_single
  .db $DA ;start of `jp c,*` in order to skip the next instruction
_:
  ld (hl),'0'
  dec hl
  inc (hl)
  ld a,(hl)
  cp $3A
  jr z,-_
rounding_done_single:


;Strip the leading zero if it exists (rounding may have bumped this to `1`)
  ld hl,strout_single
  ld a,(hl)
  cp $1A
  jr nz,+_
  inc hl
  ld a,(hl)
_:
  cp '0'
  jr nz,+_
  dec de
  ex de,hl
  ;Now lets move HL-DE bytes at DE+1 to DE
  sbc hl,de
  ld b,h
  ld c,l
  ld h,d
  ld l,e
  inc hl
  ldir
  cp a
_:

  push de
;If z flag is reset, this means that the exponent should be bumped up 1
  ld a,(pow10exp_single)
  jr z,+_
  inc a
  ld (pow10exp_single),a
_:

  ;if -4<=A<=6, then need to insert the decimal place somewhere.
  add a,4
  cp 10
  jp c,movdec_single
_:
  ;for this, we need to insert the decimal after the first digit
  ;Then, we need to append the exponent string
  ld hl,strout_single
  ld de,strout_single-1
  ld a,(hl)
  cp $1A    ;negative sign
  jr nz,+_
  ldi
_:
  ldi
  ld a,'.'
  ld (de),a

;remove any stray zeroes at the end before appending the exponent
  pop hl
  call strip_zeroes

; Write the exponent
  ld (hl),'e'
  inc hl
  ld a,(pow10exp_single)
  or a
  jp p,+_
  ld (hl),$1A    ;negative sign
  inc hl
  neg
_:
  cp 10
  jr c,+_
  ld (hl),'0'-1
  inc (hl)
  sub 10
  jr nc,$-3
  add a,10
  inc hl
_:
  add a,'0'
  ld (hl),a
  inc hl
  ld (hl),0
  ld hl,strout_single-1
  ret
movdec_single:
  ld a,(pow10exp_single)
  or a
  jp p,posdec_single
  ld l,a
;need to put zeroes before everything
  ld de,strout_single
  ld a,(de)
  cp $1A    ;negative sign
  push af
  ld a,'0'
  jr z,$+3
_:
  dec de
  ld (de),a
  inc l
  jr nz,-_
_:
  ex de,hl
  ld (hl),'.'
  pop af
  jr nz,+_
  dec hl
  ld (hl),a
_:
  ex de,hl
  pop hl
  call strip_zeroes
  ld (hl),0
  ex de,hl
  ret

posdec_single:
  ld hl,strout_single
  ld de,strout_single-1
  ld c,a
  ld a,(hl)
  ld b,0
  cp $1A    ;negative sign
  jr nz,+_
  inc c
_:
  inc c
  ldir
  ld a,'.'
  ld (de),a
  pop hl
  call strip_zeroes
  ld (hl),0
  ld hl,strout_single-1
  ret
strcase_single:
  ld hl,str_Zero
  ld a,(scrap+2)
  add a,a
  and $C0
  jr z,+_
  ld hl,str_Inf
  jp pe,+_
  ld hl,str_NaN
_:
  call mov4
  ld hl,strout_single
  ret

singletostrmul10:
;multiply the 0.24 fixed point number at scrap by 10
;overflow in A register
  ld a,(scrap+2)
  ld e,a
  ld hl,(scrap)
  xor a
  ld d,e
  ld b,h
  ld c,l
  add hl,hl \ rl d \ rla
  add hl,hl \ rl d \ rla
  add hl,bc
  ld b,a
  ld a,d
  adc a,e
  ld d,a
  ld a,b
  adc a,0
  add hl,hl \ rl d \ rla
  ld (scrap+1),de
  ld (scrap),hl
  ret



strip_zeroes:
  ld a,'0'
_:
  dec hl
  cp (hl)
  jr z,-_

;Check that the last  digit isn't a decimal!
  ld a,'.'
  cp (hl)
  ret z
  inc hl
  ret

singletostr_mul:
  rra
  call c,+_
  ld hl,4
  add hl,de
  ex de,hl
  ret
_:
  ld h,b
  ld l,c
  jp mulSingle
mul8:
;H*E => HL
  ld l,0
  ld d,l
mul8_preset:
  sla h \ jr nc,$+3 \ ld l,e
  add hl,hl \ jr nc,$+3 \ add hl,de
  add hl,hl \ jr nc,$+3 \ add hl,de
  add hl,hl \ jr nc,$+3 \ add hl,de
  add hl,hl \ jr nc,$+3 \ add hl,de
  add hl,hl \ jr nc,$+3 \ add hl,de
  add hl,hl \ jr nc,$+3 \ add hl,de
  add hl,hl \ ret nc \ add hl,de
  ret
#endif
