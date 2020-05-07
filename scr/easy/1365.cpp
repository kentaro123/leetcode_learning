#include <iostream>
#include <vector>
#include <string>
using namespace std;


vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
  vector<int> result(nums.size(),0);
  for(int i=0;i<nums.size();i++){
    int sum=0;
    for(int j=0;j<nums.size();j++){
      if(i!=j && nums[i]>nums[j]) sum+=1;
    }
    result[i] = sum;
  }
  return result;
}


int main(){
  std::vector<int> nums = {6,5,4,8};
  std::vector<int> result = smallerNumbersThanCurrent(nums);
  for(int i : result){
    std::cout << i << '\n';
  }
}
