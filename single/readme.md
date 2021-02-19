# single
These `single` routines are for a non-standard 32-bit float format. In
retrospect, the choice of name makes matters more confusing.

## Format
These floats are stored with a little-endian 24-bit significand (encoded with 23
bits, the top bit being an implicit `1`). This is followed by a sign bit, then
an 8-bit exponent with a bias of +128 (so an exponent of 0 is encoded as 128).

## Special values (0, inf, NaN)
All special values have an exponent of -128 (literally stored as 0x00).
The sign bit and the top 2 bits of the significand determines if the special
value is `+0`, `-0`, `+inf`, `-inf`, or `NaN`.
If the top bit of the significand is a 1, then the value is `inf`.
Otherwise, if the next bit is 0, then the value is `0` else it is `NaN`.

## Example values
These are example values displayed in big-endian for readability. In memory,
these are stored in little-endian. A `-` means the bit value is irrelevant.
```
                 eeeeeee s mmmmmmmm mmmmmmmm mmmmmmmm
5.87747175e-39   0000001 0 00000000 00000000 00000000  smallest positive number
3.40282367e38    1111111 0 11111111 11111111 11111111  largest positive number
1.0              1000000 0 00000000 00000000 00000000
2.0              1000001 0 00000000 00000000 00000000
-1.0             1000000 1 00000000 00000000 00000000
-0.5             0111111 1 00000000 00000000 00000000
3.14159265       1000001 0 01001001 00001111 11011011
+0               0000000 0 00------ -------- --------
-0               0000000 1 00------ -------- --------
+inf             0000000 0 1------- -------- --------
-inf             0000000 1 1------- -------- --------
NaN              0000000 - 01------ -------- --------
```

## Input/Output
```
  x: HL points to the first operand (if any)
  y: DE points to the second operand (if any)
  t: IX points to the third operand (if any)
  z: BC points to the output
```
There is one notable exception:
* `cmpSingle` takes float inputs, but returns output in the zero flag and carry flag

## Routines
These float routines are for the most part suffixed with `Single` to distinguish
them from the other float routines in this library. Most of them are in their
own file, but some files contain several routines. These cases are noted in the
chart below.

```
absSingle       |x|
acoshSingle     acosh(x)
acosSingle      acos(x)
addSingle       x+y
ameanSingle     (x+y)/2
asinhSingle     asinh(x)
asinSingle      asin(x)
atanhSingle     atanh(x)
atanSingle      atan(x)
bg2iSingle      1/BG(x,y)  (reciprocal Borchardt-Gauss mean with 2 iterations)
bgiSingle       1/BG(x,y)  (reciprocal Borchardt-Gauss mean with 3 iterations)
cisSingle       {cos(x), sin(x)}
cmpSingle       compare x to y
coshSingle      cosh(x)
cosSingle       cos(x)
div255Single    x/255 (found in divSingle_special.z80)
div85Single     x/85  (found in divSingle_special.z80)
div51Single     x/51  (found in divSingle_special.z80)
div17Single     x/17  (found in divSingle_special.z80)
div15Single     x/15  (found in divSingle_special.z80)
div5Single      x/5   (found in divSingle_special.z80)
div3Single      x/3   (found in divSingle_special.z80)
divSingle       x/y
expSingle       e^x
geomeanSingle   sqrt(x*y)
invSingle       1/x
lgSingle        log2(x)
lnSingle        log(x)     (a.k.a. ln(x))
log10Single     log10(x)
logSingle       log_y(x)
mod1Single      x mod 1
mul10Single     x*10
mul_p375        x*.375
mul_p34375      x*.34375
mul_p041015625  x*.041015625
mulSingle       x*y
negSingle       -x
pow2Single      2^x
pow10Single     10^x
powSingle       x^y
randSingle      random number on [0,1), uniform distribution
rsubSingle      -x+y
single2str      string(x)
single2ti       TIFloat(x)
sinhSingle      sinh(x)
sinSingle       sin(x)
sqrtSingle      sqrt(x)
str2single      string ==> single
subSingle       x-y
tanhSingle      tanh(x)
tanSingle       tan(x)
tiSingle        TIFloat ==> single
```

## Example Usage
Calculate `10^(pi+e)`:

```
  ; Add pi+e
  ld hl, const_pi
  ld de, const_e
  ld bc, scrap+8
  call addSingle

  ; BC points to the output, so want to load BC into HL, then call pow10
  ld h, b
  ld l, c
  call pow10Single
  ; result is at BC (which is the same as HL and scrap+8 here)
```
