S_0x8048416:
push %ebp
mov %esp,%ebp
sub $0x10,%esp
movl $0x1,-0x4(%ebp)
jmp S_0x8048441


S_0x8048433:
mov -0x4(%ebp),%eax
imul 0x8(%ebp),%eax
mov %eax,-0x4(%ebp)
subl $0x1,0x8(%ebp)


S_0x8048441:
cmpl $0x1,0x8(%ebp)
jg S_0x8048433
BB_25:
mov -0x4(%ebp),%eax
leave
ret


main:
push %ebp
mov %esp,%ebp
push $0xA
call S_0x8048416
add $0x4,%esp
leave
ret
