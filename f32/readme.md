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

## Testing Needed
* [x] f32mul2
* [ ] f32cmp
* [x] f32abs
* [x] f32neg
* [x] f32rand
