#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <iterator>
#include <string>

using namespace std;


string longestPalindrome(string s) {
  if(s.empty()) return "";
  int max = 0;
  string ans;
  ans+=s[0];
  for(int start=0;start<s.size();start++){
    for(int i=s.size()-1;i>start+max;i--){
      if(s[start]==s[i] && max<(i-start+1)){
        string memo  = s.substr(start,i-start+1);
        string memo_rev = memo;
        reverse(memo_rev.begin(),memo_rev.end());
        if(memo==memo_rev){
          max = i-start+1;
          ans = memo;
          break;
        }
      }
    }
  }
  return ans;
}
"""
模範解答
string longestPalindrome(string s) {
  int n=s.size();
  if(n==0 || n==1) return s;
  int maxlen=1;
  int low,high;
  int start=0;
  for(int i=1;i<n;i++){
    low=i-1;
    high=i;
    while(low>=0 && high<n && s[low]==s[high]){
      if(high-low+1>maxlen){
        start=low;
        maxlen=high-low+1;
      }
      --low;
      ++high;
    }
    low=i-1;
    high=i+1;
    while(low>=0 && high<n && s[low]==s[high]){
      if(high-low+1>maxlen){
        start=low;
        maxlen=high-low+1;
      }
      --low;
      ++high;
    }
  }
  return s.substr(start,maxlen);
}

"""


int main(){
  string s = "abcdbbfcba";
  string result = longestPalindrome(s);
  std::cout << result << std::endl;
}
