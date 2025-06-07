#include<bits/stdc++.h>

using namespace std;

int main(){
  vector<int> bk(13,0);//0～12の数字の配列 bk を用意
  for(int i=0;i<7;i++){
    int x;
    cin >> x;
    bk[x-1]++;
  }
  sort(bk.rbegin(),bk.rend());// bkを降順にソート(昇順はsort(bk.begin(),bk.end());)

  if(bk[0]>=3 && bk[1]>=2){cout << "Yes\n";}
  else{cout << "No\n";}
  return 0;
}
