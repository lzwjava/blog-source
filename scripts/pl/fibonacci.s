	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 2
	.globl	_fibonacci                      ; -- Begin function fibonacci
	.p2align	2
_fibonacci:                             ; @fibonacci
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	w0, [sp, #8]
	ldr	w8, [sp, #8]
	subs	w8, w8, #1
	cset	w8, gt
	tbnz	w8, #0, LBB0_2
	b	LBB0_1
LBB0_1:
	ldr	w8, [sp, #8]
	stur	w8, [x29, #-4]
	b	LBB0_3
LBB0_2:
	ldr	w8, [sp, #8]
	subs	w0, w8, #1
	bl	_fibonacci
	str	w0, [sp, #4]                    ; 4-byte Folded Spill
	ldr	w8, [sp, #8]
	subs	w0, w8, #2
	bl	_fibonacci
	mov	x8, x0
	ldr	w0, [sp, #4]                    ; 4-byte Folded Reload
	add	w8, w0, w8
	stur	w8, [x29, #-4]
	b	LBB0_3
LBB0_3:
	ldur	w0, [x29, #-4]
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	wzr, [x29, #-4]
	mov	w8, #10                         ; =0xa
	stur	w8, [x29, #-8]
	ldur	w9, [x29, #-8]
                                        ; implicit-def: $x8
	mov	x8, x9
	mov	x9, sp
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	stur	wzr, [x29, #-12]
	b	LBB1_1
LBB1_1:                                 ; =>This Inner Loop Header: Depth=1
	ldur	w8, [x29, #-12]
	ldur	w9, [x29, #-8]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB1_4
	b	LBB1_2
LBB1_2:                                 ;   in Loop: Header=BB1_1 Depth=1
	ldur	w0, [x29, #-12]
	bl	_fibonacci
	mov	x9, sp
                                        ; implicit-def: $x8
	mov	x8, x0
	str	x8, [x9]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	b	LBB1_3
LBB1_3:                                 ;   in Loop: Header=BB1_1 Depth=1
	ldur	w8, [x29, #-12]
	add	w8, w8, #1
	stur	w8, [x29, #-12]
	b	LBB1_1
LBB1_4:
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_printf
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"Fibonacci sequence up to %d:\n"

l_.str.1:                               ; @.str.1
	.asciz	"%d "

l_.str.2:                               ; @.str.2
	.asciz	"\n"

.subsections_via_symbols
