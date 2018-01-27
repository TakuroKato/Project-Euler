#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int main() {

  for (long x = 21;;x++) {
    int flag = 1;
    for (int i = 1; i <= 20; i++) {
      if (x % i != 0) {
	flag = 0;
	break;
      }
    }

    if (flag == 1) {
      cout << x << endl;
      break;
    }
  }
  
  return 0;
}
