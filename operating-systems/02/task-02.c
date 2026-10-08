#include <stdio.h>

int main(){
  int a, b, c;
  printf("Enter three sides of triangle\n");
  scanf("%d %d %d", &a, &b, &c);

  if(a + b <= c || a + c <= b || b + c <= a){
    printf("Invalid Triangle\n");
  }
  else if (a == b && b == c) {
    printf("Valid Triangle - Equilateral\n");
  }
  else if (a == b || a == c || b == c) {
    printf("Valid triangle - Isosceles\n");
  }
  else {
    printf("Valid triangle - Scalene\n");
  }
  return 0;
}
