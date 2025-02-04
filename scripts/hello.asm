global _start
section .text

_start:
    mov     rax, 0x2000004  ; sys_write
    mov     rdi, 1          ; stdout
    lea     rsi, [rel msg]
    mov     rdx, msg.len
    syscall

    mov     rax, 0x2000001  ; sys_exit
    xor     rdi, rdi        ; exit code 0
    syscall

section .data
msg:    db  "Hello, World!", 10
.len:   equ $ - msg