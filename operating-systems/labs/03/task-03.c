#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    if (argc <= 1) {
        printf("Less than 1 args.\n");
        return 1;
    }
    int count_even = 0;
    int count_odd = 0;
    int num = 0;
    for (int i = 1; i < argc; i++) {
        num = atoi(argv[i]);
        if (num % 2 == 0) {
            printf("Even Num: %d\n", num);
            count_even++;
        }
        else {
            printf("Odd Num: %d\n", num);
            count_odd++;
        }
    }
    printf("\n");
    printf("Odd Num Count: %d\n", count_odd);
    printf("Even Num Count: %d\n", count_even);
    printf("\n");

    // ===========   

    int sum = 0;
    for (int i = 1; i < argc; i++) {
        num = atoi(argv[i]);
        int rev = 0;
        while (num % 10 > 0) {
            int temp = num % 10;
            rev = (rev * 10) + temp;
            num = num / 10;
        }

        if (rev % 2 == 0) {
            rev = rev + i;
            sum += rev;
        }
        else {
            rev = rev - i;
            sum += rev;
        }
    }
    printf("Final Sum: %d\n", sum);
    return 0;
}