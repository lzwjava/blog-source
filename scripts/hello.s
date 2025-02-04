.global _start
.text

_start:
    // Write "Hello, World!" to stdout
    mov x8, #64             // syscall number for write (sys_write)
    mov x0, #1              // file descriptor 1 (stdout)
    adrp x1, msg@PAGE       // load the page address of msg
    add x1, x1, msg@PAGEOFF // add the offset within the page
    mov x2, #14             // length of the message
    svc #0                   // invoke syscall

    // Exit the program
    mov x8, #93             // syscall number for exit (sys_exit)
    mov x0, #0              // exit code 0
    svc #0                   // invoke syscall

.data
msg:
    .asciz "Hello, World!\n"
