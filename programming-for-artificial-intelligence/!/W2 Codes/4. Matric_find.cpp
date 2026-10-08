#include <iostream>
#include <vector>

int main() {
    int matrix[3][3] = {{1, 6, 2}, {8, 3, 7}, {4, 9, 5}};
    std::vector<int> results;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (matrix[i][j] > 5) {
                results.push_back(matrix[i][j]);
            }
        }
    }
    // Result: {6, 8, 7, 9}
    return 0;
}
