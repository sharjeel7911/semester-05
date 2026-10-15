// Write a C program that takes two integers as command line arguments and prints their multiplication.
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	if (argc < 2) {
		printf("Please provide 2 arguments.\n");
		return 1;
	}

	int a = atoi(argv[1]);
	int b = atoi(argv[2]);
	printf("Your multiplication of %d and %d is: %d\n", a, b, a * b);
	return 0;
}