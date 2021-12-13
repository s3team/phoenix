S_0x8048496:
push %ebp
mov %esp,%ebp
push %ebx
sub $0x14,%esp
movl $0x0,-0xc(%ebp)
sub $0xC,%esp
pushl 0x8(%ebp)
mov %eax,%ebx
call strlen
add $0x10,%esp
sub $0x1,%eax
mov %eax,-0x10(%ebp)
jmp S_0x8048505
S_0x80484CA:
mov -0xc(%ebp),%edx
mov 0x8(%ebp),%eax
add %edx,%eax
movzbl (%eax),%eax
movsbl %al,%eax
mov %eax,-0x14(%ebp)
mov -0x10(%ebp),%edx
mov 0x8(%ebp),%eax
add %edx,%eax
mov -0xc(%ebp),%ecx
mov 0x8(%ebp),%edx
add %ecx,%edx
movzbl (%eax),%eax
mov %al,(%edx)
mov -0x10(%ebp),%edx
mov 0x8(%ebp),%eax
add %edx,%eax
mov -0x14(%ebp),%edx
mov %dl,(%eax)
addl $0x1,-0xc(%ebp)
subl $0x1,-0x10(%ebp)
S_0x8048505:
mov -0xc(%ebp),%eax
cmp -0x10(%ebp),%eax
jl S_0x80484CA
BB_28:
nop
nop
mov -0x4(%ebp),%ebx
leave
ret

main:
lea 0x4(%esp),%ecx
and $0xFFFFFFF0,%esp
pushl -0x4(%ecx)
push %ebp
mov %esp,%ebp
push %ebx
push %ecx
sub $0x20,%esp
movl $0x73696874,-0x19(%ebp)
movl $0x20736920,-0x15(%ebp)
movl $0x74732061,-0x11(%ebp)
movl $0x676E6972,-0xd(%ebp)
movb $0x0,-0x9(%ebp)
movl $0xA7325,-0x1d(%ebp)
sub $0x8,%esp
lea -0x19(%ebp),%eax
push %eax
lea -0x1d(%ebp),%eax
push %eax
call printf
add $0x10,%esp
sub $0xC,%esp
lea -0x19(%ebp),%eax
push %eax
call S_0x8048496
add $0x10,%esp
sub $0x8,%esp
lea -0x19(%ebp),%eax
push %eax
lea -0x1d(%ebp),%eax
push %eax
call printf
add $0x10,%esp
sub $0xC,%esp
lea -0x19(%ebp),%eax
push %eax
call S_0x8048496
add $0x10,%esp
sub $0x8,%esp
lea -0x19(%ebp),%eax
push %eax
lea -0x1d(%ebp),%eax
push %eax
call printf
add $0x10,%esp
nop
lea -0x8(%ebp),%esp
pop %ecx
pop %ebx
pop %ebp
lea -0x4(%ecx),%esp
ret