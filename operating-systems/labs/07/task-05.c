/*
  $ ls -l 2> error.txt | sort | less
*/

#include <fcntl.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

#define r 0
#define w 1

int main() {
	int fd1[2], fd2[2];

	if (pipe(fd1) < 0 || pipe(fd2) < 0) {
		perror("pipe");
		return 1;
	}

	pid_t pid1 = fork();

	if (pid1 < 0) {
		perror("fork");
		return 1;
	}

	if (pid1 == 0) {
		close(fd1[r]);
		close(fd2[r]);
		close(fd2[w]);

		int err = open("error.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

		if (err < 0) {
			perror("open error.txt");
			return 1;
		}

		dup2(err, 2);
		dup2(fd1[w], 1);

		close(err);
		close(fd1[w]);

		execlp("ls", "ls", "-l", NULL);
		perror("execlp ls");
		return 1;
	}

	pid_t pid2 = fork();

	if (pid2 < 0) {
		perror("fork");
		return 1;
	}

	if (pid2 == 0) {
		close(fd1[w]);
		close(fd2[r]);

		dup2(fd1[r], 0);
		dup2(fd2[w], 1);

		close(fd1[r]);
		close(fd2[w]);

		execlp("sort", "sort", NULL);
		perror("execlp sort");
		return 1;
	}

	pid_t pid3 = fork();

	if (pid3 < 0) {
		perror("fork");
		return 1;
	}

	if (pid3 == 0) {
		close(fd1[0]);
		close(fd1[1]);
		close(fd2[1]);

		dup2(fd2[r], 0);
		close(fd2[r]);

		execlp("less", "less", NULL);
		perror("execlp less");
		return 1;
	}

	close(fd1[r]);
	close(fd1[w]);
	close(fd2[r]);
	close(fd2[w]);

	wait(NULL);
	wait(NULL);
	wait(NULL);

	return 0;
}