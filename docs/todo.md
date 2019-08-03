# Accuracy Issues
* xacosh

# Bugs
* atanh(x>1) should return `NaN`. `acosh` returns `NaN` as it should. The difference is that the offending value is in the second arg, not the first.

# Range Reduction
We need to apply range reduction to some existing routines:
* xln
* xatan
* xatanh
* sinSingle
* cosSingle
* asinhSingle needs to be reduced to |x|>=1

# Need to optimize the BG algorithm.
The BG algorithm, is the core to the inverse trig and inverse hyperbolic functions, as well as the natural logarithm. One easy way to make it faster is to write custom routines to perform the following:

* *sorry, already done !*

There is also the consideration of overflow. The output to the BG algorithm will be somewhere between the inputs, so overflow and underflow should never be an issue (except with the special numbers `0` and `inf`). However, the way I have it setup, particularly large numbers could cause overflow because I am adding as much as 42 to their exponents. Instead, we can decrement the exponents by 41 as well, along with `const_3028466566125`. For numeric stability, we'll need to adjust the powers several times, but this is pretty cheap.

**We also need to create a `xgeomean` routine that doesn't overflow.** If the inputs to the geometric mean function fit in our floats, the output will never overflow. However, my dirty solution uses x*y as an intermediate step, and that can overflow.
