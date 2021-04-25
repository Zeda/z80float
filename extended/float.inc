#ifndef included_x_float.inc
#define included_x_float.inc
; Equates
xOP1 = 8000h
xOP2 = xOP1+10
xOP3 = xOP1+20
xOP4 = xOP1+30
xOP5 = xOP1+40
#define seed0 80F8h
#define seed1 80FCh

; Defines
#define addx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xadd
#define subx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xsub
#define rsubx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xrsub
#define mulx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xmul
#define divx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xdiv
#define sqrtx(o1,d) ld hl,o1 \ ld bc,d \ call xsqrt
#define strx(o1,d) ld hl,o1 \ ld bc,d \ call xtostr
#define movx(src,dest)  ld hl,src \ ld de,dest \ call mov10

; Macros
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

#endif
