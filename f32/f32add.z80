#ifndef included_f32add
#define included_f32add
#include "pushpop.z80"

; uses stack and registers for all operations

f32add:
;x + y ==> z
;
  call pushpop
  ;save the location of the output
  push bc

  ; read and save the bottom 2 bytes of the first operand
  ld c,(hl)
  inc hl
  ld b,(hl)
  inc hl
  push bc

  ; read and save upper 2 bytes of the first operand
  ld c,(hl)
  inc hl
  ld b,(hl)
f32add_part2:

  ex de,hl  ; prepare to process the second operand

  ; check the exponent of the first operand for special values
  ld a,c
  add a,a
  ld a,b
  adc a,a
  ld e,a  ;save the exponent of the first operand
  jp z,f32_add_0_op2
  inc a
  jp z,f32_add_infnan_op2
  push bc

  ; now read the second operand
  ld c,(hl)
  inc hl
  ld b,(hl)
  inc hl
  push bc
  ld c,(hl)
  inc hl
  ld b,(hl)

  ; check the exponent of the second operand for special values
  ld a,c
  add a,a
  ld a,b
  adc a,a
  jp z,f32_add_op1_0
  inc a
  jp z,f32_add_op1_infnan

;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
; Now we re-align the inputs so that we can add them easily
;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
; both operands are finite, so now we need to figure out which is smaller
  dec a ;exponent of the second operand
  sub e ;exponent of the first operand
; If carry is set, then we need to negate A so that A is the number of bits to
; shift. If carry is reset, then we want to swap OP2 and OP1
; output exponent. Otherwise we need to shift OP1 A bits left and use the OP2
; exponent as the output
  jr c,f32add_negate
  ld d,b
  ld e,c
  pop ix  ; DEIX is now OP2
  pop bc
  pop hl  ; BCHL is now OP1
  jr f32add_swapped
f32add_negate:
  neg
  pop hl  ; BCHL is now OP2
  pop de
  pop ix  ; DEIX is now OP1
f32add_swapped:

; Before we do any more processing, let's compare the signs to figure out if
; we'll be adding or subtracting. Note that we can destroy the exponent of BCHL
; since we'll be using the exponent of DEIX for the result
  sla b
  ld b,a  ; number of bits to shift stored in B now
  ld a,d
  rra

  and %11000000
  push af ; If pe, then we add, if po, we subtract
; Before we shift CHL, we need to make the implicit bit an explicit 1
  set 7,c
; We'll use A as our overflow from shifting
  xor a
; If BC is 0, then we are done shifting
  inc b
  jr f32add_shift_start
f32add_shift_loop:
  srl c
  rr h
  rr l
  rra
f32add_shift_start:
  djnz f32add_shift_loop
  ld b,a  ; save the overflow

  pop af
  jp po, f32add_sub
f32add_add:
; add CHL.B to DEIX.0
  ld a,e
  add a,a
  ld a,d
  adc a,a ; A is the exponent, carry is sign
  push af ; save the carry
  ld d,a  ; exponent
  ld a,e
  or %10000000
  ; now do an integer add of the significands CHL.B + AIX.0
  push de
  push ix
  pop de
  add hl,de
  pop de
  adc a,c
  ;AHL.B is the significand
  jr nc,f32add_add_round
  inc d
  inc d
  jp z,f32add_return_inf2
  dec d
  rra
  rr h
  rr l
  .db $01 ; start of `ld bc,**`, eats the next two bytes of code
f32add_add_round:
  rl b
  jr f32add_output

f32add_sub:
; subtract CHL.B from DEIX.0
  ld a,e
  add a,a
  ld a,d
  adc a,a ; A is the exponent, carry is sign
  push af ; save the carry
  ld d,a  ; exponent
  set 7,e
  xor a
  sub b
  ld b,a
  ld a,e
  push de
  push ix
  pop de
  ex de,hl
  sbc hl,de
  pop de
  sbc a,c
  ld c,a
  ;CHL.B is the significand
  ; if there was a carry, then the sign of the output has changed and we need to
  ; perform the 2's complement of the significand
  jr nc,f32add_sub_negated
  pop af
  ccf
  push af
  xor a
  ld e,a \ sbc a,b \ ld b,a
  ld a,e \ sbc a,l \ ld l,a
  ld a,e \ sbc a,h \ ld h,a
  ld a,e \ sbc a,c \ ld c,a
f32add_sub_negated:
;now we need to re-normalize. Only the top bit of B matters.
;(note that if B had extra bits of the original significand, then we'd only have
; to normalize by at most 1 bit, and in the other case, B has at most one bit
; of the original mantissa anyways. So we only need the top bit of B.)

; for make sure that the significand is non-zero!
  ld a,b
  or c
  or h
  or l
  jr nz,f32add_sub_norm
  ld b,a
  pop af
  ex de,hl
  jr f32add_return_BCDE
f32add_sub_norm:
  ld a,c
  sla b
  inc a
  dec a
  jp m,f32add_output
f32add_sub_norm_loop:
  dec d
  jr z,f32add_output
  adc hl,hl
  adc a,a
f32add_sub_norm_start:
  jp p,f32add_sub_norm_loop
  ;now do rounding. If we normed, then we know B has no more bits from the
  ;original mantissa and so will be 0 (good) and so we can use the carry flag
  ;since that would be 0 here (from shifting a 0 out of C during the norm loop).
  ;Otherwise, we didn't norm and the carry flag still has the bit from B
f32add_output:
  ex de,hl  ;start getting ready to output the result
  ld b,h
  jr nc,f32add_rounded
  inc e
  jr nz,f32add_rounded
  inc d
  jr nz,f32add_rounded
  inc a
  jr nz,f32add_rounded
  inc b
f32add_rounded:
  add a,a
  ld c,a
  pop af
  rr b
  rr c
  jr f32add_return_BCDE





f32_add_op1_infnan:
;OP1 is finite here, so we know OP1 +- inf = +-inf and OP1 + NaN is NaN.
  pop de
  pop hl
  pop hl
  jr f32add_return_BCDE

f32_add_op1_0:
;OP1 is finite here, so we know OP1 + 0 = OP1
  ; pop off the 2 two bytes of OP2 that are on the stack
  pop bc
  ; now pop off OP1 into BCDE
  pop bc
  pop de
f32add_return_BCDE:
  ; now pop off the pointer to the output
  pop hl
  ; write BCDE to our output
  ld (hl),e
  inc hl
  ld (hl),d
  inc hl
  ld (hl),c
  inc hl
  ld (hl),b
  ret

  ret

f32_add_0_op2:
;We can just return OP2. The only "weird" case is (+-0) + (+-0) ==> +0
  ; pop off the bottom two bytes of the first operand
  pop bc
  ; now pop the pointer to the output into DE, then write
  pop de
  ldi
  ldi
  ; we need to check for -0, so read in the exponent into A
  ld a,(hl)
  add a,a
  ldi
  ld a,(hl)
  ld (de),a
  adc a,a
  ret nz
  ;the operand is 0, so we need to set the sign to be positive and exponent of 0
  ;this ensures [-0 + 0 ==> +0] and [0 + -0 ==> +0]
  ld (de),a
  ret

f32_add_infnan_op2:
;Cases to consider:
;  NaN + op2     ==> NaN
;  inf + -inf    ==> NaN
; -inf +  inf    ==> NaN
;  inf + finite  ==> inf
;  inf +  inf    ==> inf

  ; pop the bottom two bytes into DE so that we can determine if we are working
  ; with inf or NaN
  pop de
  ; If we have inf, then CDE = 0x800000, else it is NaN
  ld a,c
  add a,a
  or d
  or e
  jr nz, f32add_return_BCDE  ;return NaN

;We are adding +-inf to OP2, so now we need to check OP2 for inf/nan
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  ld c,(hl)
  inc hl
  ld h,(hl)

;HCDE is OP2, B has the sign for OP1
  ld a,c
  add a,a
  ld a,h
  adc a,a
  jr z,f32_add_return_inf
  inc a
  jr nz,f32_add_return_inf
; we are adding an inf to an inf or a NaN
; if the sign bits don't match (even if OP2 is NaN), return NaN
  ld a,h
  xor b
  jp m,f32_add_return_NaN
; If OP2 is NaN, return NaN
  ld a,c
  add a,a
  or d
  or e
  ; If the z flag is set, then we are adding infs of the same sign, so return
  ; BCDE as the float
  jr z,f32add_return_BCDE
;otherwise we are adding infs of differing signs so return NaN
f32_add_return_NaN:
  ld c,-1
  ld d,c
  ld e,c
  jr f32add_return_BCDE

f32add_return_inf2:
  pop af
  ld b,-1
  rr b
f32_add_return_inf:
; Use B as it has the sign and upper 7 bits of the correct inf.
  ld c,80h
  ld de,0
  jr f32add_return_BCDE


#endif
