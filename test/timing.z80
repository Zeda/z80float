;Set 15MHz
  di
  in a,(2)
  add a,a
  sbc a,a
  and 3
  out (20h),a

;  ld (counter+2),hl
;get the current timer and wait for it to increment
  in a,(45h)
  inc a
  ld c,a
  add a,20    ;set the timer to 20 seconds in the future
  ld (timer),a
_:
  in a,(45h)
  cp c
  jr nz,-_
;start looping
timerloop:
;Increment the counter
counter0=$+1
  ld hl,0
  ld bc,1
  add hl,bc
  ld (counter0),hl
counter1=$+1
  ld hl,0
  dec c
  adc hl,bc
  ld (counter1),hl

_:
  in a,(45h)
timer=$+1
  cp 0
  jr z,+_
  ;<<insert code here>>
  ld bc,xOP2
  ld d,b
  ld e,c
  call xrand
  ld bc,xOP1
  ld h,b
  ld l,c
  call xrand

  call xsqrt
;4927.2006cc to generate two random numbers and set up pointers
;161277.7855cc for xln
;169440.7157cc for xatan
;10405.8479cc for mul
;11089.8843cc for div
;6479.8604cc for sqrt
;1587.3159cc for add

  ;
  jp timerloop
_:
  ld hl,(counter0)
  bcall(4507h)
  bcall(452Eh)
  ld hl,(counter1)
  bcall(4507h)
  ret
