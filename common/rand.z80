#ifndef included_rand
#define included_rand

rand:
; Output is in HL
; This rand routine combines Patrik Rak's fantastic 32-bit xorshift
; (https://gist.github.com/raxoft/c074743ea3f926db0037) with a simple lcg for
; extra smoothing.
; It has a period of 281,474,976,645,120 (2^48-2^16) and uses 48 bits of state.
; 42 bytes
; 210cc
  ld hl,(seed0)
  ld b,h
  ld c,l
  add hl,hl
  add hl,hl
  inc l
  add hl,bc
  ld (seed0),hl

; xorshift
  ld hl,(seed1)     ; yw -> zt
  ld de,(seed1+2)   ; xz -> yw
  ld (seed1+2),hl   ; x = y, z = w
  ld a,l            ; w = w ^ ( w << 3 )
  add a,a
  add a,a
  add a,a
  xor l
  ld l,a
  ld a,d         ; t = x ^ (x << 1)
  add a,a
  xor d
  ld h,a
  rra            ; t = t ^ (t >> 1) ^ w
  xor h
  xor l
  ld h,e         ; y = z
  ld l,a         ; w = t
  ld (seed1),hl

; Mix the xorshift and the lcg
  add hl,bc
  ret
#endif
