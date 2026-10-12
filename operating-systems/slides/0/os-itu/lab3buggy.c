// buggy_easy.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* get_name() {
    char *name = malloc(20);
    printf("Enter a name: ");
    scanf("%19s", name);
    return name;  
}

int main() {
    int n;
    printf("How many numbers? ");
    scanf("%d", &n);

    int *arr = malloc(n * sizeof(int));  
    printf("Enter %d numbers:\n", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

   
    int sum = 0;
    for (int i = 0; i < n - 1; i++)
        sum += arr[i];

    
    double avg = (double)sum / n;

    char *name = get_name();

    printf("Hello %s!\n", name);
    printf("Sum (WRONG): %d\n", sum);
    printf("Average (WRONG): %.2f\n", avg);

    
    return 0;
}
