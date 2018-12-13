floats are stored as:
    a little endian, 1.23 fixed point value with the integer part always a value of 1.
    Since the top bit of the fixed point number is always the same, we keep this as explicit and replace it with the sign bit.
    Then an 8-bit exponent with a bias of +128

This is true except for the following special numbers. In all cases, the exponent byte is 0x00.
   +zero: top byte of mantissa is 0x00
   -zero: top byte of mantissa is 0x80
   +inf:  top byte of mantissa is 0x40
   -inf:  top byte of mantissa is 0xC0
    NAN:  top byte of mantissa is 0x20
