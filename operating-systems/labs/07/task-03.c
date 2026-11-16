#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
	int fd[2];

	if (pipe(fd) < 0) {
		perror("pipe");
		exit(EXIT_FAILURE);
	}

	pid_t pid1 = fork();

	if (pid1 < 0) {
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (pid1 == 0) {
		close(fd[0]);

		dup2(fd[1], STDOUT_FILENO);
		close(fd[1]);

		execlp("ls", "ls", (char*)NULL);

		perror("execlp ls");
		exit(EXIT_FAILURE);
	}

	pid_t pid2 = fork();

	if (pid2 < 0) {
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (pid2 == 0) {
		close(fd[1]);

		dup2(fd[0], STDIN_FILENO);
		close(fd[0]);

		int out = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

		if (out < 0) {
			perror("open");
			exit(EXIT_FAILURE);
		}

		dup2(out, STDOUT_FILENO);
		close(out);

		execlp("sort", "sort", (char*)NULL);

		perror("execlp sort");
		exit(EXIT_FAILURE);
	}

	close(fd[0]);
	close(fd[1]);

	waitpid(pid1, NULL, 0);
	waitpid(pid2, NULL, 0);

	return 0;
}