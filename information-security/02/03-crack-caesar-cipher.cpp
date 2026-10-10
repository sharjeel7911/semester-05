// Global Space
#include <algorithm>
#include <cctype>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;
using std::vector;

// ====================================================================================================

// Approach - 01
void breakCaesarCipher(const string&);

// ====================================================================================================

// Approach - 02

// Expected English letter frequencies (in percentage) for A..Z
static const double ENGLISH_FREQ[26] = {8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074};

struct Candidate {
	int key;
	double score;
	string plaintext;
};

string caesarShift(const string&, int);
vector<int> letterCounts(const string&);
double chiSquared(const string&);
int guessKeyFromMostFrequent(const string&);

// ====================================================================================================

// Main Function
int main(int argc, char* argv[]) {
	string cipher;
	if (argc > 1) {
		for (int i = 1; i < argc; ++i) {
			if (i > 1) cipher += ' ';
			cipher += argv[i];
		}
	} else {
		cout << "Enter ciphertext: ";
		getline(cin, cipher);
	}

	int choice = 0;

	while (choice != 3) {
		cout << "\n========== Caesar Cipher Breaker ==========\n";
		cout << "1. Brute-Force Decryption (All 26 Keys)\n";
		cout << "2. Statistical Cryptanalysis (Frequency + Chi-Squared)\n";
		cout << "3. Exit\n";
		cout << "Enter choice: ";

		if (!(cin >> choice)) {
			cin.clear();
			cin.ignore(10000, '\n');
			cout << "Invalid input.\n";
			continue;
		}
		cin.ignore(10000, '\n');

		switch (choice) {
			case 1:
				breakCaesarCipher(cipher);
				break;

			case 2: {
				int guessKey = guessKeyFromMostFrequent(cipher);

				cout << "\n== Naive Frequency Guess ==\n";
				cout << "Key " << guessKey << ": " << caesarShift(cipher, -guessKey) << '\n';

				vector<Candidate> candidates;

				for (int key = 0; key < 26; ++key) {
					string plaintext = caesarShift(cipher, -key);
					candidates.push_back({key, chiSquared(plaintext), plaintext});
				}

				sort(candidates.begin(), candidates.end(), [](const Candidate& a, const Candidate& b) { return a.score < b.score; });

				cout << "\n== Top Candidates (Lower Chi-Squared Is Better) ==\n";

				const int TOP_N = 3;

				for (int i = 0; i < TOP_N && i < static_cast<int>(candidates.size()); ++i) {
					cout << std::setw(2) << i + 1 << ". Key=" << std::setw(2) << candidates[i].key << "  Chi2=" << std::fixed << std::setprecision(2) << candidates[i].score << "  \"" << candidates[i].plaintext << "\"\n";
				}

				if (!candidates.empty()) {
					cout << "\nMost Probable Key: " << candidates[0].key << '\n';
					cout << "Recovered Plaintext: " << candidates[0].plaintext << '\n';
				}

				break;
			}

			case 3:
				cout << "Exiting...\n";
				break;

			default:
				cout << "Invalid choice. Please enter 1, 2, or 3.\n";
		}
	}
	return 0;
}

// ====================================================================================================

void breakCaesarCipher(const string& cipher) {
	cout << "\n--- Possible Decryptions ---\n";

	for (int shift = 0; shift < 26; shift++) {
		string decryptedText = "";

		for (char c : cipher) {
			if (isupper(c)) {
				// Shift uppercase letters backwards
				char decryptedChar = (c - 'A' - shift + 26) % 26 + 'A';
				decryptedText += decryptedChar;
			} else if (islower(c)) {
				// Shift lowercase letters backwards
				char decryptedChar = (c - 'a' - shift + 26) % 26 + 'a';
				decryptedText += decryptedChar;
			} else {
				// Keep spaces, punctuation, and numbers unchanged
				decryptedText += c;
			}
		}

		// Output the result for the current shift
		cout << "Shift " << (shift < 10 ? " " : "") << shift << ": " << decryptedText << endl;
	}
}

// ====================================================================================================

// Shift all letters by `shift` positions (mod 26). Case and non-letters are preserved.
string caesarShift(const string& text, int shift) {
	string out = text;
	int s = ((shift % 26) + 26) % 26;
	for (char& c : out) {
		if (isalpha(static_cast<unsigned char>(c))) {
			char base = isupper(static_cast<unsigned char>(c)) ? 'A' : 'a';
			c = base + (c - base + s) % 26;
		}
	}
	return out;
}

// Count letters (case-insensitive) into a 26-slot histogram
vector<int> letterCounts(const string& text) {
	vector<int> counts(26, 0);
	for (unsigned char c : text) {
		if (isalpha(c)) counts[tolower(c) - 'a']++;
	}
	return counts;
}

// Chi-squared statistic: lower means the letter distribution looks more like English
double chiSquared(const string& text) {
	vector<int> counts = letterCounts(text);
	int total = 0;
	for (int c : counts) total += c;
	if (total == 0) return 1e18;

	double chi = 0.0;
	for (int i = 0; i < 26; ++i) {
		double expected = total * ENGLISH_FREQ[i] / 100.0;
		double diff = counts[i] - expected;
		chi += diff * diff / expected;
	}
	return chi;
}

// Classic frequency-analysis guess: assume the most common letter is 'E'
int guessKeyFromMostFrequent(const string& cipher) {
	vector<int> counts = letterCounts(cipher);
	int maxIdx = static_cast<int>(max_element(counts.begin(), counts.end()) - counts.begin());
	return ((maxIdx - ('E' - 'A')) % 26 + 26) % 26;
}