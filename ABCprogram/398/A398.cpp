#include<bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin >> n;

  if(n%2 == 0){
    int c = (n-2)/2;
    cout << string(c,'-') + "==" + string(c,'-') << endl;
  }else{
    int c = (n-1)/2;
    cout << string(c,'-') + "=" + string(c,'-') << endl;
  }
}
