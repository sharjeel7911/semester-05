#include <iostream>
#include <string>
#include <unordered_map>
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::unordered_map;

void printFrequencyTable(const string);

int main() {
	string text;
	cout << "Enter text: ";
	getline(cin, text);

	printFrequencyTable(text);
	return 0;
}

void printFrequencyTable(const string text) {
	unordered_map<char, int> frequency;

	for (char c : text) {
		if (isalpha(c)) {
			c = tolower(c);
			frequency[c]++;
		}
	}
	cout << "Character Frequency Table:" << endl;
	cout << "--------------------------" << endl;
	for (const auto& pair : frequency) {
		cout << pair.first << ": " << pair.second << endl;
	}
}