#include <iostream>
using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;

void runCaesar();
void runVigenere();
void runAutoKey();

string caesarEncrypt(string text, int key);
string caesarDecrypt(string text, int key);

string vigenereEncrypt(string text, string key);
string vigenereDecrypt(string text, string key);

string autoKeyEncrypt(string text, string key);
string autoKeyDecrypt(string text, string key);

// ==================================================

int main() {
  int choice;
  while (true) {
	  cout << "1. Caesar Cipher" << endl;
	  cout << "2. Vigenere Cipher" << endl;
	  cout << "3. Autokey Cipher" << endl;
	  cout << "Enter choice: ";
	  cin >> choice;
	  cin.ignore();

	  if (choice == 1) runCaesar();
	  else if (choice == 2) runVigenere();
	  else if (choice == 3) runAutoKey();
	  else cout << "Invalid choice." << endl;

	  cout << "Continue? (y/n): ";
	  char cont;
	  cin >> cont;
	  cin.ignore();
	  if (cont != 'y') break;
  }
  return 0;
}

// ==================================================

void runCaesar() {
  string text;
  int key;

  cout << "\n--- Caesar Cipher ---" << endl;

  cout << "Enter text: ";
  getline(cin, text);

  cout << "Enter key (integer): ";
  cin >> key;
  cin.ignore();

  string encrypted = caesarEncrypt(text, key);
  string decrypted = caesarDecrypt(encrypted, key);

  cout << "Encrypted: " << encrypted << endl;
  cout << "Decrypted: " << decrypted << endl;
}
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

// ==================================================

void runVigenere() {
  string text;
  string key;

  cout << "\n--- Vigenere Cipher ---" << endl;

  cout << "Enter text: ";
  getline(cin, text);

  cout << "Enter key (string): ";
  cin >> key;
  cin.ignore();

  string encrypted = vigenereEncrypt(text, key);
  string decrypted = vigenereDecrypt(encrypted, key);

  cout << "Encrypted: " << encrypted << endl;
  cout << "Decrypted: " << decrypted << endl;
}
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

// ==================================================

void runAutoKey() {
  string text;
  string key;

  cout << "\n--- Autokey Cipher ---" << endl;

  cout << "Enter text: ";
  getline(cin, text);

  cout << "Enter key (string): ";
  cin >> key;
  cin.ignore();

  string encrypted = autoKeyEncrypt(text, key);
  string decrypted = autoKeyDecrypt(encrypted, key);

  cout << "Encrypted: " << encrypted << endl;
  cout << "Decrypted: " << decrypted << endl;
}
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