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

int find_minimum(int*, int);
void run_child_process(int, int, int);
void run_parent_process(int, int, int, int, int*, int);

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

	int pipe_p_to_c1[2], pipe_c1_to_p[2];
	int pipe_p_to_c2[2], pipe_c2_to_p[2];

	if (pipe(pipe_p_to_c1) == -1 || pipe(pipe_c1_to_p) == -1 || pipe(pipe_p_to_c2) == -1 || pipe(pipe_c2_to_p) == -1) {
		perror("Pipe creation failed");
		free(arr);
		return 1;
	}

	pid_t pid_01 = fork();
	if (pid_01 < 0) {
		perror("Fork 1 failed");
		free(arr);
		return 1;
	}

	if (pid_01 == 0) {
		// Child 1 process
		close(pipe_p_to_c1[1]);
		close(pipe_c1_to_p[0]);
		close(pipe_p_to_c2[0]);
		close(pipe_p_to_c2[1]);
		close(pipe_c2_to_p[0]);
		close(pipe_c2_to_p[1]);

		int n1 = n / 2;
		run_child_process(pipe_p_to_c1[0], pipe_c1_to_p[1], n1);
		free(arr);
		exit(0);
	}

	pid_t pid_02 = fork();
	if (pid_02 < 0) {
		perror("Fork 2 failed");
		free(arr);
		return 1;
	}

	if (pid_02 == 0) {
		// Child 2 process
		close(pipe_p_to_c2[1]);
		close(pipe_c2_to_p[0]);
		close(pipe_p_to_c1[0]);
		close(pipe_p_to_c1[1]);
		close(pipe_c1_to_p[0]);
		close(pipe_c1_to_p[1]);

		int n1 = n / 2;
		int n2 = n - n1;
		run_child_process(pipe_p_to_c2[0], pipe_c2_to_p[1], n2);
		free(arr);
		exit(0);
	}

	// Parent process
	close(pipe_p_to_c1[0]);
	close(pipe_c1_to_p[1]);
	close(pipe_p_to_c2[0]);
	close(pipe_c2_to_p[1]);

	run_parent_process(pipe_p_to_c1[1], pipe_c1_to_p[0], pipe_p_to_c2[1], pipe_c2_to_p[0], arr, n);

	free(arr);
	return 0;
}

int find_minimum(int* arr, int n) {
	int min = arr[0];
	for (int i = 1; i < n; i++) {
		if (arr[i] < min) {
			min = arr[i];
		}
	}
	return min;
}

void run_child_process(int read_fd, int write_fd, int n) {
	int* sub_arr = (int*)malloc(n * sizeof(int));
	if (!sub_arr) {
		perror("Memory allocation failed in child");
		exit(1);
	}

	// 1. Read array data from parent
	read(read_fd, sub_arr, n * sizeof(int));

	// 2. Wait for proceed signal from parent
	int proceed_signal;
	read(read_fd, &proceed_signal, sizeof(int));

	// 3. Find minimum in the sub-array
	int min_val = find_minimum(sub_arr, n);

	// 4. Send the minimum value back to parent
	write(write_fd, &min_val, sizeof(int));
	close(write_fd);

	// 5. Wait for exit permission signal from parent before exiting
	int exit_signal;
	read(read_fd, &exit_signal, sizeof(int));
	close(read_fd);

	free(sub_arr);
}

void run_parent_process(int p_to_c1_write, int c1_to_p_read, int p_to_c2_write, int c2_to_p_read, int* arr, int n) {
	int n1 = n / 2;
	int n2 = n - n1;

	// 1. Send data arrays to both children
	write(p_to_c1_write, arr, n1 * sizeof(int));
	write(p_to_c2_write, arr + n1, n2 * sizeof(int));

	// 2. Send proceed signals to both children
	int proceed_val = 1;
	write(p_to_c1_write, &proceed_val, sizeof(int));
	write(p_to_c2_write, &proceed_val, sizeof(int));

	// 3. Read minimum values back from children
	int min1, min2;
	read(c1_to_p_read, &min1, sizeof(int));
	close(c1_to_p_read);

	read(c2_to_p_read, &min2, sizeof(int));
	close(c2_to_p_read);

	int overall_min = (min1 < min2) ? min1 : min2;
	printf("Smallest number overall: %d\n", overall_min);

	// 4. Send exit permission signals to both children and close write ends
	int exit_val = 1;
	write(p_to_c1_write, &exit_val, sizeof(int));
	close(p_to_c1_write);

	write(p_to_c2_write, &exit_val, sizeof(int));
	close(p_to_c2_write);

	// 5. Wait for both child processes to finish execution
	wait(NULL);
	wait(NULL);
}