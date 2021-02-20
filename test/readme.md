# z80float Tester
This tester tests binary operators. To create a test, edit [testbinop.z80](testbinop.z80). It is created for use on the TI-83+/84+.

The first portion of this file defines the operators you want to test.
For example, it might look like to test `f32add` and `xmul`

```
op_LUT:
  .db 2
  .dw str_add, f32add, f32toa, add_op1_LUT, add_op2_LUT
  .dw str_mul, xmul, xtostr, xadd_op1_LUT, xadd_op2_LUT
```

The `.db 2` means we are testing two operations.
The subsequent lines are pointers to data in the following format:

```
  .dw op_string, op_call, to_string, OP1_LUT, OP2_LUT
```

* `op_string` might look like this (using the example):

        str_add:
          .db "+", 0

        str_mul:
          .db "*", 0

* `op_call` is the call that performs the operation
* `to_string` is the call that converts the result float to a string
* `OP1_LUT` and `OP2_LUT` are pointers to tables of operands. In the example,
  this might be:

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

        str_pi:
          .db "pi", 0
        str_2pi:
          .db "2pi", 0
        str_0:
          .db "0", 0
        str_1:
          .db "1", 0
        str_NaN:
          .db "NaN", 0
        str_inf:
          .db "inf", 0
        str_ninf:
          .db "-inf", 0

 In this case, we are using the same set of operands for both the first and
 second operand, so both pointers point to the same LUT.

Finally, you'll need to `include` any of the routines that you are using.

## Compiling
The [compile](compile) script gives an example command for compiling using
[spasm-ng](https://github.com/alberthdev/spasm-ng). You navigate to this `test`
folder and run something like:

        spasm tester.z80 tester.8xp -I ../f32 -I ../f24 -I ../conversion -I ../single -I ../extended

## Using
Send the resultant `tester.8xp` to your TI-83+/84+ (monochrome variants only),
and run `Asm(prgmTESTER` from the homescreen. It will loop through each
combination of OP1 and OP2 for each operator, pausing after each "page." You can
press `[ON]` to exit when it is paused waiting for the user to press `[Enter]`.
