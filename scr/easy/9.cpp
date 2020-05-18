#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <iterator>
#include <string>
#include <unordered_map>

using namespace std;


bool isPalindrome(int x) {
  int result=0,num=x;
  while(x>0){
    result = result*10 + (x%10);
    x /=10;
  }
  if(result==num) return true;
  else return false;
}

"""
bool isPalindrome(int x) {
  if(x>=0)
    {
        string s=to_string(x);

        string ss=s;
        reverse(ss.begin(),ss.end());

        if(ss==s)
        {
            return true;
        }
        else
            return false;
    }
    return false;
    }
"""


int main(){
  int s = 2147483647;
  bool result = isPalindrome(s);
  std::cout << result << std::endl;
}
