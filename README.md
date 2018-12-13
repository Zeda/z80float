# z80float
A floating point library for the Z80

The calling syntax for the single- and extended-precision floats are:
    HL points to the first operand
    DE points to the second operand
    BC points to where the result should be output


Extended precision floats are stored as 8 little-endian bytes for the (normalized) mantissa, then a 16-bit word with the upper bit being sign, and the lower 15 bits as the exponent. The exponent is biased such that 0x4000 corresponds to an exponent of 0. In general, the extended precision routines are named with an ```x``` leading the name. For example, ```xmul``` is the extended precision multiplication routine. Special numbers are represented with an exponent of ```-0x4000``` (actual value ```0x0000```). The sign bit still indicates sign, and the top two bits of the mantissa represent the specific special number:
```
    0 is represented with %00
    inf is represented with %11
    NaN is represented with %01
```

Single precision floats are stored as a 24-bit little-endian mantissa, with the top bit being an implicit ```1```. The actual top bit represents the sign. After that is an 8-bit exponent with a bias of ```+128```. Special values are stored with an exponent of ```-128``` (actual value: ```0```). The mantissa only requires the top three bits to contain specific values:
```
    +0 is represented as 0x00
    -0 is represented as 0x80
    +inf is represented as 0x40
    -inf is represented as 0xC0
    NaN is represented as 0x20
```
