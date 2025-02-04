.global _start
.text

_start:
    mov x8, #64
    mov x0, #1
    adrp x1, msg@PAGE
    add x1, x1, msg@PAGEOFF
    mov x2, #14
    svc #0

    mov x8, #93
    mov x0, #0
    svc #0

.data
msg:
    .asciz "Hello, World!\n"
