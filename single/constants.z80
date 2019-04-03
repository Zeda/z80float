#ifndef included_constants
#define included_constants

start_const:
const_pi:     .db $DB,$0F,$49,$81
const_e:      .db $54,$f8,$2d,$81
const_lg_e:   .db $3b,$AA,$38,$80
const_ln_2:   .db $18,$72,$31,$7f
const_log2:   .db $9b,$20,$1a,$7e
const_lg10:   .db $78,$9a,$54,$81
const_0:      .db $00,$00,$00,$00
const_1:      .db $00,$00,$00,$80
const_inf:    .db $00,$00,$40,$00
const_NegInf: .db $00,$00,$C0,$00
const_NAN:    .db $00,$00,$20,$00
const_log10_e:.db $D9,$5B,$5E,$7E
const_2pi:    .db $DB,$0F,$49,$82
const_2pi_inv:.db $83,$F9,$22,$7D
const_p25:    .db $00,$00,$00,$7E
const_p5:     .db $00,$00,$00,$7F
;    .db $,$,$,$
end_const:
sin_a1: .db $A4,$AA,$2A,$7D ;a1= 2^-3 * 11184804/2^23
sin_a2: .db $AC,$83,$08,$79 ;a2= 2^-7 *  8946604/2^23
sin_a3: .db $11,$97,$4C,$73 ;a3=2^-13 * 13408017/2^23
cos_a1: .db $DA,$FF,$7F,$7E ;a1=2^-2 * 16777178/2^23
cos_a2: .db $5C,$9F,$2A,$7B ;a2=2^-5 * 11181916/2^23
cos_a3: .db $52,$26,$32,$76 ;a3=2^-10* 11675218/2^23
exp_a1: .db $15,$72,$31,$7F  ;.693146989552
exp_a2: .db $CE,$FE,$75,$7D  ;.2402298085906
exp_a3: .db $7B,$42,$63,$7B  ;.0554833215071
exp_a4: .db $FD,$94,$1E,$79  ;.00967907584392
exp_a5: .db $5E,$01,$23,$76  ;.001243632065103
exp_a6: .db $5F,$B7,$63,$73  ;.0002171671843714
const_1p40625: .db $00,$00,$34,$80  ;1.40625

iconstSingle:
    ex (sp),hl
    ld a,(hl)
    inc hl
    ex (sp),hl
constSingle:
;A is the constant ID#
;returns nc if failed, c otherwise
;HL points to the constant
    cp (end_const-start_const)>>2
    ret nc
    ld hl,start_const
    add a,a
    add a,a
    add a,l
    ld l,a
#if ((end_const-4)>>8)!=(start_const>>8)
    ccf
    ret c
    inc h
#endif
    scf
    ret
#endif
