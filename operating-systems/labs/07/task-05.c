#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
	int fd1[2], fd2[2];

	if (pipe(fd1) < 0 || pipe(fd2) < 0) {
		perror("pipe");
		exit(EXIT_FAILURE);
	}

	pid_t pid1 = fork();

	if (pid1 < 0) {
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (pid1 == 0) {
		close(fd1[0]);
		close(fd2[0]);
		close(fd2[1]);

		int err = open("error.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

		if (err < 0) {
			perror("open error.txt");
			exit(EXIT_FAILURE);
		}

		dup2(err, STDERR_FILENO);
		dup2(fd1[1], STDOUT_FILENO);

		close(err);
		close(fd1[1]);

		execlp("ls", "ls", "-l", (char*)NULL);

		perror("execlp ls");
		exit(EXIT_FAILURE);
	}

	pid_t pid2 = fork();

	if (pid2 < 0) {
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (pid2 == 0) {
		close(fd1[1]);
		close(fd2[0]);

		dup2(fd1[0], STDIN_FILENO);
		dup2(fd2[1], STDOUT_FILENO);

		close(fd1[0]);
		close(fd2[1]);

		execlp("sort", "sort", (char*)NULL);

		perror("execlp sort");
		exit(EXIT_FAILURE);
	}

	pid_t pid3 = fork();

	if (pid3 < 0) {
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (pid3 == 0) {
		close(fd1[0]);
		close(fd1[1]);
		close(fd2[1]);

		dup2(fd2[0], STDIN_FILENO);
		close(fd2[0]);

		execlp("less", "less", (char*)NULL);

		perror("execlp less");
		exit(EXIT_FAILURE);
	}

	close(fd1[0]);
	close(fd1[1]);
	close(fd2[0]);
	close(fd2[1]);

	waitpid(pid1, NULL, 0);
	waitpid(pid2, NULL, 0);
	waitpid(pid3, NULL, 0);

	return 0;
}