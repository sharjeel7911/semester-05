/*
Question 2: Write a C program that creates an integer array of size 10 and accepts 10 integers from the user.
Add all even numbers and subtract all odd numbers to calculate the final result. (10 marks)
Example Input: 2 5 4 7 6 3 8 1 10 9
Calculation: 2 - 5 + 4 - 7 + 6 - 3 + 8 - 1 + 10 - 9
Expected Output: Final Result: 5
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[10] = {};

    printf("Enter 10 integers.\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
    }

    int result = 0;
    for (int i = 0; i < 10; i++) {
        if (arr[i] % 2 == 0) {
            result += arr[i];
        }
        else {
            result -= arr[i];
        }
    }
    printf("Final Result: %d\n", result);
    return 0;
}