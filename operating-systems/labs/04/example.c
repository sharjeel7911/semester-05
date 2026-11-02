#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <sys/wait.h> 
#include <string.h> 
 
#define WRITE 1 
#define READ 0 
 
int main() 
{ 
    int fd[2]; 
 
    char message[] = "This is OS lab time"; 
    char buffer[100]; 
 
    pipe(fd);

    if (fork()== 0) 
    { 
        close(fd[WRITE]); 
 
        ssize_t bytesread = read(fd[READ], buffer, sizeof(buffer)); 
 
        if (bytesread > 0) 
        { 
            printf("Read %zd bytes: %s\n", bytesread, buffer); 
        } 
 
        close(fd[READ]); 
    } 
    else 
    { 
        close(fd[READ]); 
 
        write(fd[WRITE], message, strlen(message) + 1); 
 
        close(fd[WRITE]); 
 
        wait(NULL); 
    } 
 
    return 0; 
} 
