.section .text
.globl S_0x8048320
S_0x8048320:
endbr32
xor %ebp,%ebp
pop %esi
mov %esp,%ecx
and $0xFFFFFFF0,%esp
push %eax
push %esp
push %edx
call S_0x8048357
add $_GLOBAL_OFFSET_TABLE_,%ebx
lea S_0x8048520,%eax
push %eax
lea S_0x80484B0,%eax
push %eax
push %ecx
push %esi
mov $S_0x8048491,%eax
push main
call __libc_start_main
hlt

S_0x8048357:
mov (%esp),%ebx
ret
BB_2:
xchg %ax,%ax
xchg %ax,%ax
nop
.globl S_0x8048360
S_0x8048360:
endbr32
ret
BB_4:
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
nop
.globl S_0x8048370
S_0x8048370:
mov (%esp),%ebx
ret
BB_6:
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax

.globl S_0x8048380
S_0x8048380:
mov $0x804A01C,%eax
cmp $0x804A01C,%eax
je S_0x80483B0
BB_8:
mov $0x0,%eax
test %eax,%eax
je S_0x80483B0
BB_9:
push %ebp
mov %esp,%ebp
sub $0x14,%esp
push $0x804A01C
call *%eax
add $0x10,%esp
leave
ret
BB_10:
nop;nop;nop;nop;nop;nop;nop;
xchg %ax,%ax

S_0x80483B0:
ret
BB_12:
nop;nop;nop;nop;nop;nop;nop;
nop;nop;nop;nop;nop;nop;nop;
nop

.globl S_0x80483C0
S_0x80483C0:
mov $0x804A01C,%eax
sub $0x804A01C,%eax
mov %eax,%edx
shr $0x1F,%eax
sar $0x2,%edx
add %edx,%eax
sar %eax
je S_0x80483F8
BB_14:
mov $0x0,%edx
test %edx,%edx
je S_0x80483F8
BB_15:
push %ebp
mov %esp,%ebp
sub $0x10,%esp
push %eax
push $0x804A01C
call *%edx
add $0x10,%esp
leave
ret
BB_16:
nop;nop;nop;nop;nop;nop;nop;

S_0x80483F8:
ret
BB_18:
nop;nop;nop;nop;nop;nop;nop;
.globl S_0x8048400
S_0x8048400:
endbr32
cmpb $0x0,S_0x804A020
jne S_0x8048428
BB_20:
push %ebp
mov %esp,%ebp
sub $0x8,%esp
call S_0x8048380
movb $0x1,S_0x804A020
leave
ret
BB_21:
nop;nop;nop;nop;nop;nop;nop;

S_0x8048428:
ret
BB_23:
nop;nop;nop;nop;nop;nop;nop;

.globl S_0x8048430
S_0x8048430:
endbr32
jmp S_0x80483C0
BB_25:
usermalloc:
endbr32
push %ebp
mov %esp,%ebp
sub $0x10,%esp
call S_0x80484A9
add $_GLOBAL_OFFSET_TABLE_,%eax
cmpl $0x0,0x8(%ebp)
jle S_0x804846B
BB_26:
mov $S_0x804A040,%edx
lea 0x3e8(%edx),%ecx
mov S_0x804A018,%edx
sub %edx,%ecx
mov %ecx,%edx
cmp %edx,0x8(%ebp)
jle S_0x8048472

S_0x804846B:
mov $0x0,%eax
jmp S_0x804848F

S_0x8048472:
mov 0x18(%eax),%edx
mov %edx,-0x4(%ebp)
mov 0x18(%eax),%ecx
mov 0x8(%ebp),%edx
add %ecx,%edx
mov %edx,0x18(%eax)
mov -0x4(%ebp),%eax

S_0x804848F:
leave
ret

.globl main
main:
.globl S_0x8048491
S_0x8048491:
endbr32
push %ebp
mov %esp,%ebp
call S_0x80484A9
add $_GLOBAL_OFFSET_TABLE_,%eax
mov $0x0,%eax
pop %ebp
ret

.globl S_0x80484A9
S_0x80484A9:
mov (%esp),%eax
ret
BB_32:
xchg %ax,%ax
nop

.globl S_0x80484B0
S_0x80484B0:
endbr32
push %ebp
call S_0x8048525
add $_GLOBAL_OFFSET_TABLE_,%ebp
push %edi
push %esi
push %ebx
sub $0xC,%esp
mov %ebp,%ebx
mov 0x28(%esp),%edi
call 0x80482C4
lea 0x8049F10,%ebx
lea 0x8049F0C,%eax
sub %eax,%ebx
sar $0x2,%ebx
je S_0x804850D
BB_34:
xor %esi,%esi
nop;nop;nop;nop;nop;nop;nop;
lea 0x0(%esi),%esi

S_0x80484F0:
sub $0x4,%esp
push %edi
pushl 0x2c(%esp)
pushl 0x2c(%esp)
call *0x8049f0c(,%esi,0x4)
add $0x1,%esi
add $0x10,%esp
cmp %esi,%ebx
jne S_0x80484F0

S_0x804850D:
add $0xC,%esp
pop %ebx
pop %esi
pop %edi
pop %ebp
ret
BB_37:
nop;nop;nop;nop;nop;nop;nop;
nop;nop;nop;nop;nop;nop;nop;

.globl S_0x8048520
S_0x8048520:
endbr32
ret

.globl S_0x8048525
S_0x8048525:
mov (%esp),%ebp
ret
.section .rodata

s_dummy: 
.byte 0x03
.byte 0x00
.byte 0x00
.byte 0x00
S_0x8048548:
.byte 0x01
.byte 0x00
.byte 0x02
.byte 0x00
.section .data

.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
S_0x804A018:
.long S_0x804A040



.section .got

.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.section .bss

S_0x804A020:
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
S_0x804A040:
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00

.section        .ctors,"aw",@progbits
.align 4
.long S_0x8048430
.section .eh_frame
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x04
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x49
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x30
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x10
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x05
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x58
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x1c
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x10
.byte 0x00
.byte 0x00
.byte 0x04
.byte 0x0e
.byte 0xc5
.byte 0x41
.byte 0x08
.byte 0x0e
.byte 0xc7
.byte 0x41
.byte 0x0c
.byte 0x0e
.byte 0xc6
.byte 0x41
.byte 0x10
.byte 0x0e
.byte 0xc3
.byte 0x41
.byte 0x14
.byte 0x0e
.byte 0x47
.byte 0x20
.byte 0x0e
.byte 0x4d
.byte 0x30
.byte 0x0e
.byte 0x44
.byte 0x2c
.byte 0x0e
.byte 0x44
.byte 0x28
.byte 0x0e
.byte 0x41
.byte 0x24
.byte 0x0e
.byte 0x6d
.byte 0x20
.byte 0x0e
.byte 0x43
.byte 0x05
.byte 0x83
.byte 0x14
.byte 0x0e
.byte 0x41
.byte 0x04
.byte 0x86
.byte 0x10
.byte 0x0e
.byte 0x41
.byte 0x03
.byte 0x87
.byte 0x0c
.byte 0x0e
.byte 0x4c
.byte 0x02
.byte 0x85
.byte 0x08
.byte 0x0e
.byte 0x45
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x65
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x34
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xd0
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x48
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x04
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x41
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xbc
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x10
.byte 0x00
.byte 0x00
.byte 0x04
.byte 0x04
.byte 0x0c
.byte 0xc5
.byte 0x50
.byte 0x05
.byte 0x0d
.byte 0x42
.byte 0x02
.byte 0x85
.byte 0x08
.byte 0x0e
.byte 0x45
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x18
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x49
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x9c
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x1c
.byte 0x00
.byte 0x04
.byte 0x04
.byte 0x0c
.byte 0xc5
.byte 0x53
.byte 0x02
.byte 0x05
.byte 0x0d
.byte 0x42
.byte 0x02
.byte 0x85
.byte 0x08
.byte 0x0e
.byte 0x45
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x5b
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x0e
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x7c
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x1c
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x10
.byte 0xff
.byte 0xff
.byte 0xfc
.byte 0xfc
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x68
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x10
.byte 0x22
.byte 0x24
.byte 0x32
.byte 0x2a
.byte 0x39
.byte 0x1a
.byte 0x3f
.byte 0x00
.byte 0x78
.byte 0x04
.byte 0x74
.byte 0x0b
.byte 0x0f
.byte 0x4a
.byte 0x0c
.byte 0x0e
.byte 0x46
.byte 0x08
.byte 0x0e
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x20
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x44
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x20
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x05
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0x84
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x30
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x10
.byte 0x08
.byte 0x07
.byte 0x44
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x3b
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0x58
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x1c
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x10
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x88
.byte 0x04
.byte 0x04
.byte 0x0c
.byte 0x1b
.byte 0x01
.byte 0x08
.byte 0x7c
.byte 0x01
.byte 0x00
.byte 0x52
.byte 0x7a
.byte 0x01
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x14
.section .eh_frame_hdr
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x88
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0xd9
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x74
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0xd4
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x28
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0x64
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x14
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0x5d
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xf4
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0x45
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xd4
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0xea
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x88
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x14
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x74
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0xd4
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xc0
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0xc4
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x9c
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0xa4
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x0a
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x58
.byte 0x3b
.byte 0x03
.byte 0x1b
.byte 0x01
