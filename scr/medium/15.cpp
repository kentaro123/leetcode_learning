#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <iterator>
#include <string>
#include <unordered_map>

using namespace std;


vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int loop = nums.size()-2;
        set<vector<int> >vec;
        int flag=0;
        for(int i=0;i<nums.size();i++){

            int r = nums.size()-1;
            int l = (i+1);
            for(int j=l;l<r;j++){

                int sum = nums[i] + nums[l] + nums[r];

                if(sum == 0){
                    vector<int> v;
                    v.push_back(nums[i]);
                    v.push_back(nums[l]);
                    v.push_back(nums[r]);
                    vec.insert(v);
                    ++l;
                    --r;
                }
                else if(sum > 0) {

                    --r;

                }
                else if(sum < 0){
                    ++l;
                }

            }

        }

        vector<vector<int> >f;
        for(auto it=vec.begin();it!=vec.end();it++){
            f.push_back(*it);
        }

        return f;
    }
"""
int maxArea(vector<int>& height) {
        int i=0,j=height.size()-1;

        int maxarea=0;
        while(i<j){

            int area=(long)min(height[i],height[j])*(abs(i-j));

            maxarea=max(maxarea,area);

            if(height[i]<=height[j])i++;
            else j--;



        }

        return maxarea;
    }
"""

int main(){
  std::vector<int> v{1,8,6,2,5,4,8,3,7};
  std::vector<int> result = threeSum(v);
  for(int i : result){
  std::cout << i << std::endl;
}
}
