#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
  printf("No of arguments %d\n", argc);

  if (argc > 1) {
      int age = atoi(argv[1]);
      printf("Your age is: %d\n", age);
  } else {
    printf("Please provide your age.\n");
  }
  return 0;
}
