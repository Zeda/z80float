# z80float
z80float is a floating point library targeting the Z80 processor. While this
project is tested on a TI-84+, the code should be generic enough to run on any
Z80 CPU with very little modification (mostly defining scrap RAM locations).

## Supported Formats

These have a complete library of routines including the basic 5 functions
(+, -, *, /, squareroot) as well as trigonometric functions
(sine/cosine/tangent), inverse trig functions (arcsine, arccosine, arctangent),
hyperbolic functions (sinh/cosh/tanh), inverse hyperbolics functions,
logarithms, exponentials, comparison, and `rand`:

* **[f24](f24)** - These are 24-bit floats modeled after IEEE-754 binary32,
  removing one exponent bit and 7 significand bits. These are well-suited to the
  Z80-- the operands can be passed via registers allowing the routines to have a
  small memory and CPU-time footprint, while still having 5 digits of precision.
  **NOTE:** `f24toa` converts an `f24` float to a string that can be displayed.
  This is found in the [conversion](conversion) folder.

* **[f32](f32)** - an IEEE-754 binary32 format (the classic "single")
  * **NOTE:** `f32toa` converts an f32 float to a string that can be displayed.
  This is found in the [conversion](conversion) folder.

* **[single](single)** - this is poorly named. This was my own 32-bit float
  format. It can represent all IEEE-754 `binary32` numbers, but the layout of
  the bits is different (keeping all exponent bits in one byte) and represents
  0/inf/NaN differently allowing slightly more numbers to be represented.

* **[extended](extended)** - These are 80-bit floats providing 19-digits
  precision. These are quite fast all things considered-- My TI-84+'s TI-OS
  takes over 85000 clock cycles to calculate a square root to 14 digits
  precision, compared to 6500cc for xsqrt (that's 13 times faster). Most other
  routines aren't that extreme, but they are generally pretty fast compared to
  the TI-OS routines. To be fair, TI's floats are BCD, so clunkier to work with.

Future ideas:
* [ ] **f64** - an IEEE-754 binary64 format (the classic "double")
  * note that in the [conversion](conversion) folder there are routines
    `f64tox.z80` and `xtof64.z80` in case you need to support the binary64
    format. This might end up being how most `f64` routines are implemented, at
    least early on.

* [ ] **f16** - The binary16 format. Although I might opt to work on
  [DW0RKiN's library](https://github.com/DW0RKiN/Floating-point-Library-for-Z80)
  instead. Their's has a bunch of 16-bit float implementations including
  binary16.

* [ ] **BCD floats** - Might be useful for calculators as these use base-10.

* [ ] **base10** floats - encoding 3 digits in 10 bits. It has the advantage of
  BCD in that it is quick to convert to and from base-10 representation, but it
  can take advantage of more base-2 arithmetic since 1000 is close to a power of
  2 (2^10 = 1024) and it can pack more digits into a smaller space than BCD (10
  bits for 3 digits instead of 12).

## Building
The compiler that I've been using for this project is
[spasm-ng](https://github.com/alberthdev/spasm-ng) which has its share of syntax
quirks. In the future, I might migrate to
[fasmg](https://flatassembler.net/docs.php?article=fasmg) using jacobly's
[Z80 includes](https://github.com/jacobly0/fasmg-z80) (they also have
[ez80 includes](https://github.com/jacobly0/fasmg-z80)).

I've set up z80float so that when you `#include` a file, it `#includes` any
dependencies that have yet to be included. For example, if you want to use
`xatan`, then `#include "xatan.z80"` will include all of the following files (if
they haven't already been included) in the following order. Note that some
routines are shared and so I am omitting multiplicities:
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
**In order for this to work**, you will need to add the format's root directory
(i.e. `extended` or `single`) to your assembler's default search path.
**You will also need to add the `common` folder to your compiler's search path!.**

With [spasm-ng](https://github.com/alberthdev/spasm-ng), I use its `-I` flag.
For example:

```
spasm foo.z80 foo.8xp -I bar/z80float/common -I bar/z80float/extended
```

## General Syntax

***NOTE:*** *The following does not apply to the 24-bit floats. View
[the readme](f24/readme.md) for f24 documentation if you want to use them!*

The calling syntax for the single- and extended-precision float routines are:
```
    HL points to the first operand
    DE points to the second operand (if needed)
    IX points to the third operand (if needed, rare)
    BC points to where the result should be output
```
In all cases unless specifically noted, registers are preserved on input and
output. Notable exceptions are the comparison routines such as `xcmp` and
`cmpSingle`.

Subroutines, like `mul16`, do not preserve registers.

## Examples
In general, the extended precision routines are prefixed with an `x`. For
example, `xmul` is the extended precision multiplication routine. The single
precision floats generally have a suffix of `Single`, as in `mulSingle`.

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

Extended precision floats are stored as 8 little-endian bytes for the
(normalized) mantissa, then a 16-bit word with the upper bit being sign, and the
lower 15 bits as the exponent. The exponent is biased such that 0x4000
corresponds to an exponent of 0. Special numbers are represented with an
exponent of `-0x4000` (physical value `0x0000`). The sign bit still indicates
sign, and the top two bits of the mantissa represent the specific special
number:
```
    0 is represented with %00
    inf is represented with %11
    NaN is represented with %01
```

The [/tools](/tools) folder has a Python program to convert numbers into the
extended-precision format that this library uses. Pass the space delimited
numbers on the command line and it will print out the number(s) in `.db` format.
For example:
```
zeda@zeda:~/z80float/tools$ python extended.py 1.2 1337
.db $9A,$99,$99,$99,$99,$99,$99,$99,$00,$40    ;1.2
.db $00,$00,$00,$00,$00,$00,$20,$A7,$0A,$40    ;1337
```

---
## Single Precision Floats

Single precision floats are stored as a 24-bit little-endian mantissa, with the
top bit being an implicit `1`. The actual top bit represents the sign. After
that is an 8-bit exponent with a bias of `+128`. Special values are stored with
an exponent of `-128` (physical value being `0x00`). The mantissa requires the
top three bits to contain specific values:
```
    +0 is represented as 0x00
    -0 is represented as 0x80
    +inf is represented as 0x40
    -inf is represented as 0xC0
    NaN is represented as 0x20
```

As with the extended-precision floats, the [/tools](/tools) folder has a Python
program to convert numbers into the single-precision format that this library
uses. For example:
```
zeda@zeda:~/z80float/tools$ python single.py 1.2 1337
.db $9A,$99,$19,$80  ;1.2
.db $00,$20,$27,$8A  ;1337
```
