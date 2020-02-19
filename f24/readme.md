Included routines:
* `f24cmp` compares two floats
* `f24add` adds two floats (x+y)
* `f24sub` subtracts two floats (x-y)
* `f24rsub` subtracts two floats (-x+y)
* `f24mul` multiplies two floats
* `f24mul2` multiplies a float by 2 (x*2)
* `f24div` divides two floats (x/y)
* `f24sqr` squares a float (x*x)
* `f24sqrt` square-root of a float (sqrt(x))


Input/Output:
*  AHL is the first operand (if required)
*  CDE is the second operand (if required)
*  BIX is the third operand (if required)
*  AHL is the output (if output is a float)

An exception is that `f24cmp` outputs flags instead of a number

Format is:
* top bit is sign
* 7 bits for the exponent (bias is +63, so an exponent of 0 is encoded as
  `0x3F` = `0b0111111`)
* 17 bits for the mantissa, with the top bit being an implicit `1`.

Example values:
```
        s eeeeeee mmmmmmmmmmmmmmmm
1.0     0 0111111 0000000000000000
2.0     0 1000000 0000000000000000
-1.0    1 0111111 0000000000000000
-0.5    1 0111110 0000000000000000
pi      0 1000000 1001001000100000
```

Special numbers:
* `0` is represented by an exponent of -63, which is represented by `00`.
* `inf` is represented by 1*2^64, which is represented by an exponent of +64 and
   a mantissa stored as 0.
* `NaN` is represented with a mantissa >1.0 and exponent of +64
```
        s eeeeeee mmmmmmmmmmmmmmmm
+0      0 0000000 ----------------
-0      1 0000000 ----------------
+inf    0 1111111 0000000000000000
-inf    1 1111111 0000000000000000
NaN     - 1111111 xxxxxxxxxxxxxxxx
                  some non-zero value so as not to be interpreted as inf
```
