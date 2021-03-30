#ifndef included_pow2Single
#define included_pow2Single
#include "pushpop.z80"
#include "mulSingle.z80"
#include "subSingle.z80"
#include "addSingle.z80"
#include "mov4.z80"
#include "constants.z80"

;requires       by
;   lgSingle    powSingle
;   mulSingle   powSingle,expSingle
;   invSingle   powSingle,expSingle,exp2Single

#define var_x   scrap     ;4 bytes
#define var_c   scrap+4   ;4 bytes

;           HL  DE  BC      desc
pow2Single:
;Computes 2^x
  call pushpop
  push bc

exp_inject:
;if x is on [0,1):
;  2^x = 1.000000001752 + x * (0.693146989552 + x * (0.2402298085906 + x * (5.54833215071e-2 + x * (9.67907584392e-3 + x * (1.243632065103e-3 + x * 2.171671843714e-4)))))
;Please note that usually I like to reduce to [-.5,.5] as the extra overhead is usually worth it.
;In this case, our polynomial is the same degree, with error different by less than 1 bit, so it's just a waste to range-reduce in this way.
;
;int(x) -> out_exp
;x-=int(x)  ;leaves x in [0,1)
;If x==0    -> out==1
;if x==inf  -> out==inf
;if x==-inf -> out==0
;if x==NAN  -> out==NAN
  ld de,var48+10
  call mov4
  ld hl,(var48+10)
  ld de,(var48+12)
  ld a,e
  add a,a
  push af   ;keep track of sign
  rrca
  ld (var48+12),a
  ld c,a
  ld a,d
    or a
    jp z,exp_spec
    cp 80h-23
    jp c,exp_underflow
    sub a,128
    jr c,+_ ;int(x)=0
    inc a
    cp 7
    jp nc,exp_overflow
    set 7,c
    ld b,a
    xor a
    add hl,hl \ rl c \ rla \ djnz $-4
    ld b,7Fh
    bit 7,c \ jr nz,exp_normalized
    ld e,a
    ld a,h \ or l \ or c
    ld a,e
    jr z,exp_zeroed
    dec b \ add hl,hl \ rl c \ jp p,$-4
    .db $11 ;start of `ld de,**`
exp_zeroed:
    ld b,0
exp_normalized:
    ld (var48+10),hl
    res 7,c
    ld (var48+12),bc
    .db $06 ;start of 'ld b,*` just to eat the next byte
_:
    xor a
comp_exp:
  pop hl
  rr l
  jr nc,+_
  cpl
  or a
  jp z,exp_underflow+1
  ;perform 1-(var48+10)--> var48+10
  ld hl,const_1
  ld de,var48+10
  ld b,d
  ld c,e
  call subSingle
_:
  push af
;our 'x' is at var48+10
;our `temp` is at var48+6 so as not to cause issues with mulSingle)
;uses 14 bytes of RAM
  ld hl,var48+10
  ld de,exp_a6
  ld bc,var48+6
  call mulSingle
  ld d,b
  ld e,c
  ld hl,exp_a5 \ call addSingle \ ld hl,var48+10 \ call mulSingle
  ld hl,exp_a4 \ call addSingle \ ld hl,var48+10 \ call mulSingle
  ld hl,exp_a3 \ call addSingle \ ld hl,var48+10 \ call mulSingle
  ld hl,exp_a2 \ call addSingle \ ld hl,var48+10 \ call mulSingle
  ld hl,exp_a1 \ call addSingle \ ld hl,var48+10 \ call mulSingle
  ld hl,const_1
  call addSingle
  ld hl,var48+9
  pop af
  add a,(hl)
  ld (hl),a
  ex de,hl
  pop de
  jp mov4
exp_spec:
;bit 6 means INF
;bit 5 means NAN
;no bits means zero
;NAN -> NAN
;+inf -> +inf
;-inf -> +0  because lim approaches 0 from the right
    ld a,c
    add a,a
    jr z,exp_zero
    jp m,exp_inf
;exp_NAN
    pop af
    ld de,0040h
exp_return_spec:
    pop hl
    rr e
    ld (hl),a \ inc hl
    ld (hl),a \ inc hl
    ld (hl),e \ inc hl
    ld (hl),d
    ret
exp_overflow:
exp_inf:
;+inf -> +inf
;-inf -> +0  because lim approaches 0 from the right
    pop af
    sbc a,a ;FF if should be 0,
    cpl
    and 80h
    ld d,0
    ld e,a
    jr exp_return_spec
exp_underflow:
exp_zero:
    pop af
    or a
    ld de,$8000
    jr exp_return_spec
#undefine var_x
#undefine var_c
#endif
