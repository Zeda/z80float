#define addi(x,y)	ld hl,x \ ld de,y \ call FloatAdd_80
#define subt(x,y)	ld hl,x \ ld de,y \ call FloatSub_80
#define rsub(x,y)	ld hl,y \ ld de,x \ call FloatSub_80
#define mult(x,y)	ld hl,x \ ld de,y \ call FloatMul_80
#define divi(x,y)	ld hl,x \ ld de,y \ call FloatDiv_80
#define sqrt(x)		ld hl,x \ call FloatSqrt_80
#define copy(x,y)	ld hl,x \ ld de,y \ call from_to
;fpOP1 = 8000h
;fpOP2 = 800Eh
;fpOP3 = 801Ch
;fpOP4 = 802Ah
;fpOP5 = 8038h
fpOP1 = 8000h
fpOP2 = 800Ah
fpOP3 = 8014h
fpOP4 = 801Eh
fpOP5 = 8028h

fpAns = 8054h
Ans   = fpAns 
temp1 = 8062h
StringOutp = 8070h
#ifdef Karatsuba
word64_1	= fpOP1+4	;8 bytes
word64_2	= fpOP2+4	;8 bytes
outp128		= 8070h		;16 bytes
word32_1	= outp128+16	;4 bytes
word32_2	= word32_1+4	;4 bytes
outp64		= word32_2+4	;8 bytes	;48 bytes total
outp		= outp64
floatStackPtr	= outp+8	;8090h
#else
floatStackPtr	= 8070h
#endif
