#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    // 1. Initialize variables
    std::string filename = "data.txt";
    std::vector<std::string> lines; // C++ equivalent of a dynamic array
    std::string currentLine;

    // 2. Open the file
    std::ifstream file(filename);

    // 3. Check if file opened successfully
    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file!" << std::endl;
        return 1;
    }

    // 4. Read file line by line
    while (std::getline(file, currentLine)) {
        lines.push_back(currentLine);
    }

    // 5. Close the file manually (Good practice)
    file.close();

    // 6. Display the stored lines
    std::cout << "Stored " << lines.size() << " lines from file:" << std::endl;
    for (const auto& line : lines) {
        std::cout << line << std::endl;
    }

    return 0;
}