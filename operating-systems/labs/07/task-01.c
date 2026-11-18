/*
  $ ls > files.txt
*/

/*
  STDIN_FILENO = 0
  STDOUT_FILENO = 1
  STDERR_FILENO = 2
*/

#include <fcntl.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
	pid_t pid = fork();

	if (pid < 0) {
		perror("fork");
		return 1;
	}

	if (pid == 0) {
		int fd = open("file.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

		if (fd < 0) {
			perror("open");
			return 1;
		}

		dup2(fd, 1);
		close(fd);

		execlp("ls", "ls", NULL);
		perror("execlp");
		return 1;
	}

	wait(NULL);

	return 0;
}