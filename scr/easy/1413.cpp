#include <iostream>
#include <vector>
using namespace std;



vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
  int n = candies.size();
  int ma = candies[0];
  for(int i=1;i<n;i++) ma = max(ma,candies[i]);

  vector<bool> ans(n,false);
  for(int i=0;i<n;i++){
    if(ma-candies[i]<=extraCandies) ans[i]=true;
  }
  return ans;
}


int main(){
  vector<int> candies={2,3,1,5,3};
  int extraCandies = 3;
  vector<bool> ans = kidsWithCandies(candies,extraCandies);
  for(bool i : ans){
    std::cout << i << '\n';
  }
}
