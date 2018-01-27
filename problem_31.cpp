#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main(){
  long long count = 0;

  int t = 200*100*40*20*10*4*2;
  int k = 0;

  for (int g = 0; g < 2; g++) {
    for (int f = 0; f < 4; f++) {
      for (int e = 0; e < 10; e++) {
	for (int d = 0; d < 20; d++) {
	  for (int c = 0; c < 40; c++) {
	    for (int b = 0; b < 100; b++) {
	      for (int a = 0; a < 200; a++) {
		if (a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g == 200) {
		  printf("%d,%d,%d,%d,%d,%d,%d\n",a,b,c,d,e,f,g);
		  count++;
		} else if (a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g > 200) {
		  continue;
		}
		k++;
	      }
	    }
	  }
	  printf("progress...%d/%d\n",k,t);	      
	}
      }
    }
  }

  count += 8;
  cout << count << endl;
  
  return 0;
}
