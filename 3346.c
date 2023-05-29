#include <stdio.h>

int main() {
  double f1, f2, t1, t2;
  scanf("%lf %lf", &f1, &f2);
  t1 = 100 + f1;
  t2 = t1 + ((f2/100)*t1);

  printf("%lf\n", t2-100);
  return 0;
}