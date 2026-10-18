#include <algorithm>
#include <array>
#include <cctype>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;

const array<double, 26> ENG_PCT = {8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07};

// Score decrypted text by counting common English words
int scoreText(const string& text) {
	static const vector<pair<string, int>> words = {{"THE", 5}, {"AND", 4}, {"THAT", 4}, {"THIS", 3}, {"WITH", 3}, {"ION", 3}, {"TION", 3}, {"ING", 3}, {"ENT", 3}, {"HER", 3}, {"HIS", 3}, {"ARE", 2}, {"FOR", 2}, {"HAVE", 2}, {"FROM", 2}, {"NOT", 2}, {"YOU", 2}};
	int s = 0;
	for (const auto& [w, wt] : words) {
		size_t pos = text.find(w);
		while (pos != string::npos) {
			s += wt;
			pos = text.find(w, pos + 1);
		}
	}
	return s;
}

// key[cipherIndex] = plaintext letter
string decrypt(const string& cipher, const array<char, 26>& key) {
	string out = cipher;
	for (char& c : out) {
		if (isalpha(static_cast<unsigned char>(c))) {
			char u = toupper(static_cast<unsigned char>(c));
			c = key[u - 'A'];
		}
	}
	return out;
}

int main1() {
	string cipher;
	cout << "Enter ciphertext: ";
	getline(cin, cipher);
	for (char& c : cipher) c = toupper(static_cast<unsigned char>(c));

	// 1. Count cipher letters and convert to percentages
	array<int, 26> count{};
	int total = 0;
	for (char c : cipher)
		if (isalpha(static_cast<unsigned char>(c))) {
			count[c - 'A']++;
			total++;
		}

	array<double, 26> cipherPct{};
	for (int i = 0; i < 26; i++) cipherPct[i] = total ? 100.0 * count[i] / total : 0.0;

	// 2. Sort cipher letters and English letters by frequency
	array<int, 26> cOrder, eOrder;
	for (int i = 0; i < 26; i++) cOrder[i] = eOrder[i] = i;
	sort(cOrder.begin(), cOrder.end(), [&](int a, int b) { return count[a] > count[b]; });
	sort(eOrder.begin(), eOrder.end(), [&](int a, int b) { return ENG_PCT[a] > ENG_PCT[b]; });

	// 3. Initial key: most frequent cipher letter -> most frequent English letter
	array<char, 26> key{};
	for (int i = 0; i < 26; i++) key[cOrder[i]] = static_cast<char>('A' + eOrder[i]);

	// 4. Hill climbing: swap key entries, keep changes that improve the score
	mt19937 rng(12345);
	array<char, 26> bestKey = key;
	int bestScore = scoreText(decrypt(cipher, key));

	for (int restart = 0; restart < 20; restart++) {
		array<char, 26> cur = (restart == 0) ? key : bestKey;
		if (restart > 0) shuffle(cur.begin(), cur.end(), rng);
		int curScore = scoreText(decrypt(cipher, cur));

		for (int step = 0; step < 5000; step++) {
			int a = rng() % 26, b = rng() % 26;
			if (a == b) continue;
			swap(cur[a], cur[b]);
			int s = scoreText(decrypt(cipher, cur));
			if (s >= curScore) {
				curScore = s;
			} else {
				swap(cur[a], cur[b]);  // revert
			}
		}
		if (curScore > bestScore) {
			bestScore = curScore;
			bestKey = cur;
		}
	}

	// 5. Output
	cout << "\nCipher  Cipher%  English%  Plain\n";
	for (int i = 0; i < 26; i++) {
		if (count[i] == 0) continue;
		char c = 'A' + i;
		cout << "  " << c << "      " << cipherPct[i] << "%      " << ENG_PCT[bestKey[i] - 'A'] << "%     " << bestKey[i] << "\n";
	}
	cout << "\nDecrypted: " << decrypt(cipher, bestKey) << "\n";
	return 0;
}

// ===========================================================

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