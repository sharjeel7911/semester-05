// Write a C program to display second minimum number in an array. User enter integers and you
// need to calculate the size of array and allocate run time memory for array.
#include <stdio.h>
#include <stdlib.h>

void find_second_min(int* arr, int size);
void solve_interactive(void);
void solve_cli(int argc, char** argv);

int main(int argc, char** argv) {
	if (argc > 1) {
		solve_cli(argc, argv);
	} else {
		solve_interactive();
	}
	return 0;
}

void find_second_min(int* arr, int size) {
	int min = __INT_MAX__;
	int second_min = __INT_MAX__;

	for (int i = 0; i < size; i++) {
		if (arr[i] < min) {
			second_min = min;
			min = arr[i];
		} else if (arr[i] < second_min && arr[i] != min) {
			second_min = arr[i];
		}
	}

	if (second_min == __INT_MAX__) {
		printf("There is no second minimum number in the array\n");
	} else {
		printf("Second minimum number in the array is: %d\n", second_min);
	}
}

void solve_interactive(void) {
	int size = 0;
	printf("Enter the size of array\n");
	if (scanf("%d", &size) != 1 || size < 1) {
		printf("Invalid array size\n");
		return;
	}

	int* arr = (int*)malloc(size * sizeof(int));
	if (arr == NULL) {
		printf("Memory allocation failed\n");
		return;
	}

	printf("Enter the elements of array\n");
	for (int i = 0; i < size; i++) {
		scanf("%d", &arr[i]);
	}

	find_second_min(arr, size);
	free(arr);
}

void solve_cli(int argc, char** argv) {
	int size = argc - 1;
	if (size < 1) {
		printf("No command-line arguments provided\n");
		return;
	}

	int* arr = (int*)malloc(size * sizeof(int));
	if (arr == NULL) {
		printf("Memory allocation failed\n");
		return;
	}

	for (int i = 0; i < size; i++) {
		arr[i] = atoi(argv[i + 1]);
	}

	find_second_min(arr, size);
	free(arr);
}