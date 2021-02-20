;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
; These are the operations we'll be testing
;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
op_LUT:
  .db 2
  .dw str_add, f32add, f32toa, add_op1_LUT, add_op2_LUT
  .dw str_mul, xmul, xtostr, xadd_op1_LUT, xadd_op2_LUT


;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
; Operations
;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
str_add:
  .db "+", 0

str_mul:
  .db "*", 0

add_op2_LUT:
add_op1_LUT:
  .db 7
  .dw str_pi,   f32_const_pi
  .dw str_2pi,  f32_const_2pi
  .dw str_0,    f32_const_0
  .dw str_1,    f32_const_1
  .dw str_NaN,  f32_const_NaN
  .dw str_inf,  f32_const_inf
  .dw str_ninf, f32_const_ninf

xadd_op2_LUT:
xadd_op1_LUT:
  .db 7
  .dw str_pi,   xconst_pi
  .dw str_2pi,  xconst_2pi
  .dw str_0,    xconst_0
  .dw str_1,    xconst_1
  .dw str_NaN,  xconst_NaN
  .dw str_inf,  xconst_inf
  .dw str_ninf, xconst_ninf

;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
; op1 and op2 strings
;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
str_pi:
  .db "pi", 0
str_2pi:
  .db "2pi", 0
str_0:
  .db "0", 0
str_1:
  .db "1", 0
; str_NaN:
;   .db "NaN", 0
; str_inf:
;   .db "inf", 0
str_ninf:
  .db "-inf", 0


;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
; Include files for testing
;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;:;;
#include "float.inc"
#include "xconst.z80"
#include "xtostr.z80"
#include "xmul.z80"
f32:
#include "f32const.z80"
#include "f32toa.z80"
#include "f32add.z80"
; .echo "f32: ", $-f32," bytes"
