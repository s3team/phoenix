fac:
push   %ebp
mov    %esp,%ebp
sub    $0x10,%esp
movl   $0x1,-0x4(%ebp)
jmp    B_1
B_0:
mov    -0x4(%ebp),%eax
imul   0x8(%ebp),%eax
mov    %eax,-0x4(%ebp)
subl   $0x1,0x8(%ebp)
B_1:
cmpl   $0x1,0x8(%ebp)
jg     B_0
B_2:
mov    -0x4(%ebp),%eax
leave  
ret    

main:
push   %ebp
mov    %esp,%ebp
and    $0xfffffff0,%esp
sub    $0x10,%esp
movl   $0xa,(%esp)
call   fac
leave  
ret    
