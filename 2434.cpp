#include <iostream>

using namespace std;

int main() {
  
  int n, saldo;

  cin >> n >> saldo;

  int mov, menor;
  menor = saldo;

  for (int i = 0; i < n; i++) {
    cin >> mov;

    saldo = saldo + mov;

    if (saldo < menor) {
      menor = saldo;
    }
  }

  cout << menor << endl;

  return 0;
}
