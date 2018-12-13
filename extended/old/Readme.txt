Updated: 19:29 7 April 2014
29 minutes past the 19th hour, of the 7th day of the April of the year 2014.
Zeda Thomas


Sections:
	Formats
	Routines
	Timings and Info
	To Do
==============================
Formats
==============================
  This library does NOT conform to the IEEE extended precision 80-bit floating point format.
The z80 works much better with little-endian, so conventions had to be broken for efficiency.
That said, the storage format is very similar (in fact, it is reversed):
	64 bits normalized mantissa, little endian
	15 bits signed base 2 exponent with bias of 16384
	1 bit sign
The mantissa is normalized so that the leading bit is always 1, except for the special cases,
Zero, Infinity, and NAN (Not A  Number). Floats work with "scientific notation" but in base 2
instead of base 10. If the mantissa was 110100111, and the exponent was 4, it would be interpreted as:
	1.10100111*2^4
Translating from binary to decimal, 1.65234375*2^4 = 26.4375. The mantissa has a "bias of 16384" so
16388 corresponds to the 2^4. The reasoning for this is because it makes a lot of the overflow
detection much easier. 2^-4 would be 16380. Internally, the mantissa and sign are stored in a 16-bit
integer, with the sign bit being bit 15.
  An example of what the number -26.4375 would look like in memory:
	56~63    48~55    40~47    32~39    24~31    16~23    8~15     0~7        exp+sign= 32768+16384+4
	00000000 00000000 00000000 00000000 00000000 00000000 00000000 110100111  00000000 11000100
  It's a bit more confusing than if it had been stored big-endian (indeed, that is how it was originally),
but it is more cumbersome to work with in code.

  There are special numbers including +Zero, -Zero, +infinity, -infinity, and NAN. These are all numbers that
are not normalized, and there format is to have exponent as -16384 (so bias brings this to 0 when stored)
and then:
	upper bit of the mantissa is 0 for Zero, else 1 for infinity or NAN
	if the top bit is 1, the next bit is 1 for infinity, 0 for NAN
  The rest of the bits are unused and so may be used to convey information.

==============================
Routines
==============================
  Here are the routines currently available, if this document is up to date:
	    routine		    effect			modifies	
	fpOP1_Add_fpOP2		fpOP1 + fpOP2 -> fpOP1		fpOP1,fpOP2
	fpOP1_Sub_fpOP2		fpOP1 - fpOP2 -> fpOP1		fpOP1,fpOP2
	fpOP1_Mul_fpOP2		fpOP1 * fpOP2 -> fpOP3		fpOP1 to fpOP3, outp128, outp64, word32_1, word32_2 
	fpOP1_Div_fpOP2		fpOP2 / fpOP1 -> fpOP3		fpOP1 to fpOP3
	fpOP1_inv		1.0   / fpOP1 -> fpOP3		fpOP1 to fpOP3
	fpOP1_Sqrt		sqrt(fpOP1)   -> fpOP1		fpOP1 to fpOP3, Ans, temp1
  Alternatively, you can provide HL as a pointer to the first argument
and DE points to the second, if there is one using the following routines:
	FloatAdd_80
	FloatSub_80
	FloatMul_80
	FloatDiv_80
	FloatInv_80
	FloatSqrt_80

==============================
Timings and Info
==============================

Division is generally around 18000 to 20000 clock cycles, but there are some early-exit procedures that can cut it down to under 7000 clock cycles in special circumstances.

The square root algorithm uses Newton's Method. The first iteration is optimized, but then the next 4 iterations obtains 56 bits of precision. We need 64 bits, so we need one more iteration which costs about 22000 t-states (and would theoretically yield 112 bits of precision-- far more than we need).

The multiplication algorithm is divide-and-conquer, using Karatsuba multiplication. This becomes practical after 16x16->32 multiplication, so the "base case" multiplication is a speed optimized 16 bit multiplication (32-bit output). Then 3 of these and a few add/subs make up the 32x32->64, and finally 3 of these build up to make the final 64x64->128 multiplication. The end product is a multiplication that typically takes 8500 to 11500 clock cycles, but may dip below 7000 due to the base-case optimizations.

Zero is defined with exponent = -16384, mantissa= leading bit 0

NAN is defined with exponent = -16384, mantissa = leading bits 10, followed by anything. May return info.

Infinity is defined with exponent = -16384, mantissa = leading bits 11, followed by anything. May return info.

Floats are in the syntax, 64-bit mantissa, followed by a 15-bit signed exponent, with +16384 bias, and then a sign bit.

Floating Point Operation Registers (fpOPs) have 96 bits for a mantissa, followed by a 15-bit exponent and 1-bit sign.

==============================
To Do
==============================
  Float->Str
  Str->Float
  pow2
  log2
  arctangent
  sine
  cosine
  abs
  int
  ipart
  fpart
  min
  max
  rand
  Complex Math
