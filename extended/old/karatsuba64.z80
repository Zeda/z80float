Karatsuba64:
;Input: (word64_1),(word64_2)
;Output: (outp128)
;11039 t-states worst

	ld hl,(word64_1) \ ld (word32_1),hl
	ld hl,(word64_1+2) \ ld (word32_1+2),hl
	ld hl,(word64_2) \ ld (word32_2),hl
	ld hl,(word64_2+2) \ ld (word32_2+2),hl
	call KaratsubaMul32
	ld hl,(outp64) \ ld (outp128),hl
	ld hl,(outp64+2) \ ld (outp128+2),hl
	ld hl,(outp64+4) \ ld (outp128+4),hl
	ld hl,(outp64+6) \ ld (outp128+6),hl

	ld hl,(word64_1+4) \ ld (word32_1),hl
	ld hl,(word64_1+6) \ ld (word32_1+2),hl
	ld hl,(word64_2+4) \ ld (word32_2),hl
	ld hl,(word64_2+6) \ ld (word32_2+2),hl
	call KaratsubaMul32
	ld hl,(outp64) \ ld (outp128+8),hl
	ld hl,(outp64+2) \ ld (outp128+10),hl
	ld hl,(outp64+4) \ ld (outp128+12),hl
	ld hl,(outp64+6) \ ld (outp128+14),hl

;512+2*Karatsuba
	xor a

	ld hl,(word64_1)
	ld de,(word64_1+4)
	add hl,de
	ld (word32_1),hl
	ld hl,(word64_1+2)
	ld de,(word64_1+6)
	adc hl,de
	ld (word32_1+2),hl
	rla

	ld hl,(word64_2)
	ld de,(word64_2+4)
	add hl,de
	ld (word32_2),hl
	ld hl,(word64_2+2)
	ld de,(word64_2+6)
	adc hl,de
	ld (word32_2+2),hl
	push af
	call KaratsubaMul32
;790+3*Karatsuba
	pop af
	ld c,a
	ld a,0
	jr nc,Addmore_2
	ld a,c
	ld bc,(word64_1)
	ld hl,(word64_1+4)
	add hl,bc
	ex de,hl
	ld bc,(word64_1+2)
	ld hl,(word64_1+6)
	adc hl,bc
	ex de,hl
	ld bc,(outp64+4)
	add hl,bc
	ld (outp64+4),hl
	ex de,hl
	ld bc,(outp64+6)
	adc hl,bc
	ld (outp64+6),hl
	ld c,a
	ld a,0
	adc a,c
Addmore_2:
	rr c
	jr nc,label_2
	ld bc,(word64_2)
	ld hl,(word64_2+4)
	add hl,bc
	ex de,hl
	ld bc,(word64_2+2)
	ld hl,(word64_2+6)
	adc hl,bc
	ex de,hl
	ld bc,(outp64+4)
	add hl,bc
	ld (outp64+4),hl
	ex de,hl
	ld bc,(outp64+6)
	adc hl,bc
	ld (outp64+6),hl
label_2:
	ld d,0 \ adc a,d

;(outp64) - (outp128) - (outp128+8)
	ld hl,(outp64)
	ld bc,(outp128)
	sbc hl,bc
	ld (outp64),hl

	ld hl,(outp64+2)
	ld bc,(outp128+2)
	sbc hl,bc
	ld (outp64+2),hl

	ld hl,(outp64+4)
	ld bc,(outp128+4)
	sbc hl,bc
	ld (outp64+4),hl

	ld hl,(outp64+6)
	ld bc,(outp128+6)
	sbc hl,bc
	ld (outp64+6),hl
	sbc a,d

	ld hl,(outp64)
	ld bc,(outp128+8)
	sbc hl,bc
	ld (outp64),hl

	ld hl,(outp64+2)
	ld bc,(outp128+10)
	sbc hl,bc
	ld (outp64+2),hl

	ld hl,(outp64+4)
	ld bc,(outp128+12)
	sbc hl,bc
	ld (outp64+4),hl

	ld hl,(outp64+6)
	ld bc,(outp128+14)
	sbc hl,bc
	ld (outp64+6),hl
	sbc a,d

;(outp64) + (outp128+4)
	ld hl,(outp64)
	ld bc,(outp128+4)
	add hl,bc
	ld (outp128+4),hl

	ld hl,(outp64+2)
	ld bc,(outp128+6)
	adc hl,bc
	ld (outp128+6),hl

	ld hl,(outp64+4)
	ld bc,(outp128+8)
	adc hl,bc
	ld (outp128+8),hl

	ld hl,(outp64+6)
	ld bc,(outp128+10)
	adc hl,bc
	ld (outp128+10),hl

	ld hl,(outp128+12)
	ld e,a
	adc hl,de
	ld (outp128+12),hl
	ret nc
	ld hl,(outp128+14)
	inc hl
	ld (outp128+14),hl
	ret
KaratsubaMul32:
;Input: (word32_1), (word32_2)
;Output: (outp64)
;2931 t-states worst case, 2345 best
;Previous best optimized: 3666 t-states worst case, 2880 lower bound

;has a bug. For example, in pi*e, multiplying the upper 32 bits of each ends in A189, but should be a288

	ld bc,(word32_1)
	ld de,(word32_2)
	call mul16  ;DEHL
	ld (outp),hl
	ld (outp+2),de


	ld bc,(word32_1+2)
	ld de,(word32_2+2)
	call mul16  ;DEHL
	ld (outp+4),hl
	ld (outp+6),de

	xor a
	ld hl,(word32_1)
	ld bc,(word32_1+2)
	add hl,bc
	rla
	ex de,hl

	ld hl,(word32_2)
	ld bc,(word32_2+2)
	add hl,bc
	ld b,h
	ld c,l

	push af
  call mul16
;DEHL
	pop af
	push hl
	ld c,a
	ld a,0
	jr nc,Addmore_1
;(ax+b)(cx+d) = acx^2+axd+bcx+bd
;c flag is c
;
;x=2^16
;a,c are 0 or 1
;  If a = 1, add c to A (A is the overflow thing), add (word32_2)+(word32_2+2) to DE
;  If c = 1, add b to DE
	ld a,c
	ld bc,(word32_1)
	ld hl,(word32_1+2)
	add hl,bc
	add hl,de
	ex de,hl
	ld c,a
	ld a,0
	adc a,c
Addmore_1:
	rr c
	jr nc,label_1
;if bit 7 is set, A =2, else A=0
	ld bc,(word32_2)
	ld hl,(word32_2+2)
	add hl,bc
	add hl,de
	ex de,hl
	adc a,0
label_1:
	pop hl


;ADEHL - (outp) - (outp+4)
	ld bc,(outp)
;	or a
	sbc hl,bc
	ex de,hl
;HLDE
	ld bc,(outp+2)
	sbc hl,bc \ sbc a,0
	ex de,hl
;DEHL
	ld bc,(outp+4)
	sbc hl,bc
	ex de,hl
;HLDE
	ld bc,(outp+6)
	sbc hl,bc \ sbc a,0
	ex de,hl
;DEHL + (outp+2)
	ld bc,(outp+2)
	add hl,bc
	ld (outp+2),hl
	ex de,hl
;HLDE

	ld bc,(outp+4)
	ld de,(outp+6)
	adc hl,bc
	ld (outp+4),hl
	ld h,0 \ ld l,a
	adc hl,de
	ld (outp+6),hl
	ret
