#include <iostream>

using namespace std;

int main() {
  string palavra;
  cin >> palavra;

  if (palavra.length() >= 10)
    cout << "palavrao" << endl;
  else
    cout << "palavrinha" << endl;

  return 0;
}