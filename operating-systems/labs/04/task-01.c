/*
  Write a C program in which the parent process receives an integer array through
  command-line arguments and passes it to its child process using pipe, The child process
  sorts that array (using the sorting algorithm of your choice) and return that array back to
  parent process using a separate pipe. The parent processes finally prints that sorted array
  on the terminal.
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int compare_ints(const void*, const void*);
void run_child_process(int, int, int);
void run_parent_process(int, int, int*, int);

int main(int argc, char** argv) {
	if (argc < 2) {
		printf("Usage: %s num1 num2 num3 ...\n", argv[0]);
		return 1;
	}

	int n = argc - 1;
	int* arr = malloc(n * sizeof(int));
	if (arr == NULL) {
		perror("Memory allocation failed");
		return 1;
	}

	for (int i = 0; i < n; i++) {
		arr[i] = atoi(argv[i + 1]);
	}

	int pipe_1[2] = {}, pipe_2[2] = {};
	if (pipe(pipe_1) == -1 || pipe(pipe_2) == -1) {
		perror("Pipe creation failed");
		free(arr);
		return 1;
	}

	pid_t pid = fork();
	if (pid < 0) {
		perror("Fork failed");
		free(arr);
		return 1;
	}

	if (pid > 0) {
		close(pipe_1[0]);  // Close unused read end of pipe_1
		close(pipe_2[1]);  // Close unused write end of pipe_2
		run_parent_process(pipe_1[1], pipe_2[0], arr, n);
		free(arr);
	} else {
		close(pipe_1[1]);
		close(pipe_2[0]);
		free(arr);  // Free parent's initial array copy in child
		run_child_process(pipe_1[0], pipe_2[1], n);
	}
	return 0;
}

int compare_ints(const void* a, const void* b) { return (*(int*)a - *(int*)b); }

void run_child_process(int read_fd, int write_fd, int n) {
	int* arr = malloc(n * sizeof(int));
	if (!arr) {
		perror("Memory allocation failed in child");
		exit(1);
	}

	read(read_fd, arr, n * sizeof(int));
	close(read_fd);

	qsort(arr, n, sizeof(int), compare_ints);

	write(write_fd, arr, n * sizeof(int));
	close(write_fd);

	free(arr);
	exit(0);
}

void run_parent_process(int write_fd, int read_fd, int* arr, int n) {
	write(write_fd, arr, n * sizeof(int));
	close(write_fd);

	wait(NULL);

	read(read_fd, arr, n * sizeof(int));
	close(read_fd);

	printf("Sorted array: ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}
