#define char_TI_TOK
#define bcall(x) rst 28h \ .dw x
#include "f32.inc"

_VPutS        = 4561h
_VPutMap      = 455Eh
_GrBufCpy     = 486Ah
_GetKeyRetOff = 500Bh
penCol        = 86D7h
penRow        = 86D8h
sGrFlags      = 14h
textWrite     =  7
fontFlags     = 32h
fracDrawLFont =  2
_GrBufClr     = 4BD0h
onFlags       = 9h	;on key flags
onInterrupt   = 4		;1=on key interrupt request

.db $BB,$6D
.org $9D95

  ld hl,op_LUT

tester:
  res fracDrawLFont,(iy + fontFlags)
  set textWrite,(iy + sGrFlags)

  ld a,(hl)
  ld (num_ops),a
ops_loop:
  ld (op_counter),a
  inc hl
  ld c,(hl)
  inc hl
  ld b,(hl)
  ld (opstr), bc
  inc hl
  ld c,(hl)
  inc hl
  ld b,(hl)
  ld (opcall), bc
  inc hl
  ld c,(hl)
  inc hl
  ld b,(hl)
  ld (tostr), bc
  inc hl
  ld c,(hl)
  inc hl
  ld b,(hl)
  ld (op1_LUT), bc
  inc hl
  ld c,(hl)
  inc hl
  ld b,(hl)
  ld (op2_LUT), bc

  push hl
  call test_op
  pop hl
  jr nz,end_test

  ld a,(op_counter)
  dec a
  jr nz, ops_loop
end_test:
  set fracDrawLFont,(iy + fontFlags)
  res textWrite,(iy + sGrFlags)
  ret

test_op:
  ld hl,(op1_LUT)
  ld a,(hl)
  ld (num_pages),a
  inc hl
op1_loop:
  ld (op1_counter), a
  push hl
  ; clear the screen and reset the pen coords
  bcall(_GrBufClr)
  ld hl,0
  ld (penCol),hl
  pop hl

  ;get the string to display for the first operand
  ld e,(hl)
  inc hl
  ld d,(hl)
  inc hl
  push hl
  ex de,hl
  bcall(_VPutS)
  ; draw the operator
  ld hl,(opstr)
  bcall(_VPutS)

  pop hl
  ; save the second operand pointer
  ld de,op1_ptr
  ldi
  ldi
  push hl
  call test_op2
  call pause
  pop hl
  ret nz
  ld a, (op1_counter)
  dec a
  jr nz,op1_loop
  ret

test_op2:
  ld hl,(op2_LUT)
  ld b,(hl)
op2_loop:
  push bc
  ;get the string to display for the first operand
  inc hl
  ld e,(hl)
  inc hl
  ld d,(hl)
  ex de,hl
  ; we'll hold on to the column to restore after
  ld a,(penCol)
  push af ; penCol
  push de
  bcall(_VPutS)
  ld a,32
  ld (penCol),a
  ld a,'='
  bcall(_VPutMap)

  pop hl
  ; get the pointer to op2
  inc hl
  ld e,(hl)
  inc hl
  ld d,(hl)
  push hl ;save HL for later
  ld hl,(op1_ptr)
  ld bc,8800h
  ld ix,(opcall)
  call call_ix
  ld h,b
  ld l,c
  ld bc,8000h
  ld ix,(tostr)
  call call_ix
  ld h,b
  ld l,c
  bcall(_VPutS)
  pop hl
  pop af
  ld (penCol),a
  ld a,(penRow)
  add a,6
  ld (penRow),a
  pop bc
  djnz op2_loop
  ret

pause:
  ld hl,3600h
  ld (penCol),hl
  ld hl,s_press_enter
  bcall(_VPutS)

  ld a,(num_pages)
  ld hl,(op1_counter)
  call out_of

  ld hl,s_ops
  bcall(_VPutS)

  ld a,(num_ops)
  ld hl,(op_counter)
  call out_of


  bcall(_GrBufCpy)
  bcall(_GetKeyRetOff)
  ; check if ON was pressed
  bit onInterrupt, (iy+onFlags)
  res onInterrupt, (iy+onFlags)
  ret

out_of:
  push af
  sub l
  inc a
  ld hl,8000h
  call uitoa_8
  bcall(_VPutS)
  ld a,'/'
  bcall(_VPutMap)
  pop af
  ld hl,8000h
  call uitoa_8
  bcall(_VPutS)
  ret

s_press_enter:
  .db "Press Enter  ", 0
s_ops:
  .db ", op ", 0

call_ix:
  jp (ix)

#include "uitoa_8.z80"

;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
; Variables used by the tester
;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
op_counter:
  .db 0
num_ops:
  .db 0
op1_counter:
  .db 0
num_pages:
  .db 0
op1_ptr:
  .dw 0
opcall:
  .dw f32add
opstr:
  .dw 0
tostr:
  .dw f32toa
op1_LUT:
  .dw 0
op2_LUT:
  .dw 0


#include "testbinop.z80"

.echo "Full test:", $-$9D95," bytes"
