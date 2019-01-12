;single.inc
#ifndef scrap
#define scrap 8000h
#endif
curKey  =80F6h
keyCount=80F7h
seed1_0 =80F8h
seed1_1 =80FAh
seed2_0 =80FCh
seed2_1 =80FEh
hyperout=scrap+9
hyperout2=scrap+13

.echo "===Math:",$-math_single

gbuf        = 9340h
_VPutS      = 4561h
_VPutMap    = 455Eh
_GrBufCpy   = 486Ah
_InvertRect = 4D5Fh
penCol      = 86D7h
penRow      = 86D8h
sGrFlags    = 14h
textWrite   = 7
flags       =89F0h
