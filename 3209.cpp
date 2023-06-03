#include <iostream>

using namespace std;

int main() {
  int n, k, qtd_tomadas;

  cin >> n;

  for (int i = 0; i < n; i++) {
    qtd_tomadas = 0;
    cin >> k;

    for (int j = 0; j < k; j++) {
      int f;
      cin >> f;

      if (j == k-1) {
        qtd_tomadas += f;
      } else {
        qtd_tomadas += f-1;
      }
    }

    cout << qtd_tomadas << endl;
  }

  return 0;
}