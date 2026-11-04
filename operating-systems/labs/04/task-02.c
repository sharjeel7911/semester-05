/*
  Write a C program that inputs N numbers from the user and passes N/2 numbers to each
  of its two child processes through pipes. The child processes search their own list for
  the smallest number and send those numbers to their parent process through pipes. The
  parent process finally prints the smallest of them.
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define READ 0
#define WRITE 1

int min(int* arr, int n) {
	int min = arr[0];
	for (int i = 1; i < n; i++) {
		if (arr[i] < min) {
			min = arr[i];
		}
	}
	return min;
}

int main() {
	int n;
	printf("Enter the number of elements (N): ");
	if (scanf("%d", &n) != 1 || n < 2) {
		printf("Invalid input. N must be at least 2.\n");
		return 1;
	}

	int* arr = malloc(n * sizeof(int));
	if (!arr) {
		perror("Memory allocation failed");
		return 1;
	}

	printf("Enter %d numbers:\n", n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	int pfd_p_to_c1[2], pfd_c1_to_p[2];
	int pfd_p_to_c2[2], pfd_c2_to_p[2];

	if (pipe(pfd_p_to_c1) == -1 || pipe(pfd_c1_to_p) == -1 || pipe(pfd_p_to_c2) == -1 || pipe(pfd_c2_to_p) == -1) {
		perror("Pipe creation failed");
		free(arr);
		return 1;
	}

	int n1 = n / 2;
	int n2 = n - n1;

	// ==================== Create Child Processes ====================
	pid_t pid_1 = fork();
	if (pid_1 < 0) {
		perror("Fork 1 failed");
		free(arr);
		return 1;
	}

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
		// Close unused read/write ends in parent
		close(pfd_p_to_c1[READ]);
		close(pfd_c1_to_p[WRITE]);
		close(pfd_p_to_c2[READ]);
		close(pfd_c2_to_p[WRITE]);

		// Send slices to children
		write(pfd_p_to_c1[WRITE], arr, n1 * sizeof(int));
		close(pfd_p_to_c1[WRITE]);

		write(pfd_p_to_c2[WRITE], arr + n1, n2 * sizeof(int));
		close(pfd_p_to_c2[WRITE]);

		// Read responses from children
		int min1 = 0, min2 = 0;
		read(pfd_c1_to_p[READ], &min1, sizeof(int));
		close(pfd_c1_to_p[READ]);

		read(pfd_c2_to_p[READ], &min2, sizeof(int));
		close(pfd_c2_to_p[READ]);

		// Reap children
		wait(NULL);
		wait(NULL);

		int min = (min1 < min2) ? min1 : min2;
		printf("Smallest number overall: %d\n", min);

		free(arr);
	}

	// ========== Child process - 01 ==========

	if (pid_1 == 0) {
		close(pfd_p_to_c1[WRITE]);
		close(pfd_c1_to_p[READ]);
		close(pfd_p_to_c2[READ]);
		close(pfd_p_to_c2[WRITE]);
		close(pfd_c2_to_p[READ]);
		close(pfd_c2_to_p[WRITE]);

		int n1 = n / 2;
		read(pfd_p_to_c1[READ], arr, n1 * sizeof(int));
		close(pfd_p_to_c1[READ]);

		int min_val = min(arr, n1);

		write(pfd_c1_to_p[WRITE], &min_val, sizeof(int));
		close(pfd_c1_to_p[WRITE]);

		free(arr);
		exit(0);
	}

	// ========== Child process - 02 ==========

	if (pid_2 == 0) {
		close(pfd_p_to_c2[1]);
		close(pfd_c2_to_p[0]);
		close(pfd_p_to_c1[0]);
		close(pfd_p_to_c1[1]);
		close(pfd_c1_to_p[0]);
		close(pfd_c1_to_p[1]);

		int n2 = n - (n / 2);
		read(pfd_p_to_c2[READ], arr, n2 * sizeof(int));
		close(pfd_p_to_c2[READ]);

		int min_val = min(arr, n2);

		write(pfd_c2_to_p[WRITE], &min_val, sizeof(int));
		close(pfd_c2_to_p[WRITE]);

		free(arr);
		exit(0);
	}
	return 0;
}