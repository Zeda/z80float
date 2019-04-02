#ifndef included_swapbuf
#define included_swapbuf
swapbuf:
;HL and DE point to the buffers to swap
;BC is the number of bytes
;Destroys A
  ld a,(de)
  ldi
  dec hl
  ld (hl),a
  inc hl
  jp pe,swapbuf
  ret
#endif
