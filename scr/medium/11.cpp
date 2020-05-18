#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <iterator>
#include <string>
#include <unordered_map>

using namespace std;


int maxArea(vector<int>& height) {
  int max = 0;
  int men = 0;
  for(int i=0;i<height.size();i++){
    if(max<height[i]*(height.size()-i)){
    for(int j=i;j<height.size();j++){
      if(height[i]<height[j]) men = height[i]*(j-i);
      else men = height[j]*(j-i);
      if(men>max) max=men;
    }
  }
  }
  return max;
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
  int result = maxArea(v);
  std::cout << result << std::endl;
}
