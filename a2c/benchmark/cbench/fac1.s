.section .text
.globl S_0x8048300
S_0x8048300:
endbr32
xor %ebp,%ebp
pop %esi
mov %esp,%ecx
and $0xFFFFFFF0,%esp
push %eax
push %esp
push %edx
call S_0x8048337
add $_GLOBAL_OFFSET_TABLE_,%ebx
lea S_0x80484D0,%eax
push %eax
lea S_0x8048460,%eax
push %eax
push %ecx
push %esi
mov $S_0x8048416,%eax
push main
call __libc_start_main
hlt

S_0x8048337:
mov (%esp),%ebx
ret
BB_2:
xchg %ax,%ax
xchg %ax,%ax
nop
.globl S_0x8048340
S_0x8048340:
endbr32
ret
BB_4:
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
nop
.globl S_0x8048350
S_0x8048350:
mov (%esp),%ebx
ret
BB_6:
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax
xchg %ax,%ax

.globl S_0x8048360
S_0x8048360:
mov $S_0x804A018,%eax
cmp $S_0x804A018,%eax
je S_0x8048390
BB_8:
mov $0x0,%eax
test %eax,%eax
je S_0x8048390
BB_9:
push %ebp
mov %esp,%ebp
sub $0x14,%esp
push $S_0x804A018
call *%eax
add $0x10,%esp
leave
ret
BB_10:
nop;nop;nop;nop;nop;nop;nop;
xchg %ax,%ax

S_0x8048390:
ret
BB_12:
nop;nop;nop;nop;nop;nop;nop;
nop;nop;nop;nop;nop;nop;nop;
nop

.globl S_0x80483A0
S_0x80483A0:
mov $S_0x804A018,%eax
sub $S_0x804A018,%eax
mov %eax,%edx
shr $0x1F,%eax
sar $0x2,%edx
add %edx,%eax
sar %eax
je S_0x80483D8
BB_14:
mov $0x0,%edx
test %edx,%edx
je S_0x80483D8
BB_15:
push %ebp
mov %esp,%ebp
sub $0x10,%esp
push %eax
push $S_0x804A018
call *%edx
add $0x10,%esp
leave
ret
BB_16:
nop;nop;nop;nop;nop;nop;nop;

S_0x80483D8:
ret
BB_18:
nop;nop;nop;nop;nop;nop;nop;
.globl S_0x80483E0
S_0x80483E0:
endbr32
cmpb $0x0,S_0x804A018
jne S_0x8048408
BB_20:
push %ebp
mov %esp,%ebp
sub $0x8,%esp
call S_0x8048360
movb $0x1,S_0x804A018
leave
ret
BB_21:
nop;nop;nop;nop;nop;nop;nop;

S_0x8048408:
ret
BB_23:
nop;nop;nop;nop;nop;nop;nop;

.globl S_0x8048410
S_0x8048410:
endbr32
jmp S_0x80483A0

.globl main
main:
.globl S_0x8048416
S_0x8048416:
endbr32
push %ebp
mov %esp,%ebp
sub $0x10,%esp
call S_0x804845C
add $_GLOBAL_OFFSET_TABLE_,%eax
movl $0x5,-0x4(%ebp)
movl $0x1,-0x8(%ebp)
movl $0x1,-0xc(%ebp)
jmp S_0x804844F

S_0x8048441:
mov -0x8(%ebp),%eax
imul -0xc(%ebp),%eax
mov %eax,-0x8(%ebp)
addl $0x1,-0xc(%ebp)

S_0x804844F:
mov -0xc(%ebp),%eax
cmp -0x4(%ebp),%eax
jle S_0x8048441
BB_28:
mov -0x8(%ebp),%eax
leave
ret

.globl S_0x804845C
S_0x804845C:
mov (%esp),%eax
ret

.globl S_0x8048460
S_0x8048460:
endbr32
push %ebp
call S_0x80484D5
add $_GLOBAL_OFFSET_TABLE_,%ebp
push %edi
push %esi
push %ebx
sub $0xC,%esp
mov %ebp,%ebx
mov 0x28(%esp),%edi
call 0x80482A8
lea 0x8049F10,%ebx
lea 0x8049F0C,%eax
sub %eax,%ebx
sar $0x2,%ebx
je S_0x80484BD
BB_31:
xor %esi,%esi
nop;nop;nop;nop;nop;nop;nop;
lea 0x0(%esi),%esi

S_0x80484A0:
sub $0x4,%esp
push %edi
pushl 0x2c(%esp)
pushl 0x2c(%esp)
call *0x8049f0c(,%esi,0x4)
add $0x1,%esi
add $0x10,%esp
cmp %esi,%ebx
jne S_0x80484A0

S_0x80484BD:
add $0xC,%esp
pop %ebx
pop %esi
pop %edi
pop %ebp
ret
BB_34:
nop;nop;nop;nop;nop;nop;nop;
nop;nop;nop;nop;nop;nop;nop;

.globl S_0x80484D0
S_0x80484D0:
endbr32
ret

.globl S_0x80484D5
S_0x80484D5:
mov (%esp),%ebp
ret
.section .rodata

s_dummy: 
.byte 0x03
.byte 0x00
.byte 0x00
.byte 0x00
S_0x80484F8:
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
.section .got

.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00
.section .bss

S_0x804A018:
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x00

.section        .ctors,"aw",@progbits
.align 4
.long S_0x8048410
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
.byte 0x71
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x10
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
.byte 0x80
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xfc
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
.byte 0x5c
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xb0
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
.byte 0x6c
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x9c
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
.byte 0x7e
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
.byte 0x46
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x46
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
.byte 0xfd
.byte 0x34
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
.byte 0x38
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
.byte 0xbc
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
.byte 0x90
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
.byte 0x60
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0xd9
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x4c
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0xd4
.byte 0x00
.byte 0x00
.byte 0x01
.byte 0x00
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0x64
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xec
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0x60
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xcc
.byte 0xff
.byte 0xff
.byte 0xff
.byte 0x1a
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x80
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x44
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x6c
.byte 0xff
.byte 0xff
.byte 0xfe
.byte 0x04
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0xb8
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0xf4
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x94
.byte 0xff
.byte 0xff
.byte 0xfd
.byte 0xd4
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x09
.byte 0x00
.byte 0x00
.byte 0x00
.byte 0x50
.byte 0x3b
.byte 0x03
.byte 0x1b
.byte 0x01
