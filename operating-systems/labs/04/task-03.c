/*
  Modify the solution of Task2 in such a way that the child processes wait for a signal
  (i.e. a number) from the parent process, after receiving data, to proceed. And after
  sending back the processed data, the child processes must wait for permission to be
  granted from the parent process to exit.
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
		// close(pfd_p_to_c1[WRITE]); // kept open to send proceed and exit signals later
		write(pfd_p_to_c2[WRITE], arr + n1, n2 * sizeof(int));
		// close(pfd_p_to_c2[WRITE]); // kept open to send proceed and exit signals later

		// Send signal (number) to both children to proceed
		int proceed_signal = 1;
		printf("[Parent] Sending proceed signal to child processes...\n");
		write(pfd_p_to_c1[WRITE], &proceed_signal, sizeof(int));  // $CHANGED: send proceed signal to child 1
		write(pfd_p_to_c2[WRITE], &proceed_signal, sizeof(int));  // $CHANGED: send proceed signal to child 2
		// Read responses from children
		int min1 = 0, min2 = 0;
		read(pfd_c1_to_p[READ], &min1, sizeof(int));
		close(pfd_c1_to_p[READ]);

		read(pfd_c2_to_p[READ], &min2, sizeof(int));
		close(pfd_c2_to_p[READ]);

		// Send permission signal (number) to both children allowing them to exit
		int exit_signal = 1;
		printf("[Parent] Granting exit permission to child processes...\n");
		write(pfd_p_to_c1[WRITE], &exit_signal, sizeof(int));
		close(pfd_p_to_c1[WRITE]);

		write(pfd_p_to_c2[WRITE], &exit_signal, sizeof(int));
		close(pfd_p_to_c2[WRITE]);

		// Reap children
		wait(NULL);
		wait(NULL);

		int overall_min = (min1 < min2) ? min1 : min2;
		printf("Smallest number overall: %d\n", overall_min);

		free(arr);
		return 0;
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
		// 1. Receive data
		read(pfd_p_to_c1[READ], arr, n1 * sizeof(int));

		// 2. Wait for signal (number) from parent to proceed
		int proceed_signal = 0;
		read(pfd_p_to_c1[READ], &proceed_signal, sizeof(int));

		// 3. Process data
		int min_val = min(arr, n1);

		// 4. Send back processed data
		write(pfd_c1_to_p[WRITE], &min_val, sizeof(int));
		close(pfd_c1_to_p[WRITE]);

		// 5. Wait for permission (number) from parent to exit
		int exit_signal = 0;
		read(pfd_p_to_c1[READ], &exit_signal, sizeof(int));
		close(pfd_p_to_c1[READ]);

		free(arr);
		exit(0);
	}

	// ========== Child process - 02 ==========

	if (pid_2 == 0) {
		close(pfd_p_to_c2[WRITE]);
		close(pfd_c2_to_p[READ]);
		close(pfd_p_to_c1[READ]);
		close(pfd_p_to_c1[WRITE]);
		close(pfd_c1_to_p[READ]);
		close(pfd_c1_to_p[WRITE]);

		int n2 = n - (n / 2);
		// 1. Receive data
		read(pfd_p_to_c2[READ], arr, n2 * sizeof(int));

		// 2. Wait for signal (number) from parent to proceed
		int proceed_signal = 0;
		read(pfd_p_to_c2[READ], &proceed_signal, sizeof(int));

		// 3. Process data
		int min_val = min(arr, n2);

		// 4. Send back processed data
		write(pfd_c2_to_p[WRITE], &min_val, sizeof(int));
		close(pfd_c2_to_p[WRITE]);

		// 5. Wait for permission (number) from parent to exit
		int exit_signal = 0;
		read(pfd_p_to_c2[READ], &exit_signal, sizeof(int));
		close(pfd_p_to_c2[READ]);

		free(arr);
		exit(0);
	}

	return 0;
}