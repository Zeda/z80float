# z80float
z80float is a floating point library targeting the Z80 processor. While the project is tested on a TI-84+, the code should be generic enough to run on any Z80 CPU with very little modification (mostly defining scrap RAM locations).

## Building
z80float is set up so that if you include a file, it includes all of its dependencies. For example, if you want to use xatan, `#include "xatan.z80"` will include all of the following files (if they haven't already been included) in the following order. Note that some routines are shared and so I am omitting multiplicities:
```
xatan.z80
  routines/pushpop.z80
  constantsx.z80
  xmul.z80
    routines/mov.z80
    mul/mul64.z80
      mul/mul32.z80
        mul/mul16.z80
    routines/rl64.z80
  xadd.z80
    routines/swapxOP2xOP3.z80
    routines/sub64.z80
    routines/add64.z80
  xsqrt.z80
    routines/srl64.z80"
    sqrt/sqrt64.z80"
      sqrt/sqrt32.z80"
        sqrt/sqrtHLIX.z80
          sqrt/sqrt16.z80
        div/div32_16.z80
      div/div32.z80"
  xbg.z80
    mul/xmul11.z80
      routines/addmantissa0102.z80
      mul/xmul3.z80
        routines/rl64.z80
    mul/xmul13.z80
    mul/xmul31.z80
      routines/srl64_x4.z80
      routines/normalizexOP1.z80
    mul/xmul7.z80
    mul/xmul17.z80
    mul/xmul15.z80
    mul/xmul5.z80
    xsub.z80
    xdiv.z80
      div/div64.z80
        div/div64_32.z80
      routines/cmp64.z80
    xamean.z80
    xgeomean.z80  
```
**In order for this to work**, you will need to add the `single` and/or `extended` directory to your assembler's default search path.

I use [spasm-ng](https://github.com/alberthdev/spasm-ng) with its `-I` flag. For example:

```
spasm foo.z80 foo.8xp -I bar/z80float/extended```

## General Syntax
The calling syntax for the single- and extended-precision float routines are:
```
    HL points to the first operand
    DE points to the second operand (if needed)
    IX points to the third operand (if needed, rare)
    BC points to where the result should be output
```
In all cases unless specifically noted, registers are preserved on input and output. Notable exceptions are the comparison routines, `xcmp` and `cmpSingle`.

Subroutines, like `mul16`, do not preserve registers.

## Examples
In general, the extended precision routines are prefixed with an `x`. For example, `xmul` is the extended precision multiplication routine. The single precision floats generally have a suffix of `Single`, as in `mulSingle`.

To evaluate `log_2(pi^e)` with extended-precision floats you could do:
```
  ;first do pi^e and store it to temp mem, xOP1
  ld hl,xconst_pi
  ld de,xconst_e
  ld bc,xOP1
  call xpow

  ;Now BC points to xOP1, and we want to compute log_2
  ;Need to put the pointer into HL, so do BC --> HL
  ;Store back to xOP1, so don't change BC. DE isn't used.
  ld h,b
  ld l,c
  call xlg
```

For single-precision:
```
  ;first do pi^e and store it to temp mem, scrap
  ld hl,const_pi
  ld de,const_e
  ld bc,scrap
  call powSingle

  ;Now BC points to scrap, and we want to compute log_2
  ;Need to put the pointer into HL, so do BC --> HL
  ;Store back to scrap, so don't change BC. DE isn't used.
  ld h,b
  ld l,c
  call lgSingle
```



---
# Formats
## Extended Precision Floats

Extended precision floats are stored as 8 little-endian bytes for the (normalized) mantissa, then a 16-bit word with the upper bit being sign, and the lower 15 bits as the exponent. The exponent is biased such that 0x4000 corresponds to an exponent of 0. Special numbers are represented with an exponent of `-0x4000` (physical value `0x0000`). The sign bit still indicates sign, and the top two bits of the mantissa represent the specific special number:
```
    0 is represented with %00
    inf is represented with %11
    NaN is represented with %01
```

The [/tools](/tools) folder has a Python program to convert numbers into the extended-precision format that this library uses. Pass the space delimited numbers on the command line and it will print out the number(s) in `.db` format. For example:
```
zeda@zeda:~/z80float/tools$ python extended.py 1.2 1337
.db $9A,$99,$99,$99,$99,$99,$99,$99,$00,$40    ;1.2
.db $00,$00,$00,$00,$00,$00,$20,$A7,$0A,$40    ;1337
```

---
## Single Precision Floats

Single precision floats are stored as a 24-bit little-endian mantissa, with the top bit being an implicit `1`. The actual top bit represents the sign. After that is an 8-bit exponent with a bias of `+128`. Special values are stored with an exponent of `-128` (physical value being `0x00`). The mantissa requires the top three bits to contain specific values:
```
    +0 is represented as 0x00
    -0 is represented as 0x80
    +inf is represented as 0x40
    -inf is represented as 0xC0
    NaN is represented as 0x20
```

As with the extended-precision floats, the [/tools](/tools) folder has a Python program to convert numbers into the single-precision format that this library uses. For example:
```
zeda@zeda:~/z80float/tools$ python single.py 1.2 1337
.db $9A,$99,$19,$80  ;1.2
.db $00,$20,$27,$8A  ;1337
```
