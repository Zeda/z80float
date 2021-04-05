# f32
This format conforms to the IEEE-754 binary32/single format. Notable differences
from the other [single](../single) format in this library:

| "single" (as it appears in this library)| binary32                           |
|-----------------------------------------|------------------------------------|
| exponent bias is +128                   | exponent bias is +127 |
| All special values (0, inf, NaN) are stored with an exponent of -128 | 0 has an exponent of -127, inf and NaN have an exponent of +128 |
| Sign bit is stored in the top bit of the significand so the exponent is not split across bytes. | Sign bit is stored in the top byte, so the exponent is split across two bytes. |


# Format
binary32 floats are stored in little endian. The "most significant bit" is sign,
the next 8 bits are exponent, and the next 23 bits encode the 24-bit significand
(note that the top bit of the significand is always `1`, so we don't need to
store it explicitly):
```
'm' is significand
'e' is exponent
's' is sign
'x' is any value (0 or 1, doesn't matter)
'-' is any value (0 or 1, doesn't matter)

        seeeeeee emmmmmmm mmmmmmmm mmmmmmmm
+0      00000000 0xxxxxxx xxxxxxxx xxxxxxxx
-0      10000000 0xxxxxxx xxxxxxxx xxxxxxxx
 1      00111111 10000000 00000000 00000000
 2      01000000 00000000 00000000 00000000
-1      10111111 10000000 00000000 00000000
pi      01000000 01001001 00001111 11011011
+inf    01111111 10000000 00000000 00000000
-inf    11111111 10000000 00000000 00000000
NaN     -1111111 1xxxxxxx xxxxxxxx xxxxxxxx ;as long as at least 1 'x' is non-zero

```

## Routines
(Note, I haven't tested very small and very large numbers.)

| tested |   routine   | Description |
|--------|-------------|-------------|
|  yes   | f32abs      | \|x\| - absolute value of x
|  yes   | f32acos     | arccosine(x)
|  yes   | f32acosh    | hyperbolic arccosine(x)
|  yes   | f32add      | x+y
|  yes   | f32amean    | (x+y)/2 - arithmetic mean
|  yes   | f32asin     | arcsine(x)
|  yes   | f32asinh    | hyperbolic arcsine(x)
|  yes   | f32atan     | arctangent(x)
|  yes   | f32atanh    | hyperbolic arctangent(x)
|  yes   | f32bgi      | 1/BG(x,y) - BG(x,y) is the Borchardt-Gauss Mean
|        | f32cmp      | compares x to y - returns Z and C flag
|  yes   | f32cos      | cosine(x)
|  yes   | f32cosh     | hyperbolic cosine(x)
|  yes   | f32div      | x/y
|  yes   | f32exp      | e^x
|  yes   | f32geomean  | sqrt(x*y) - geometric mean
|  yes   | f32log      | log(x) - natural logarithm
|  yes   | f32log10    | log10(x) - log base 10
|  yes   | f32log2     | log2(x) - log base 2
|  yes   | f32logy     | log_y(x) - log base y
|  yes   | f32mod1     | x % 1
|  yes   | f32mul      | x*y
|  yes   | f32mul2     | x*2
|  yes   | f32neg      | -x
|  yes   | f32pow      | x^y
|  yes   | f32pow10    | 10^x
|  yes   | f32pow2     | 2^x
|  yes   | f32rand     | rand - uniform random variable selected from [0,1)
|  yes   | f32randnorm | randnorm - normal random variable centered about 0 with standard deviation of 1.
|  yes   | f32rsub     | -x+y
|  yes   | f32sin      | sine(x)
|  yes   | f32sinh     | hyperbolic sine(x)
|  yes   | f32sqrt     | sqrt(x) - square root
|  yes   | f32sub      | x-y
|  yes   | f32tan      | tangent(x)
|        | f32tanh     | hyperbolic tangent(x) - seems to be broken at tanh(0)

## Useful Subroutines
These are in the [/f32/routines](/f32/routines) folder:

* f32_muli8
  * multiply an f32 float by a signed 8-bit integer
  * this is faster than multiplying two floats
* f32_mulu8_divpow2
  * multiply an f32 float by an unsigned 8-bit integer, and divide by a power of 2
  * this is faster than multiplying two floats.
* f32mulpow2
  * multiply an f32 float by a power of 2
  * Significantly faster than multiplication. This just needs to do an 8-bit add
    along with edge-case testing (and special numbers).
