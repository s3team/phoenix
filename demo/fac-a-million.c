#include <stdio.h>

int fac(int n)
{
  int f=1;

  while (n>1) {
    f *= n;
    n--;
  }

  return f;
}

int main()
{
  int i,f;
  for (i=0; i<1000000; i++)
    f = fac(10);
  printf("fac(10) = %d\n", f);
  return f;
}
