#include<iostream>
#include<cstdio>
#include<cmath>
#define N 2000000
using namespace std;

long long arr[N];
long long  sum = 0;

int main (){
  for(long long i = 0; i < N; i++){
    arr[i] = 1;
  }
  for(long long i = 2; i < sqrt(N); i++){
    if(arr[i]){
      for(long long j = 0; i * (j + 2) < N; j++){
	arr[i *(j + 2)] = 0;
      }
    }
  }
  
  for(long long i = 2; i < N; i++){
    if(arr[i]){
      cout << i << endl;
      sum += i;
    }
  }

  cout << sum << endl;
  
  return 0;
}
