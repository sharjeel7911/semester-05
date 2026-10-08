#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> a = {1, 2};
    vector<int> b = a; // Deep copy: 'b' gets its own memory
    b.push_back(3);    // 'a' remains {1, 2}

    // Printing 'a'
    cout << "Vector a: ";
    for (int x : a) cout << x << " ";
    
    cout << "\t";

    // Printing 'b'
    cout << "Vector b: ";
    for (int x : b) cout << x << " ";
    
    cout << endl;

    return 0;
}