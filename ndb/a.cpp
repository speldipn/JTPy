#include <iostream>
#include <string>
#include <cmath>

using namespace std;


int main(void) {
    string a,b;
    cin >> a;
    cin >> b;

    int total = 0;
    for(int i = b.length()-1; i >= 0; --i) {
        int c = stoi(a) * stoi(string(1,b[i]));
        cout << c << endl;

        total += c * pow(10, b.length()-1 - i);
    }

    cout << total << endl;

    return 0;
}
