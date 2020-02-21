# f24
These routines are for a non-standard 24-bit float format. While there is a
standard for `binary16` and `binary32`, there is not one for 24-bit floats.
This does give me some artistic liberties, but I tried to be sensible :)

## Format
The format I went with has 1 bit for the sign and 7 bits for the exponent, and
these are packed into a byte. The significand is 17 bits, but the top bit
is treated as an implicit `1`, and so it is actually encoded as a 16-bit word.

## Special values (0, inf, NaN)
The exponent has a bias of `+63`, or `0b0111111` in binary. `0` is encoded as an
exponent of `-63`, regardless of the significand. `inf` is encoded as `2^64`,
and `NaN` is encoded as `2^64*1.x` where `x` is any non-zero value.

## Example values
Example values:
```
              s eeeeeee mmmmmmmmmmmmmmmm
2.16841e-19   0 0000001 0000000000000000  smallest representable positive number
1.84466e19    0 1111110 1111111111111111  largest representable positive number
1.0           0 0111111 0000000000000000
2.0           0 1000000 0000000000000000
-1.0          1 0111111 0000000000000000
-0.5          1 0111110 0000000000000000
3.1416        0 1000000 1001001000100000
+0            0 0000000 ----------------
-0            1 0000000 ----------------
+inf          0 1111111 0000000000000000
-inf          1 1111111 0000000000000000
NaN           - 1111111 xxxxxxxxxxxxxxxx some non-zero value so as not to be interpreted as inf
```

## Input/Output
I aimed to keep input/output consistent. Floats are stored in registers `AHL`
and `CDE`, where `A` and `C` hold the sign (top bit) and exponent (bottom bits),
and `HL` and `DE` hold the bottom 16 bits of the significand. `AHL` always holds
the first input (often referred to in these documents as `x`), and `CDE` always
holds the second floating-point input (referred to as `y` in these docs). In all
cases where output is a float, the result is in `AHL`.

There are three "strange" routines:
* `f24rand` has no input
* `f24cmp` takes float inputs, but returns output in the zero flag and carry flag
* `f24div_pow2` takes as second input an unsigned integer in register `B`.

To summarize:
*  AHL is `x`, the first operand (if required)
*  CDE is `y`, the second operand (if required)
*  AHL is the output (if output is a float)


## Routines
These float routines are for the most part prefixed with `f24` to distinguish
them. Most of them are in their own file, but some files contain several
routines. These cases are noted in the chart below.

```
f24abs       |x|
f24acosh     acosh(x)
f24acos      acos(x)
f24add       x+y
f24amean     (x+y)/2
f24asinh     asinh(x)
f24asin      asin(x)
f24atanh     atanh(x)
f24atan      atan(x)
f24bg        1/BG(x,y)  (this is a special-purpose routine)
f24cmp       compare x to y
f24cosh      cosh(x)
f24cos       cos(x)
f24neg       -x
f24div       x/y
f24div2      x/2        (included in f24amean.z80)
f24div_pow2  x/2^k
f24exp       e^x
f24geomean   sqrt(x*y)
f24log10     log10(x)
f24log2      log2(x)
f24logy      log_y(x)
f24log       log(x)     (a.k.a. ln(x))
f24mod1      x mod 1
f24mul2      x*2
f24mul3      x*3
f24mul       x*y
f24pow10     10^x
f24pow2      2^x
f24pow       x^y
f24rand      random number on [0,1)
f24rsub      -x+y       (included with f24sub.z80)
f24sinh      sing(x)
f24sin       sin(x)
f24sqrt      sqrt(x)
f24sqr       x*x
f24sub       x-y
f24tanh      tanh(x)
f24tan       tan(x)
```
