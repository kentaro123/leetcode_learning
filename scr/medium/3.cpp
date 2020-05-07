#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <iterator>
#include <string>

using namespace std;


int lengthOfLongestSubstring(string s) {
  int max = 0;
  for(int i=0;i<s.size();i++){
    bool flag = true;
    int count = 0;
    std::vector<char> v;
    for(int k=i;flag && k<s.size();k++){
      for(int j=0;j<v.size();j++){
        if(s[k]==v[j]) flag=false;
      }
      if(flag){
        v.push_back(s[k]);
        count+=1;
      }
      else break;
    }
    std::cout << s[i] << '\n';
    std::cout << count << '\n';
    if(max<count) max=count;
  }
  return max;
}

"""
模範回答
int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> map;
        int res = 0;
        auto l = 0;
        for (auto r = 0; r < s.size(); ++r) {
            char ch = s[r];
            if (map.count(ch) == 1) {
                l = std::max(map[ch] + 1, l);
            }
            res = std::max(res, r - l + 1);
            map[ch] = r;
        }
        return res;
    }
"""


int main(){
  string s = "aab";
  int result = lengthOfLongestSubstring(s);
  std::cout << result << std::endl;
}
