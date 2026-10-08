#include <stdio.h>

void check_prime_number(int num);

int main(){
  int num = 0;
  printf("Enter a Number\n");
  scanf("%d", &num);
  check_prime_number(num);
  return 0;
}

void check_prime_number(int num){
  if (num <= 1){
    printf("Invalid Number\n");
    return;
  }
  if (num == 2) {
    printf("Prime Number\n");
    return;
  }
  if (num % 2 == 0) {
    printf("Not a Prime Number\n");
    return;
  }

  for (int i = 3; i * i <= num; i += 2) {
    if (num % i == 0) {
        printf("Not a Prime Number\n");
        return;
    }
  }
  printf("Prime Number\n");
}
