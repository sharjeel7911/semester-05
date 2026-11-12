#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <fcntl.h> 
#include <sys/wait.h> 
int main() { 
    int fd; 
    pid_t pid; 
    pid = fork(); 
    if (pid == 0) 
    { 
        fd = open("input.txt", O_CREAT | O_TRUNC | O_RDWR, 0777); 
         dup2(fd, 1); 
        char *args[] = {"ls", NULL}; 
        execvp("ls", args); 
    } 
    else{  // Parent waits for first child 
        wait(NULL);} 
    // STEP 2: Create second child 
    
    
    
    
    pid = fork(); 
  
    if (pid == 0) 
    { 
        // Child 2: Read input.txt 
  
        fd = open("input.txt", O_RDONLY); 
  
        dup2(fd, 0); 
        char *args[] = {"wc", "-w", NULL}; 
        execvp("wc", args); 
    } 
    else 
    {  // Parent waits for second child 
        wait(NULL); 
    } 
    return 0; 
} 