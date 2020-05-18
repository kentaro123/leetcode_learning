#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <iterator>
#include <string>
#include <unordered_map>

using namespace std;


string convert(string s, int numRows) {
  int n=s.size();
  if(n<numRows || numRows==1) return s;
  int num = numRows*2-2;
  string hash[numRows];
  for(int i=0;i<n;i+=num){
    for(int j=0;j<num && i+j<n;j++){
      if(j<numRows) hash[j] += s[i+j];
      else hash[2*numRows-2-j] += s[i+j];
    }
  }
  string result;
  for(int i=0;i<numRows;i++){
    result += hash[i];
  }
  return result;
}

int main(){
  string s = "ABAB";
  int a = 2;
  string result = convert(s,a);
  std::cout << result << std::endl;
}
