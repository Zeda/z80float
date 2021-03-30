#ifndef included_xfma
#define included_xfma
#include "pushpop.z80"
#include "mov.z80"
#include "routines/add64.z80"
#include "routines/sub64.z80"
#include "routines/sla64.z80"
#include "routines/rr64.z80"
#include "routines/srl64.z80"
#include "routines/srl64_x4.z80"
#include "routines/swapbuf.z80"
#include "xmul.z80"


xfma:
;Fused Multiply-Add
;Performs x*y+t -> z
;HL points to x
;DE points to y
;BC points to z
;IX points to t
  call pushpop
  push bc   ;save the output location
  push ix   ;save the location of what to add

;First multiply x and y, but keep full 128-bits precision
  ld bc,var_z+8
  call xmul

;Now we need to perform a high-precision addition
;First we move the float to scrap
  pop hl
  ld de,var_z-10
  call mov10

;Now do a special add
  call fma_add

;Now return the result
  pop de
  ld hl,var_z+8
  jp mov10

fma_add:
; Zero out the bottom 8 bytes of the addend
  ld hl,0
  ld (var_z-12),hl
  ld (var_z-14),hl
  ld (var_z-16),hl
  ld (var_z-18),hl


; Check for special cases
	ld de,(var_z-2)
	ld hl,(var_z+16)
  res 7,h
  res 7,d

  ld a,h
  or l
  jp z,caseadd_fma
  ld a,d
  or e
  jp z,caseadd1_fma

; Now make sure var_z has the bigger exponent
  sbc hl,de
  jr nc,+_
  xor a
  sub l
  ld l,a
  sbc a,a
  sub h
  ld h,a
  push hl
; We need to swap.
  ld de,var_z-18
  ld hl,var_z
  ld bc,18
  call swapbuf
  pop hl
_:
  ld a,h
  or a
  ret nz
  ld a,l
  cp 130
  ret nc
;Now we need to shift down by A bits.
  or a
  jr z,add_shifted_fma
  rra \ call c,srl_var_z_m_18
  rra \ call c,srl2_var_z_m_18
  rra \ call c,srl4_var_z_m_18
  and $1F
  ld l,a
  ld bc,255&(var_z-19)
  ld h,(var_z-18)>>8
  add hl,bc
  sub 18
  cpl
  ld c,a
  ld de,var_z-19
  ldir
  ld c,a
  ld a,17
  sub c
  jr z,add_shifted_fma
  ld b,a
  xor a
  ld (de),a \ inc de \ djnz $-2
add_shifted_fma:
;If the signs match, then just add
;If they differ, then subtract
	ld hl,var_z-1
	ld a,(var_z+17)
  xor (hl)
  jp p,xfma_add

; Subtract the mantissas
  ld hl,var_z-18
  ld de,var_z
  call sub64
  inc hl
  inc de
  call sbc64
  jr nc,+_
;Negate the mantissa, invert the sign
; Invert the sign
  inc de
  inc de
  ld a,(de)
  xor 80h
  ld (de),a

; Negate the mantissa
  ld hl,var_z
  ld bc,$1000
  ld a,c \ sbc a,(hl) \ ld (hl),a \ inc hl
  djnz $-4
_:
  ret m

;need to shift up until top bit is 1. Should be at most 1 shift, I think
  ld de,(var_z+16)

; Make sure that the mantissa isn't zero
  ld hl,var_z
  ld b,15
  ld a,(hl)
_:
  inc hl \ or (hl) \ jr nz,+_
  djnz -_
  inc hl
  ld (hl),a
  inc hl
  ld (hl),a
  ret

_:
  dec de
  ld a,d
  and $7F
  or e
  jp z,add_zero_fma

  ld hl,var_z
  call sla64
  inc hl
  call rl64
  jp p,-_
  ld (var_z+16),de
  ret

xfma_add:
  ;add the mantissas
  ld hl,var_z-18
  ld de,var_z
  call add64
  inc hl
  inc de
  call adc64
  ret nc
  ex de,hl
  inc hl
  inc (hl) \ jr nz,+_
  inc hl
  inc (hl)
  ld a,(hl)
  dec hl
  and $7F
  jr z,add_inf_fma
  scf
_:
  dec hl
  jp rr64
srl4_var_z_m_18:
  ld hl,var_z-3
  ld b,a
  call srl64_4
  dec hl
  call rrd8
  ld a,b
  ret
srl2_var_z_m_18:
  call srl_var_z_m_18
srl_var_z_m_18:
  ld hl,var_z-3
  ld b,a
  call srl64
  dec hl
  call rr64
  ld a,b
  ret
caseadd_fma:
;zero+x => x for all x
;NaN +x => NaN for all x
;inf-inf=> NaN
;inf +x => inf, x != inf
  ret
caseadd1_fma:
;x+zero => x
;x+inf  => inf
;x+NaN  => NaN
  ret
add_zero_fma:
  xor a
  ld (var_z+15),a
  ld h,a
  ld l,a
  ld (var_z+16),hl
  ret
add_inf_fma:
  xor a
  ld (var_z+15),a
  dec a
  ld h,a
  ld l,a
  ld (var_z+16),hl
  ret
#endif
