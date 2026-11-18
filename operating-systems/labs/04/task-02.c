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

#define r 0
#define w 1

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

	int fd1[2], fd2[2];
	int fd3[2], fd4[2];

	if (pipe(fd1) == -1 || pipe(fd2) == -1 || pipe(fd3) == -1 || pipe(fd4) == -1) {
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
		close(fd1[r]);
		close(fd2[w]);
		close(fd3[r]);
		close(fd4[w]);

		// Send slices to children
		write(fd1[w], arr, n1 * sizeof(int));
		close(fd1[w]);

		write(fd3[w], arr + n1, n2 * sizeof(int));
		close(fd3[w]);

		// Read responses from children
		int min1 = 0, min2 = 0;
		read(fd2[r], &min1, sizeof(int));
		close(fd2[r]);

		read(fd4[r], &min2, sizeof(int));
		close(fd4[r]);

		// Reap children
		wait(NULL);
		wait(NULL);

		int min = (min1 < min2) ? min1 : min2;
		printf("Smallest number overall: %d\n", min);

		free(arr);
	}

	// ========== Child process - 01 ==========

	if (pid_1 == 0) {
		close(fd1[w]);
		close(fd2[r]);
		close(fd3[r]);
		close(fd3[w]);
		close(fd4[r]);
		close(fd4[w]);

		int n1 = n / 2;
		read(fd1[r], arr, n1 * sizeof(int));
		close(fd1[r]);

		int min_val = min(arr, n1);

		write(fd2[w], &min_val, sizeof(int));
		close(fd2[w]);

		free(arr);
		exit(0);
	}

	// ========== Child process - 02 ==========

	if (pid_2 == 0) {
		close(fd3[w]);
		close(fd4[r]);
		close(fd1[r]);
		close(fd1[w]);
		close(fd2[r]);
		close(fd2[w]);

		int n2 = n - (n / 2);
		read(fd3[r], arr, n2 * sizeof(int));
		close(fd3[r]);

		int min_val = min(arr, n2);

		write(fd4[w], &min_val, sizeof(int));
		close(fd4[w]);

		free(arr);
		exit(0);
	}
	return 0;
}