/*
  Write a C program in which the parent process receives an integer array through
  command-line arguments and passes it to each of its two child processes using pipe.
  Child1 process will find the sum of array elements, child2 will find min of array
  elements and return their respective results back to parent process using separate pipes.
  The parent processes will print min and sum value on the terminal.
  HINT: You need to create 4 separate pipes for this task.
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define READ 0
#define WRITE 1

int find_sum(const int* arr, int n) {
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += arr[i];
	}
	return sum;
}

int find_min(const int* arr, int n) {
	int min_val = arr[0];
	for (int i = 1; i < n; i++) {
		if (arr[i] < min_val) {
			min_val = arr[i];
		}
	}
	return min_val;
}

int main(int argc, char** argv) {
	if (argc < 2) {
		printf("Usage: %s <num1> <num2> ... <numN>\n", argv[0]);
		return 1;
	}

	int n = argc - 1;
	int* arr = malloc(n * sizeof(int));
	if (!arr) {
		perror("Memory allocation failed");
		return 1;
	}

	for (int i = 0; i < n; i++) {
		arr[i] = atoi(argv[i + 1]);
	}

	int pfd_p_to_c1[2], pfd_c1_to_p[2];
	int pfd_p_to_c2[2], pfd_c2_to_p[2];

	if (pipe(pfd_p_to_c1) == -1 || pipe(pfd_c1_to_p) == -1 || pipe(pfd_p_to_c2) == -1 || pipe(pfd_c2_to_p) == -1) {
		perror("Pipe creation failed");
		free(arr);
		return 1;
	}

	// ==================== Fork Child 1 ====================
	pid_t pid_1 = fork();
	if (pid_1 < 0) {
		perror("Fork 1 failed");
		free(arr);
		return 1;
	}

	// ==================== Fork Child 2 ====================
	pid_t pid_2 = -1;
	if (pid_1 > 0) {
		pid_2 = fork();
		if (pid_2 < 0) {
			perror("Fork 2 failed");
			free(arr);
			return 1;
		}
	}

	// ==================== PARENT PROCESS ====================
	if (pid_1 > 0 && pid_2 > 0) {
		// Close read ends for parent-to-child pipes
		close(pfd_p_to_c1[READ]);
		close(pfd_p_to_c2[READ]);

		// Close write ends for child-to-parent pipes
		close(pfd_c1_to_p[WRITE]);
		close(pfd_c2_to_p[WRITE]);

		// Send full array to both child processes
		write(pfd_p_to_c1[WRITE], arr, n * sizeof(int));
		close(pfd_p_to_c1[WRITE]);

		write(pfd_p_to_c2[WRITE], arr, n * sizeof(int));
		close(pfd_p_to_c2[WRITE]);

		// Read sum from Child 1 and min from Child 2
		int sum = 0, min_val = 0;
		read(pfd_c1_to_p[READ], &sum, sizeof(int));
		close(pfd_c1_to_p[READ]);

		read(pfd_c2_to_p[READ], &min_val, sizeof(int));
		close(pfd_c2_to_p[READ]);

		// Reap children
		wait(NULL);
		wait(NULL);

		// Output results
		printf("Sum of array elements (from Child 1): %d\n", sum);
		printf("Minimum array element (from Child 2): %d\n", min_val);

		free(arr);
		return 0;
	}

	// ==================== CHILD 01 (Calculates Sum) ====================
	if (pid_1 == 0) {
		// Close Child 2 pipes completely
		close(pfd_p_to_c2[READ]);
		close(pfd_p_to_c2[WRITE]);
		close(pfd_c2_to_p[READ]);
		close(pfd_c2_to_p[WRITE]);

		// Close unused ends for Child 1
		close(pfd_p_to_c1[WRITE]);
		close(pfd_c1_to_p[READ]);

		// Receive array from parent
		read(pfd_p_to_c1[READ], arr, n * sizeof(int));
		close(pfd_p_to_c1[READ]);

		// Calculate sum
		int sum = find_sum(arr, n);

		// Send sum back to parent
		write(pfd_c1_to_p[WRITE], &sum, sizeof(int));
		close(pfd_c1_to_p[WRITE]);

		free(arr);
		exit(0);
	}

	// ==================== CHILD 02 (Calculates Min) ====================
	if (pid_2 == 0) {
		// Close Child 1 pipes completely
		close(pfd_p_to_c1[READ]);
		close(pfd_p_to_c1[WRITE]);
		close(pfd_c1_to_p[READ]);
		close(pfd_c1_to_p[WRITE]);

		// Close unused ends for Child 2
		close(pfd_p_to_c2[WRITE]);
		close(pfd_c2_to_p[READ]);

		// Receive array from parent
		read(pfd_p_to_c2[READ], arr, n * sizeof(int));
		close(pfd_p_to_c2[READ]);

		// Calculate minimum
		int min_val = find_min(arr, n);

		// Send min back to parent
		write(pfd_c2_to_p[WRITE], &min_val, sizeof(int));
		close(pfd_c2_to_p[WRITE]);

		free(arr);
		exit(0);
	}
	return 0;
}