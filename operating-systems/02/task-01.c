#include <stdio.h>

int main(){
  int length = 0, width = 0;
  printf("Enter length and width\n");
  scanf("%d %d", &length, &width);

  int area = length * width;
  printf("Area: = %d\n", area);
  return 0;
}
