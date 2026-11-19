/*
  $ ls / -lR 2> error.txt | grep "Nov" | sort | less
*/

#include <fcntl.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

#define r 0
#define w 1

int main() {
	int fd1[2], fd2[2], fd3[2];

	if (pipe(fd1) == -1 || pipe(fd2) == -1 || pipe(fd3) == -1) {
		perror("pipe error");
		return 1;
	}

	pid_t pid1 = fork();

	if (pid1 < 0) {
		perror("fork 1 err");
		return 1;
	}

	if (pid1 == 0) {
		close(fd1[r]);

		close(fd2[r]);
		close(fd2[w]);

		close(fd3[r]);
		close(fd3[w]);

		int err = open("error.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

		if (err < 0) {
			perror("open error.txt");
			return 1;
		}

		dup2(err, 2);
		dup2(fd1[w], 1);

		close(err);
		close(fd1[w]);

		execlp("ls", "ls", "/", "-lR", NULL);
		perror("execlp 1 err");
		return 1;
	}

	pid_t pid2 = fork();

	if (pid2 < 0) {
		perror("fork 2 err");
		return 1;
	}

	if (pid2 == 0) {
		close(fd1[w]);

		close(fd2[r]);

		close(fd3[r]);
		close(fd3[w]);

		dup2(fd1[r], 0);
		dup2(fd2[w], 1);

		close(fd1[r]);
		close(fd2[w]);

		execlp("grep", "grep", "Nov", NULL);
		perror("execlp 2 err");
		return 1;
	}

	pid_t pid3 = fork();

	if (pid3 < 0) {
		perror("fork 3 err");
		return 1;
	}

	if (pid3 == 0) {
		close(fd1[w]);
		close(fd1[r]);

		close(fd2[w]);

		dup2(fd2[r], 0);
		dup2(fd3[w], 1);

		close(fd2[w]);
		close(fd3[w]);

		execlp("sort", "sort", NULL);
		perror("execlp 3 err");
		return 1;
	}

	pid_t pid4 = fork();

	if (pid4 < 0) {
		perror("fork 4 err");
		return 1;
	}

	if (pid4 == 0) {
		close(fd1[w]);
		close(fd1[r]);

		close(fd2[w]);
		close(fd2[r]);

		close(fd3[w]);

		dup2(fd3[r], 0);

		close(fd3[r]);

		execlp("less", "less", NULL);
		perror("execlp 4 err");
		return 1;
	}

	close(fd1[w]);
	close(fd1[r]);

	close(fd2[w]);
	close(fd2[r]);

	close(fd3[w]);
	close(fd3[r]);

	wait(NULL);
	wait(NULL);
	wait(NULL);
	wait(NULL);

	return 0;
}