#include <iostream>
#include <vector>
#include <string>
using namespace std;


vector<int> decompressRLElist(vector<int>& nums) {
  std::vector<int> v;
  for(int i=0;i<nums.size();i+=2){
    for(int j=0;j<nums[i];j++)v.emplace_back(nums[i+1]);
  }
  return v;
}


int main(){
  std::vector<int> v = {1,2,3,4};
  std::vector<int> result = decompressRLElist(v);
  for(int i : result){
    std::cout << i << '\n';
  }
}
