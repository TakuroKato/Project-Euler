#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main() {
  long x = 600851475143;

  for (long i = 2; i < (x/2); i++) {
    if (x % i == 0) {
      cout << i << endl;
      x = x / i;
      i = 2;
    }
  }
  cout << "the answer is " << x <<endl;
  return 0;
}
