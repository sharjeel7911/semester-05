#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
	pid_t pid = fork();

	if (pid < 0) {
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (pid == 0) {
		int fd = open("location.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

		if (fd < 0) {
			perror("open");
			exit(EXIT_FAILURE);
		}

		dup2(fd, STDOUT_FILENO);
		close(fd);

		execlp("pwd", "pwd", (char*)NULL);

		perror("execlp");
		exit(EXIT_FAILURE);
	}
	wait(NULL);
	return 0;
}