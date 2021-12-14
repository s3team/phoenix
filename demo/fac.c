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
  return fac(10);
}
