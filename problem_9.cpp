#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main() {

  int c = 0;
  
  for (int a = 1; a <= 1000; a++) {
    for (int b = a; b <= 1000; b++) {
      c = 1000 - a - b;
      if (c > 0) {
	if ( pow(a,2) + pow(b,2) == pow(c,2) ) {
	  cout << a << endl<< b << endl << c << endl << a*b*c << endl;
	  break;
	}
      }
    }   
  }

  return 0;
}
