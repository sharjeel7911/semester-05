/*
  w a C program in which the parent process receives an integer array through
  command-line arguments and passes it to its child process using pipe, The child process
  sorts that array (using the sorting algorithm of your choice) and return that array back to
  parent process using a separate pipe. The parent processes finally prints that sorted array
  on the terminal.
*/

#include <stdio.h>      // for printf, perror
#include <stdlib.h>     // for malloc, free, atoi, qsort
#include <sys/types.h>  // for pid_t
#include <sys/wait.h>   // for wait
#include <unistd.h>     // for fork, pipe, read, write, close

#define r 0
#define w 1

int cmp_int(const void* a, const void* b) { return *(int*)a - *(int*)b; }

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

	int pfd_1[2] = {0}, pfd_2[2] = {0};
	if (pipe(pfd_1) == -1 || pipe(pfd_2) == -1) {
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
		// PARENT PROCESS
		close(pfd_1[r]);
		close(pfd_2[w]);

		// Send array to child
		w(pfd_1[w], arr, n * sizeof(int));
		close(pfd_1[w]);

		// Receive sorted array from child
		r(pfd_2[r], arr, n * sizeof(int));
		close(pfd_2[r]);

		wait(NULL);

		printf("Sorted array: ");
		for (int i = 0; i < n; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
		free(arr);
	}

	else {
		// CHILD PROCESS
		close(pfd_1[w]);
		close(pfd_2[r]);

		// Receive array from parent
		r(pfd_1[r], arr, n * sizeof(int));
		close(pfd_1[r]);

		// Sort array
		// qsort(buffer, buffer_size, sizeof(data_type), cmp_func);
		qsort(arr, n, sizeof(int), cmp_int);

		// Send sorted array to parent
		w(pfd_2[w], arr, n * sizeof(int));
		close(pfd_2[w]);

		free(arr);
		exit(0);
	}
	return 0;
}