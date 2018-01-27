#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

long long myPow(long long x, long long n){
  if(n == 0)
    return 1;
  if(n % 2 == 0)
    return myPow(x * x, n / 2);
  else
    return x * myPow(x, n - 1);
}

int main() {
  
  cout << myPow(3,256) << endl;

  return 0;
}
