// todo: may add some header files
#include <limits.h>
#include <string.h>
#include <stdio.h>

#define __x86__

// define marcos for get sub registers.
#ifdef __x64__
#define get_exx(var) \
    *((unsigned int*)&var)
#endif

#define get_xx(var) \
    *((unsigned short*)&var)
#define get_hx(var) \
    *((unsigned char*)&var+1)
#define get_lx(var) \
    *((unsigned char*)&var)


// define pop, push operations
#ifdef __x64__
#define PUSH(var) \
    (*(unsigned long long *)rsp = var,\
    rsp -= 8)

#define POP() \
    (rsp += 8, *((unsigned long long*)rsp-1))

#define LEAVE() \
    rsp = rbp; \
    rbp = POP();

#define CALL_FUNC(func) \
    (PUSH(rbp), \
    ((unsigned long(*)(void*, void*, void*, void*, void*))func)(*((void **)rsp+1), *((void **)rsp+2), *((void **)rsp+3),*((void **)rsp+4), *((void **)rsp+1)))

#define RETURN(reg) \
    rsp += 8; \
    return reg;

#else
#define PUSH(var) \
    (esp -= 4, *(unsigned int*)esp = var) 
    
#define POP() \
    (esp += 4, *((unsigned int*)esp-1))

#define LEAVE() \
    esp = ebp; \
    ebp = POP();

#define CALL_FUNC(func) \
    (PUSH(ebp), \
    ((unsigned int(*)(void*, void*, void*, void*, void*))func)(*((void **)esp+1), *((void **)esp+2), *((void **)esp+3),*((void **)esp+4),*((void **)esp+5)))

#define RETURN(reg) \
    esp += 4; \
    return reg;

#endif

// allocate reg variable
#ifdef __x64__
unsigned long long rax = 0;
unsigned long long rbx = 0;
unsigned long long rcx = 0;
unsigned long long rdx = 0;
unsigned long long rdi = 0;
unsigned long long rbp = 0;
unsigned long long rsi = 0;
unsigned long long rsp = 0;
unsigned long long r8 = 0;
unsigned long long r9 = 0;
unsigned long long r10 = 0;
unsigned long long r11 = 0;
unsigned long long r12 = 0;
unsigned long long r13 = 0;
unsigned long long r14 = 0;
unsigned long long r15 = 0;
#else
unsigned int eax = 0;
unsigned int ebx = 0;
unsigned int ecx = 0;
unsigned int edx = 0;
unsigned int edi = 0;
unsigned int ebp = 0;
unsigned int esi = 0;
unsigned int esp = 0;
unsigned int e8 = 0;
unsigned int e9 = 0;
unsigned int e10 = 0;
unsigned int e11 = 0;
unsigned int e12 = 0;
unsigned int e13 = 0;
unsigned int e14 = 0;
unsigned int e15 = 0;
#endif

// EFLAGS operations
#define CF 0
#define PF 1
#define AF 2
#define ZF 3
#define SF 4
#define OF 5
#define DF 6
unsigned char EFLAGS[7];

#define SET_EFLAGS(pos, val) \
    EFLAGS[pos] = val;

#define GET_EFLAGS(pos) \
    EFLAGS[pos]

#define OP(op1, op2, opcode) \
    (op1 opcode op2)

double v1, v2;
int i1, i2;
#define UPDATE_EFLAGS(op1, op2, opcode) \
    v1 = (unsigned int)op1; \
    v2 = (unsigned int)op2; \
    if(OP(v1, v2, opcode) == 0) EFLAGS[ZF] = 1; \
    else EFLAGS[ZF] = 0; \
    if(OP(v1, v2, opcode) > 0u - 1 \
       || OP(v1, v2, opcode) < 0) EFLAGS[CF] = 1; \
    else EFLAGS[CF] = 0; \
    EFLAGS[SF] = (unsigned int)OP(op1, op2, opcode) >> (sizeof(op1)*8-1); \
    v1 = (int)op1; \
    v2 = (int)op2; \
    if(OP(v1, v2, opcode) > (1<<(sizeof(op1)*8)-1)-1 \
       || OP(v1, v2, opcode) < -(1<<(sizeof(op1)*8)-1)) EFLAGS[OF] = 1; \
    else EFLAGS[OF] = 0; \
    i1 = 7, i2 = 0; \
    while(i1-- >= 0)i2 += (OP(op1, op2, opcode) >> i1) % 2; \
    EFLAGS[PF] = (i2 % 2) == 0;

unsigned char S_0x804A020[4] = {0x00,0x00,0x00,0x00,};
const unsigned char S_0x8048648[4] = {0x01,0x00,0x02,0x00,};
const unsigned char s_dummy[4] = {0x03,0x00,0x00,0x00,};
unsigned int BB_31();
unsigned int usermain();
unsigned int S_0x8048496();


unsigned int BB_31(){
		//nop;/
}

unsigned int usermain(){
		ecx = &*(unsigned int *)(esp+0x4);
		esp &= 0xFFFFFFF0;
		PUSH(*(unsigned int *)(ecx-0x4));
		PUSH(ebp);
		ebp = esp;
		PUSH(ebx);
		PUSH(ecx);
		esp -= 0x20;
		*(unsigned int *)(ebp-0x19) = 0x73696874;
		*(unsigned int *)(ebp-0x15) = 0x20736920;
		*(unsigned int *)(ebp-0x11) = 0x74732061;
		*(unsigned int *)(ebp-0xd) = 0x676E6972;
		*(unsigned char *)&*(unsigned int *)(ebp-0x9) = 0x0;
		esp -= 0xC;
		eax = &*(unsigned int *)(ebp-0x19);
		PUSH(eax);
		eax = CALL_FUNC(puts);
		esp += 0x10;
		esp -= 0xC;
		eax = &*(unsigned int *)(ebp-0x19);
		PUSH(eax);
		eax = CALL_FUNC(S_0x8048496);
		esp += 0x10;
		esp -= 0xC;
		eax = &*(unsigned int *)(ebp-0x19);
		PUSH(eax);
		eax = CALL_FUNC(puts);
		esp += 0x10;
		esp -= 0xC;
		eax = &*(unsigned int *)(ebp-0x19);
		PUSH(eax);
		eax = CALL_FUNC(S_0x8048496);
		esp += 0x10;
		esp -= 0xC;
		eax = &*(unsigned int *)(ebp-0x19);
		PUSH(eax);
		eax = CALL_FUNC(puts);
		esp += 0x10;
		//nop;/
		esp = &*(unsigned int *)(ebp-0x8);
		ecx = POP();
		ebx = POP();
		ebp = POP();
		esp = &*(unsigned int *)(ecx-0x4);
		RETURN(eax);
}

unsigned int S_0x8048496(){
		PUSH(ebp);
		ebp = esp;
		PUSH(ebx);
		esp -= 0x14;
		*(unsigned int *)(ebp-0xc) = 0x0;
		esp -= 0xC;
		PUSH(*(unsigned int *)(ebp+0x8));
		ebx = eax;
		eax = CALL_FUNC(strlen);
		esp += 0x10;
		eax -= 0x1;
		*(unsigned int *)(ebp-0x10) = eax;
		goto S_0x8048505;
	S_0x80484CA:
		edx = *(unsigned int *)(ebp-0xc);
		eax = *(unsigned int *)(ebp+0x8);
		eax += edx;
		*(unsigned int *)&eax = *(unsigned char *)&*(unsigned int *)(eax);
		*(int *)&eax = *(char *)&get_lx(eax);
		*(unsigned int *)(ebp-0x14) = eax;
		edx = *(unsigned int *)(ebp-0x10);
		eax = *(unsigned int *)(ebp+0x8);
		eax += edx;
		ecx = *(unsigned int *)(ebp-0xc);
		edx = *(unsigned int *)(ebp+0x8);
		edx += ecx;
		*(unsigned int *)&eax = *(unsigned char *)&*(unsigned int *)(eax);
		*(unsigned char *)(edx) = get_lx(eax);
		edx = *(unsigned int *)(ebp-0x10);
		eax = *(unsigned int *)(ebp+0x8);
		eax += edx;
		edx = *(unsigned int *)(ebp-0x14);
		*(unsigned char *)(eax) = get_lx(edx);
		*(unsigned int *)(ebp-0xc) += 0x1;
		*(unsigned int *)(ebp-0x10) -= 0x1;
	S_0x8048505:
		eax = *(unsigned int *)(ebp-0xc);
		UPDATE_EFLAGS(eax, *(unsigned int *)(ebp-0x10), -);
		if(GET_EFLAGS(SF) != GET_EFLAGS(OF)) goto S_0x80484CA;
	BB_28:
		//nop;/
		//nop;/
		ebx = *(unsigned int *)(ebp-0x4);
		LEAVE();
		RETURN(eax);
}



/* main function:
    1. allocate stack.
    2. setup stack.
    3. call entry point.
*/
int main(int argc, char * argv[]){

    unsigned char * stack;
#ifdef __x64__
    stack = (char*)malloc(6291456 * 2);
    rsp = rbp = (int)stack + 6291456 * 2 - 32;
#else
    stack = (char*)malloc(6291456);
    esp = ebp = (int)stack + 6291456 - 16;
#endif

    memset(EFLAGS, 0, sizeof(EFLAGS));

    // original main function here
    usermain();

    free(stack);
    return 0;
}


