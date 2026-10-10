#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <utility>
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::getline;
using std::pair;

string cleanKey(const string&);
string cleanText(const string&);
vector<pair<char, char>> makePairs(const string&);
void createMatrix(const string&, char [5][5]);
void findPosition(char [5][5], char, int&, int&);
string transformPair(pair<char, char>, char [5][5], int);
string playFairEncrypt(const string&, const string&);
string playFairDecrypt(const string&, const string&);

int main() {
  string text;
  string key;
  char mode;

  cout << "\n--- Playfair Cipher ---" << endl;

  cout << "Encrypt or decrypt? (e/d): ";
  cin >> mode;
  cin.ignore();

  cout << "Enter text: ";
  getline(cin, text);

  cout << "Enter key: ";
  getline(cin, key);

  if (tolower(static_cast<unsigned char>(mode)) == 'd') {
    cout << "Decrypted: " << playFairDecrypt(text, key) << endl;
  }
  else {
    cout << "Encrypted: " << playFairEncrypt(text, key) << endl;
  }
  return 0;
}

// Clean key: keep letters only, J becomes I, remove duplicate letters
string cleanKey(const string& text) {
  string cleaned = "";
  for (char c : text) {
    if (isalpha(static_cast<unsigned char>(c))) {
      c = toupper(static_cast<unsigned char>(c));
      if (c == 'J') {
        c = 'I';
      }
      if (cleaned.find(c) == string::npos) {
        cleaned += c;
      }
    }
  }
  return cleaned;
}

// Clean plaintext: keep letters only, J becomes I, keep duplicates
string cleanText(const string& text) {
  string cleaned = "";
  for (char c : text) {
    if (isalpha(static_cast<unsigned char>(c))) {
      c = toupper(static_cast<unsigned char>(c));
      if (c == 'J') {
        c = 'I';
      }
      cleaned += c;
    }
  }
  return cleaned;
}

// Split text into pairs, inserting filler between repeats and at the end
vector<pair<char, char>> makePairs(const string& text) {
  vector<pair<char, char>> pairs;

  for (size_t i = 0; i < text.length();) {
    char first = text[i];
    char second;

    if (i + 1 >= text.length() || text[i] == text[i + 1]) {
      second = (first == 'X') ? 'Q' : 'X';
      i++;
    }
    else {
      second = text[i + 1];
      i += 2;
    }
    pairs.push_back({first, second});
  }
  return pairs;
}

// Build the 5x5 matrix: key letters first, then the rest of the alphabet without J
void createMatrix(const string& key, char matrix[5][5]) {
  bool used[26] = {false};
  int count = 0;

  for (char c : key) {
    if (!used[c - 'A']) {
      used[c - 'A'] = true;
      matrix[count / 5][count % 5] = c;
      count++;
    }
  }

  for (char c = 'A'; c <= 'Z'; c++) {
    if (c != 'J' && !used[c - 'A']) {
      used[c - 'A'] = true;
      matrix[count / 5][count % 5] = c;
      count++;
    }
  }
}

// Find the position of a character in the matrix
void findPosition(char matrix[5][5], char c, int& row, int& col) {
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
      if (matrix[i][j] == c) {
        row = i;
        col = j;
        return;
      }
    }
  }
}

// Transform a pair. step = 1 encrypts (shift right/down), step = 4 decrypts (shift left/up)
string transformPair(pair<char, char> p, char matrix[5][5], int step) {
  int r1, c1, r2, c2;

  findPosition(matrix, p.first, r1, c1);
  findPosition(matrix, p.second, r2, c2);

  // Same row
  if (r1 == r2) {
    return string(1, matrix[r1][(c1 + step) % 5]) + matrix[r2][(c2 + step) % 5];
  }

  // Same column
  if (c1 == c2) {
    return string(1, matrix[(r1 + step) % 5][c1]) + matrix[(r2 + step) % 5][c2];
  }

  // Rectangle: swap columns
  return string(1, matrix[r1][c2]) + matrix[r2][c1];
}

// Encrypt the plaintext using the Playfair cipher
string playFairEncrypt(const string& text, const string& key) {
  char matrix[5][5];
  createMatrix(cleanKey(key), matrix);

  string ciphertext = "";
  for (pair<char, char> p : makePairs(cleanText(text))) {
    ciphertext += transformPair(p, matrix, 1);
  }
  return ciphertext;
}

// Decrypt the ciphertext. Filler letters (X/Q) from encryption remain in the output
string playFairDecrypt(const string& text, const string& key) {
  char matrix[5][5];
  createMatrix(cleanKey(key), matrix);

  string plaintext = "";
  for (pair<char, char> p : makePairs(cleanText(text))) {
    plaintext += transformPair(p, matrix, 4);
  }
  return plaintext;
}
