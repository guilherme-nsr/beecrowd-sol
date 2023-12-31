#include <iostream>
 
using namespace std;
 
int main() {
 
  int n, m;
  string acao;

  cin >> n >> m;

  for (int i = 0; i < m; ++i) {
    cin >> acao;

    if (acao == "fechou") {
      n -= 1;
      n += 2;
    } else {
      n -= 1;
    }
  }

  cout << n << endl;

  return 0;
}