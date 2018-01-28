#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

long ac(long m, long n) {
  if(m == 0) return n+1;
  if(n == 0) return ac(m-1,1);
  return ac(m-1,ac(m,n-1));
}

int main() {
  long a = 0, b = 0;
  cin >> a >> b;
  cout << ac(a,b) << endl;  
  return 0;
}
