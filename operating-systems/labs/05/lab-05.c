#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

#define READ 0
#define WRITE 1

void calculate_sum(int p1[], int p2[], int n) {
	int arr[n], sum = 0;

	close(p1[WRITE]);
	close(p2[READ]);

	read(p1[READ], arr, sizeof(arr));

	for (int i = 0; i < n; i++) sum += arr[i];

	write(p2[WRITE], &sum, sizeof(sum));

	close(p1[READ]);
	close(p2[WRITE]);
	exit(0);
}

void calculate_min(int p3[], int p4[], int n) {
	int arr[n], min;

	close(p3[WRITE]);
	close(p4[READ]);

	read(p3[READ], arr, sizeof(arr));

	min = arr[0];

	for (int i = 1; i < n; i++)
		if (arr[i] < min) min = arr[i];

	write(p4[WRITE], &min, sizeof(min));

	close(p3[READ]);
	close(p4[WRITE]);
	exit(0);
}

int main(int argc, char* argv[]) {
	if (argc < 2) {
		printf("Usage: %s num1 num2 num3 ...\n", argv[0]);
		return 1;
	}

	int n = argc - 1;
	int arr[n];

	for (int i = 0; i < n; i++) arr[i] = atoi(argv[i + 1]);

	int p1[2], p2[2], p3[2], p4[2];

	if (pipe(p1) == -1 || pipe(p2) == -1 || pipe(p3) == -1 || pipe(p4) == -1) {
		perror("pipe");
		return 1;
	}

	pid_t child1 = fork();

	if (child1 == -1) {
		perror("fork");
		return 1;
	}

	if (child1 == 0) {
		close(p3[READ]);
		close(p3[WRITE]);
		close(p4[READ]);
		close(p4[WRITE]);

		calculate_sum(p1, p2, n);
	}

	pid_t child2 = fork();

	if (child2 == -1) {
		perror("fork");
		return 1;
	}

	if (child2 == 0) {
		close(p1[READ]);
		close(p1[WRITE]);
		close(p2[READ]);
		close(p2[WRITE]);

		calculate_min(p3, p4, n);
	}

	close(p1[READ]);
	close(p2[WRITE]);
	close(p3[READ]);
	close(p4[WRITE]);

	write(p1[WRITE], arr, sizeof(arr));
	write(p3[WRITE], arr, sizeof(arr));

	close(p1[WRITE]);
	close(p3[WRITE]);

	int sum, min;

	read(p2[READ], &sum, sizeof(sum));
	read(p4[READ], &min, sizeof(min));

	close(p2[READ]);
	close(p4[READ]);

	waitpid(child1, NULL, 0);
	waitpid(child2, NULL, 0);

	printf("Sum = %d\n", sum);
	printf("Minimum = %d\n", min);

	return 0;
}