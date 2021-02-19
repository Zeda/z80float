# extended
This is an 80-bit float format with a 1-bit sign, 15-bit exponent and 64-bit
significand.

# Format
`extended` floats are stored in little endian. The "most significant bit" is
sign, the next 15 bits are exponent, and the next 64 bits encode the 64-bit
significand (note that the top bit of the significand **is** stored explicitly).
The exponent is stored with a bias of +16384 (so an exponent of 0 is stored as
the literal value 16384). Like the so-called "single" format this library uses,
special values +0 ,-0, +inf, -inf, and NaN are stored with an exponent of -16384
(literal stored as a 0), and the sign and top two bits of the significand
determine which special value it is.

```
m is significand
e is exponent
s is sign
- is any value (0 or 1, doesn't matter)

        seeeeeee eeeeeeee mmmmmmmm mmmmmmmm mmmmmmmm mmmmmmmm mmmmmmmm mmmmmmmm mmmmmmmm mmmmmmmm
+0      00000000 00000000 00------ -------- -------- -------- -------- -------- -------- --------
-0      10000000 00000000 00------ -------- -------- -------- -------- -------- -------- --------
+inf    00000000 00000000 1------- -------- -------- -------- -------- -------- -------- --------
+inf    10000000 00000000 1------- -------- -------- -------- -------- -------- -------- --------
NaN     -0000000 00000000 01------ -------- -------- -------- -------- -------- -------- --------
 1      01000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
 2      01000000 00000001 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
 1      11000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
pi      01000000 00000001 11001001 00001111 11011010 10100010 00100001 01101000 11000010 00110101

```

## Input/Output
```
  x: HL points to the first operand (if any)
  y: DE points to the second operand (if any)
  t: IX points to the third operand (if any)
  z: BC points to the output
```
There is one notable exception:

* `xcmp` takes float inputs, but returns output in the zero flag and carry flag

## Routines
These float routines are for the most part prefixed with `x` to distinguish
them from the other float routines in this library. Most of them are in their
own file, but some files contain several routines. These cases are noted in the
chart below.

```
xabs       |x|
xacos      acos(x)
xacosh     acosh(x)
xadd       x+y
xamean     (x+y)/2
xasin      asin(x)
xasinh     asinh(x)
xatan      atan(x)
xatanh     atanh(x)
xbg        1/BG(x,y)  (reciprocal Borchardt-Gauss mean)
xcis       {cos(x), sin(x)}
xcmp       compare x to y
xcos       cos(x)
xcosh      cosh(x)
xdiv       x/y
xdiv2      x/2
xexp       e^x
xfma       x*y+t
xgeomean   sqrt(x*y)
xinv       1/x
xlg        log2(x)
xln        log(x)     (a.k.a. ln(x))
xlog       log_y(x)
xlog10     log10(x)
xmod1      x mod 1
xmul       x*y
xmul2      x*2  (found in the extended/mul directory)
xmul3      x*3  (found in the extended/mul directory)
xmul5      x*5  (found in the extended/mul directory)
xmul7      x*7  (found in the extended/mul directory)
xmul10     x*10 (found in the extended/mul directory)
xmul11     x*11 (found in the extended/mul directory)
xmul13     x*13 (found in the extended/mul directory)
xmul15     x*15 (found in the extended/mul directory)
xmul17     x*17 (found in the extended/mul directory)
xmul31     x*31 (found in the extended/mul directory)
xneg       -x
xpow       x^y
xpow2      2^x
xpow10     10^x
xrand      random number on [0,1), uniform distribution
xrsub      -x+y
xsin       sin(x)
xsinh      sinh(x)
xsqrt      sqrt(x)
xsub       x-y
xtan       tan(x)
xtanh      tanh(x)
strtox     "string" ==> extended float
xtostr     string(x)
xtoTI      TIFloat(x)
TItox      TIFloat ==> extended
```

## Example Usage
Calculate `10^(pi+e)`:

```
  ; Add pi+e
  ld hl, const_pi
  ld de, const_e
  ld bc, xOP1
  call xadd

  ; BC points to the output, so want to load BC into HL, then call pow10
  ld h, b
  ld l, c
  call xpow10
  ; result is at BC (which is the same as HL and xOP1 here)
```
