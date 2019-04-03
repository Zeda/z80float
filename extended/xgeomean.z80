#ifndef included_xgeomean
#define included_xgeomean
#include "xmul.z80"
#include "xsqrt.z80"

#if 1=1
xgeomean:
;Input:
;  HL points to one number
;  DE points to anothers
;104+xmul+xsqrt
;avg: 16573.025
  push hl
  push bc
  ld bc,xOP1
  call xmul
  ld h,b
  ld l,c
  pop bc
  call xsqrt
  pop hl
  ret



#else
xgeomean:
;Input:
;  HL points to x
;  DE points to y
;Returns sqrt(x*y)
;104+xmul+xsqrt   ;Needs to be corrected
;avg: 16573.025

  call pushpop
  push bc
;Multiply x and y. This can cause an overflow or underflow, though, so we'll need to adjust the exponent! (The "correct" implmentation of geomean never underflows or overflows.)
  push de
  ld de,xOP1
  call mov10
  pop hl
  call mov10
	ld hl,(xOP1+8)
	ld de,(xOP2+8)
  res 7,h
  res 7,d
  add hl,de
  ld a,h
  rra
  rr l
  sub $40
  ld h,a

;Save the adjustment for later
  ex (sp),hl
  push hl

; Now we set the new exponents
  ld hl,$4000
  ld d,h
  ld e,l
  ld (xOP2+8),hl
;If carry is set, 2nd exponent needs to be incremented
  rl l
  ld (xOP1+8),hl

;Now actually multiply
  call xmul_stepin_geomean

;Now get the square root
  ld hl,var_z+8
  pop bc
  call xsqrt

; Now we need to adjust the exponent
  ld hl,8
  add hl,bc
  pop bc
  ld e,(hl)
  inc hl
  ld d,(hl)
  ex de,hl
  add hl,bc
  ex de,hl
  ld (hl),d
  dec hl
  ld (hl),e
  ret
#endif
#endif
