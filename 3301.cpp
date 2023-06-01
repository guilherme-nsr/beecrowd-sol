#include <iostream>
 
using namespace std;

void printSobrinhoMeio(int h, int z, int l) {
  if ((h > z && h < l) || (h < z && h > l)) {
    cout << "huguinho" << endl;
  } else if ((z > h && z < l) || (z < h && z > l)) {
    cout << "zezinho" << endl;
  } else {
    cout << "luisinho" << endl;
  }
}

int main() {
  int h, z, l;
  cin >> h >> z >> l;
  
  printSobrinhoMeio(h, z, l);

  return 0;
}