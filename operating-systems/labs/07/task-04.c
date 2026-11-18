/*
  $ grep “m” < input.txt | sort > output.txt
*/

#include <fcntl.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

#define r 0
#define w 1

int main() {
	int fd[2];

	if (pipe(fd) < 0) {
		perror("pipe");
		return 1;
	}

	pid_t pid1 = fork();

	if (pid1 < 0) {
		perror("fork");
		return 1;
	}

	if (pid1 == 0) {
		close(fd[r]);

		int in = open("input.txt", O_RDONLY);

		if (in < 0) {
			perror("open input.txt");
			return 1;
		}

		dup2(in, 0);
		dup2(fd[w], 1);

		close(in);
		close(fd[r]);

		execlp("grep", "grep", "m", NULL);
		perror("execlp grep");
		return 1;
	}

	pid_t pid2 = fork();

	if (pid2 < 0) {
		perror("fork");
		return 1;
	}

	if (pid2 == 0) {
		close(fd[w]);

		dup2(fd[r], 0);
		close(fd[r]);

		int out = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

		if (out < 0) {
			perror("open output.txt");
			return 1;
		}

		dup2(out, 1);
		close(out);

		execlp("sort", "sort", NULL);
		perror("execlp sort");
		return 1;
	}

	close(fd[r]);
	close(fd[w]);

	wait(NULL);
	wait(NULL);

	return 0;
}