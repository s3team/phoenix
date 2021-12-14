#include <string.h>

void reverse(char s[])
{
  int c, i, j;
  
  for (i=0, j=strlen(s)-1; i<j; i++, j--)
  {
    c = s[i];
    s[i] = s[j];
    s[j] = c;
  }
}

#include <stdio.h>
void main()
{
  char s[] = "this is a string";
  printf("%s\n", s);
  reverse(s);
  printf("%s\n", s);
  reverse(s);
  printf("%s\n", s);
}
