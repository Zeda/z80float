fpOP1 = 8000h
fpOP2 = 800Ah
fpOP3 = 8014h
fpOP4 = 801Eh
fpOP5 = 8028h
seed0 = 80F8h
seed1 = 80FCh

#define addx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xadd
#define subx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xsub
#define rsubx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xrsub
#define mulx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xmul
#define divx(o1,o2,d) ld hl,o1 \ ld de,o2 \ ld bc,d \ call xdiv
#define sqrtx(o1,d) ld hl,o1 \ ld bc,d \ call xsqrt
#define strx(o1,d) ld hl,o1 \ ld bc,d \ call xtostr
