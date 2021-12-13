/* K&R, p.87 */

void swap (int v[], int i, int j)
{
    int temp;

    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}

void qsort(int v[], int left, int right)
{
  int i, last;
  
  if (left >= right) /* do nothing if array contains */
    return;          /* fewer than two elements */
  swap(v, left, (left+right)/2); /* move partition elem */
  last = left;                   /* to v[0] */
  for (i = left+1; i <= right; i++) /* partition */
    if(v[i] < v[left])
      swap(v, ++last, i);
  
  swap(v, left, last);
  qsort(v, left, last-1);
  qsort(v, last+1, right);
}

#include <stdio.h>
void main()
{
  int a[10] = {1, 5, 1321413, 33, 9, 90, 909, 87,34335,12343};

  qsort(a,0,9);

  for (int i=0; i<10; i++)
    printf("%d, ", a[i]);
  printf("\n");
}
