#include <iostream>

using namespace std;

int main() {
  int n, h, b, a, m, d;
  string e, g;

  cin >> n;

  b = 0;
  a = 0;
  m = 0;
  d = 0;

  for (int i = 0; i < n; i++) {
    cin >> e >> g >> h;
    
    if (g == "bonecos") {
      b = b + h;
    } else if (g == "arquitetos") {
      a = a + h;
    } else if (g == "musicos") {
      m = m + h;
    } else if (g == "desenhistas") {
      d = d + h;
    }
  }

  int p = 0;
  p = p + b / 8;
  p = p + a / 4;
  p = p + m / 6;
  p = p + d / 12;

  cout << p << endl;

  return 0;
}