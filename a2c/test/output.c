// todo: may add some header files
#include <limits.h>
#include <string.h>
#include <stdio.h>

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

unsigned int usermain();
unsigned int S_0x8048416();


unsigned int usermain(){
		PUSH(ebp);
		ebp = esp;
		PUSH(0xA);
		eax = CALL_FUNC(S_0x8048416);
		esp += 0x4;
		LEAVE();
		RETURN(eax);
}

unsigned int S_0x8048416(){
		PUSH(ebp);
		ebp = esp;
		esp -= 0x10;
		*(unsigned int *)(ebp-0x4) = 0x1;
		goto S_0x8048441;
	S_0x8048433:
		eax = *(unsigned int *)(ebp-0x4);
		eax *= *(unsigned int *)(ebp+0x8);
		*(unsigned int *)(ebp-0x4) = eax;
		*(unsigned int *)(ebp+0x8) -= 0x1;
	S_0x8048441:
		UPDATE_EFLAGS(*(unsigned int *)(ebp+0x8), 0x1, -);
		if(GET_EFLAGS(ZF) == 0 && GET_EFLAGS(SF) == GET_EFLAGS(OF)) goto S_0x8048433;
	BB_25:
		eax = *(unsigned int *)(ebp-0x4);
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

    usermain();

    free(stack);
    
    return 0;
}


