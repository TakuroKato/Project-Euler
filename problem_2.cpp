#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main() {
  int f1 = 1, f2 = 2, f3 = 0;

  int sum = 2;
  for (int i = 0; f3 < 4000000; i++) {
    f3 = f2 + f1;
    if (f3 % 2 == 0) {
      sum += f3;
    }

    f1 = f2;
    f2 = f3;
    
  }

  cout << sum << endl;
 
  return 0;
}
