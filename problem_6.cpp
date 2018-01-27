#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main() {

  long sum = 0;
  for (int i = 1; i <= 100; i++) sum += i;

  printf("%ld\n",sum);

  long sum_s = 0;
  for (int i = 1; i <= 100; i++) sum_s += pow(i,2);

  printf("%ld\n",sum_s);

  long ans = pow(sum,2) - sum_s;
  
  printf("%ld\n", ans);
  
  return 0;
}
