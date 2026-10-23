#include <bits/stdc++.h>

#include <vector>
// #include <iostream>
// #include <vector>
// #include <string>
// #include <algorithm> sort(), reverse(), max(), min()
// #include <cmath>	Math functions (sqrt, pow, abs)
// #include <map> Sorted key-value pairs
// #include <unordered_map>	Hash-based key-value pairs
// #include <set>	Sorted unique elements
// #include <unordered_set>	Hash-based unique elements
// #include <stack>	Stack data structure
// #include <queue>	Queue and priority queue
// #include <deque>	Double-ended queue
// #include <list>	Doubly linked list
// #include <forward_list>	Singly linked list
// #include <utility>	pair, swap, and other utilities
// #include <numeric>	accumulate(), iota(), gcd()
// #include <climits>	Integer limits (INT_MAX, INT_MIN)
// #include <limits>	Numeric limits for different types
// #include <cstring>	C-style string and memory functions
// #include <cctype>	Character functions (isdigit, tolower)

using namespace std;

vector<int> v = {1, 3, 4};

// 1. Caesar Cipher
string caesarEncrypt(string text, int key) {
	for (char& c : text) {
		if (isalpha(c)) {
			char base = isupper(c) ? 'A' : 'a';
			c = (c - base + key) % 26 + base;
		}
	}
	return text;
}

string caesarDecrypt(string text, int key) {
	for (char& c : text) {
		if (isalpha(c)) {
			char base = isupper(c) ? 'A' : 'a';
			c = (c - base - key + 26) % 26 + base;
		}
	}
	return text;
}

// ====================================================================================================
// ====================================================================================================
// ====================================================================================================

// 2. Vigenere Cipher
string vigenereEncrypt(string text, string key) {
	int j = 0;
	for (char& c : text) {
		if (isalpha(c)) {
			char base = isupper(c) ? 'A' : 'a';
			int shift = tolower(key[j]) - 'a';

			c = ((c - base) + shift) % 26 + base;
			j = (j + 1) % key.length();
		}
	}
	return text;
}

string vigenereDecrypt(string text, string key) {
	int j = 0;
	for (char& c : text) {
		if (isalpha(c)) {
			char base = isupper(c) ? 'A' : 'a';
			int shift = tolower(key[j]) - 'a';

			c = ((c - base) - shift + 26) % 26 + base;
			j = (j + 1) % key.length();
		}
	}
	return text;
}

// ====================================================================================================
// ====================================================================================================
// ====================================================================================================

// 3. Auto-Key Cipher
string autoKeyEncrypt(string text, string key) {
	int j = 0;
	string keyStream = key;
	for (char& c : text) {
		if (isalpha(c)) {
			char original = c;
			char base = isupper(c) ? 'A' : 'a';
			int shift = tolower(keyStream[j]) - 'a';

			c = ((c - base) + shift) % 26 + base;
			keyStream += tolower(original);
			j++;
		}
	}
	return text;
}
string autoKeyDecrypt(string text, string key) {
	int j = 0;
	string keyStream = key;
	for (char& c : text) {
		if (isalpha(c)) {
			char base = isupper(c) ? 'A' : 'a';
			int shift = tolower(keyStream[j]) - 'a';

			c = ((c - base) - shift + 26) % 26 + base;
			keyStream += tolower(c);
			j++;
		}
	}
	return text;
}

// ====================================================================================================
// ====================================================================================================
// ====================================================================================================

#include <cctype>
#include <string>
#include <vector>

using namespace std;

// Generate 25-char key matrix (combining I and J)
string prepareKey(string key) {
	string cleaned = "";
	for (char c : key) {
		if (isalpha(c)) {
			c = toupper(c);
			if (c == 'J') {
				c = 'I';
			}
			if (cleaned.find(c) == string::npos) {
				cleaned += c;
			}
		}
	}

	for (char i = 'A'; i <= 'Z'; i++) {
		if (i == 'J') continue;
		if (cleaned.find(i) == string::npos) {
			cleaned += i;
		}
	}
	return cleaned;
}

// Prepare plaintext (handle double letters & odd lengths)
string prepareText(string text) {
	string clean = "";
	for (char c : text) {
		if (isalpha(c)) {
			char u = toupper(c);
			if (u == 'J') u = 'I';
			clean += u;
		}
	}
	string prepared = "";
	for (size_t i = 0; i < clean.length(); i++) {
		prepared += clean[i];
		if (i + 1 < clean.length()) {
			if (clean[i] == clean[i + 1]) {
				prepared += 'X';
			} else {
				prepared += clean[i + 1];
				i++;
			}
		}
	}
	if (prepared.length() % 2 != 0) prepared += 'X';
	return prepared;
}
vector<pair<char, char>> prepareText(const string& text, bool encrypt) {
	string clean = "";
	for (char c : text) {
		if (isalpha(c)) {
			char u = toupper(c);
			clean += (u == 'J') ? 'I' : u;
		}
	}

	vector<pair<char, char>> pairs;
	size_t i = 0;
	while (i < clean.size()) {
		char a = clean[i];

		if (!encrypt) {
			if (clean.size() % 2 != 0) {
				clean += 'X';
			}

			if (i + 1 < clean.size()) {
				pairs.push_back({a, clean[i + 1]});
			}
			i += 2;
		} else if (i + 1 >= clean.size() || clean[i] == clean[i + 1]) {
			pairs.push_back({a, a == 'X' ? 'Q' : 'X'});
			i++;
		} else {
			pairs.push_back({a, clean[i + 1]});
			i += 2;
		}
	}
	return pairs;
}

// Find row and column of a character in the matrix
pair<int, int> findPos(const string& matrix, char c) {
	int idx = matrix.find(c);
	return {idx / 5, idx % 5};
}

// Playfair Encryption & Decryption
string playFair(const string& text, const string& key, bool encrypt) {
	string matrix = prepareKey(key);
	int shift = encrypt ? 1 : 4;
	string result = "";

	vector<pair<char, char>> pairs = prepareText(text, encrypt);

	for (auto [a, b] : pairs) {
		auto [r1, c1] = findPos(matrix, a);
		auto [r2, c2] = findPos(matrix, b);

		if (r1 == r2) {
			result += matrix[r1 * 5 + (c1 + shift) % 5];
			result += matrix[r2 * 5 + (c2 + shift) % 5];
		} else if (c1 == c2) {
			result += matrix[((r1 + shift) % 5) * 5 + c1];
			result += matrix[((r2 + shift) % 5) * 5 + c2];
		} else {
			result += matrix[r1 * 5 + c2];
			result += matrix[r2 * 5 + c1];
		}
	}
	return result;
}

// int main() {
// 	string text = "MONARCHY";
// 	string key = "KEYWORD";
//
// 	string encrypted = playFair(text, key, true);
// 	string decrypted = playFair(encrypted, key, false);
//
// 	cout << "Plaintext:  " << text << "\n";
// 	cout << "Encrypted:  " << encrypted << "\n";
// 	cout << "Decrypted:  " << decrypted << "\n";
//
// 	return 0;
// }

// ====================================================================================================
// ====================================================================================================
// ====================================================================================================

// #include <algorithm>
// #include <cctype>
// #include <iostream>
// #include <string>
// #include <vector>
//
// using namespace std;
//
// const double ENGLISH_FREQ[26] = {8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.09, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07};
//
// struct Candidate {
// 	int key;
// 	double score;
// 	string text;
// };
//
// string shift(string text, int s) {
// 	s = (s % 26 + 26) % 26;
// 	for (char& c : text) {
// 		if (isalpha(c)) {
// 			char b = isupper(c) ? 'A' : 'a';
// 			c = b + (c - b + s) % 26;
// 		}
// 	}
// 	return text;
// }
//
// double chiSquared(const string& text) {
// 	vector<int> counts(26, 0);
// 	int total = 0;
// 	for (char c : text) {
// 		if (isalpha(c)) {
// 			counts[tolower(c) - 'a']++;
// 			total++;
// 		}
// 	}
// 	if (total == 0) return 1e18;
// 	double chi = 0;
// 	for (int i = 0; i < 26; ++i) {
// 		double exp = total * ENGLISH_FREQ[i] / 100.0;
// 		chi += (counts[i] - exp) * (counts[i] - exp) / exp;
// 	}
// 	return chi;
// }
//
// int main() {
// 	string cipher;
// 	cout << "Enter ciphertext: ";
// 	getline(cin, cipher);
//
// 	vector<Candidate> candidates;
// 	for (int key = 0; key < 26; ++key) {
// 		string plain = shift(cipher, -key);
// 		candidates.push_back({key, chiSquared(plain), plain});
// 	}
//
// 	sort(candidates.begin(), candidates.end(), [](auto& a, auto& b) { return a.score < b.score; });
//
// 	cout << "\nTop 3 Candidates:\n";
// 	for (int i = 0; i < 5; ++i) {
// 		cout << i + 1 << ". Key=" << candidates[i].key << " | " << candidates[i].text << "\n";
// 	}
// 	return 0;
// }

// ====================================================================================================
// ====================================================================================================
// ====================================================================================================
