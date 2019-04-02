#define bcall(x) rst 28h \ .dw x
xOP1 = 86FCh
xOP2 = xOP1+10
xOP3 = xOP1+20
xOP4 = xOP1+30
xOP5 = xOP1+40
#define seed0 80F8h
#define seed1 80FCh
#define addx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xadd
#define subx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xsub
#define rsubx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xrsub
#define mulx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xmul
#define divx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xdiv
#define sqrtx(o1,d) ld hl,o1 \ ld bc,d \ call xsqrt
#define strx(o1,d) ld hl,o1 \ ld bc,d \ call xtostr
#macro dec_hl_opt(x)
#if (x&255)>0
  dec l
#else
  dec hl
#endif
#endmacro
#macro inc_hl_opt(x)
#if (x&255)<255
  inc l
#else
  inc hl
#endif
#endmacro
#define test(x,y,s) call testputs \ .db s,0 \ ld hl,x \ ld de,y \ call subtest
penCol    = 86D7h
penRow    = 86D8h
_VPutS    = 4561h
fontFlags     = 32h
fracDrawLFont = 2
sGrFlags      = 14h
textWrite     = 7
_GrBufClr     = 4BD0h
_GrBufCpy     = 486Ah
_PutS         = 450Ah
#define inc_FMA
#define char_TI_TOK
.db $BB,$6D
.org $9D95
  bcall(_GrBufClr)
  res fracDrawLFont,(iy + fontFlags)
  set textWrite, (IY + sGrFlags)
  ld hl,0
  ld (penCol),hl
  call randinit
_:
  ld hl,str_num
  ld bc,xOP1
  call strtox
  call testputs
  .db "Float "
str_num:
  .db ".1234",0
  ld hl,xOP1
  ld b,h
  ld c,l
  call xtostr
  ld h,b
  ld l,c
  call puts
  rsubx(xconst_pi,xconst_e,xOP4)
  call testputs \ .db "(e-pi)=",0
  strx(xOP4,xOP1)
  ld h,b
  ld l,c
  call puts
  ld hl,xconst_pi
  ld bc,xOP1
  call xmul11
  call testputs \ .db "11pi=",0
  strx(xOP1,xOP1)
  ld h,b
  ld l,c
  call puts
  ld hl,xconst_pi
  ld de,xconst_10
  ld bc,xOP1
  call xmul7
  call testputs \ .db "7pi=",0
  strx(xOP1,xOP1)
  ld h,b
  ld l,c
  call puts
  ld hl,xconst_e
  ld bc,xOP1
  call xcos
  call testputs \ .db "cos(e)=",0
  strx(xOP1,xOP1)
  ld h,b
  ld l,c
  call puts
  bcall(_GrBufCpy)
  ret
xconst_1p3:
  .db $00,$00,$00,$00,$00,$D9,$B0,$C9 \ .dw $4000
subtest:
  ld bc,8000h
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex \ inc hl \ inc de
  ld a,(de) \ xor (hl) \ call tohex
  xor a
  ld (bc),a
  ld l,a
  ld h,b
  bcall(_VPutS)
  ld hl,(penCol)
  ld l,0
  ld a,6
  add a,h
  ld h,a
  ld (penCol),hl
  ret
tohex:
  push af
  and $0F
  add a,'0'
  cp $3A
  jr c,$+4
  add a,7
  ld (bc),a
  inc bc
  pop af
  rrca
  rrca
  rrca
  rrca
  and $0F
  add a,'0'
  cp $3A
  jr c,$+4
  add a,7
  ld (bc),a
  inc bc
  ret
testputs:
  ex (sp),hl
  call puts
  ex (sp),hl
  ret
puts:
  push de
  push bc
  push af
  bcall(_VPutS)
  ex de,hl
  ld hl,(penCol)
  ld l,0
  ld a,6
  add a,h
  ld h,a
  ld (penCol),hl
  ex de,hl
  pop af
  pop bc
  pop de
  ret
#ifndef included_xneg
#define included_xneg
#ifdef ZAPP
#ifndef included_pushpop
#define included_pushpop
pushpop:
  ex (sp),hl
  push de
  push bc
  push af
  push hl
  ld hl,pushpopret
  ex (sp),hl
  push hl
  push af
  ld hl,12
  add hl,sp
  ld a,(hl)
  inc hl
  ld h,(hl)
  ld l,a
  pop af
  ret
pushpopret:
  pop af
  pop bc
  pop de
  pop hl
  ret
#endif
#ifndef included_mov10
#define included_mov10
#define included_mov4
mov10:
  ldi
mov9:
  ldi
mov8:
  ldi
mov7:
  ldi
mov6:
  ldi
mov5:
  ldi
mov4:
  ldi
  ldi
  ldi
  ldi
  ret
#endif
#endif
xneg:
  call pushpop
  ld d,b
  ld e,c
  call mov9
  ld a,(hl)
  xor 80h
  ld (de),a
  ret
#endif
randinit:
  ld a,r
  ld hl,seed0
  xor (hl) \ ld (hl),a \ inc hl
  xor (hl) \ ld (hl),a \ inc hl
  xor (hl) \ ld (hl),a \ inc hl
  xor (hl) \ ld (hl),a \ inc hl
  xor (hl) \ ld (hl),a \ inc hl
  xor (hl) \ ld (hl),a \ inc hl
  xor (hl) \ ld (hl),a \ inc hl
  or 97
  or (hl) \ ld (hl),a
  ret
rand:
  ld hl,(seed0)
  ld de,(seed0+2)
  ld b,h
  ld c,l
  add hl,hl \ rl e \ rl d
  add hl,hl \ rl e \ rl d
  inc l
  add hl,bc
  ld (seed0),hl
  ld hl,(seed0+2)
  adc hl,de
  ld (seed0+2),hl
  ex de,hl
  ld hl,(seed1)
  ld bc,(seed1+2)
  add hl,hl \ rl c \ rl b
  ld (seed1+2),bc
  sbc a,a
  and %11000101
  xor l
  ld l,a
  ld (seed1),hl
  ex de,hl
  add hl,bc
  ret
.echo "Total: ",$-$9D95
start_xconst:
xconst_pi:
  .db $35,$C2,$68,$21,$a2,$da,$0f,$c9 \ .dw $4001
xconst_e:
  .db $9B,$4a,$bb,$a2,$58,$54,$f8,$ad \ .dw $4001
xconst_lg_e:
  .db $bC,$f0,$17,$5c,$29,$3b,$aa,$b8 \ .dw $4000
xconst_ln_2:
  .db $aC,$79,$cf,$d1,$f7,$17,$72,$b1 \ .dw $3FFF
xconst_log10_2:
  .db $99,$F7,$CF,$FB,$84,$9A,$20,$9A \ .dw $3FFE
xconst_lg_10:
  .db $FE,$8A,$1B,$CD,$4B,$78,$9A,$D4 \ .dw $4001
xconst_0:
  .db $00,$00,$00,$00,$00,$00,$00,$00 \ .dw $0000
xconst_1:
  .db $00,$00,$00,$00,$00,$00,$00,$80 \ .dw $4000
xconst_INF:
  .db $00,$00,$00,$00,$00,$00,$00,$C0 \ .dw $0000
xconst_nINF:
  .db $00,$00,$00,$00,$00,$00,$00,$C0 \ .dw $8000
xconst_NaN:
  .db $00,$00,$00,$00,$00,$00,$00,$40 \ .dw $0000
xconst_log10_e:
  .db $95,$71,$28,$37,$A9,$D8,$5B,$DE,$FE,$3F
xconst_2pi:
  .db $35,$C2,$68,$21,$a2,$da,$0f,$c9 \ .dw $4002
xconst_2pi_inv:
  .db $2A,$15,$44,$4E,$6E,$83,$F9,$A2,$FD,$3F
xconst_p5:
  .db $00,$00,$00,$00,$00,$00,$00,$80 \ .dw $3FFF
xconst_p25:
  .db $00,$00,$00,$00,$00,$00,$00,$80 \ .dw $3FFE
xconst_sqrt_2:
  .db $0F,$6D,$DE,$F9,$33,$F3,$04,$B5 \ .dw $4000
end_xconst:
xconst_3028466566125:
  .db $00,$00,$40,$FB,$20,$AB,$47,$B0 \ .dw $4029
