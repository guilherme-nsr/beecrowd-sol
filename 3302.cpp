#include <iostream>

using namespace std;

int main() {
  int n, r;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> r;
    cout << "resposta " << i+1 << ": " << r << endl;
  }

  return 0;
}