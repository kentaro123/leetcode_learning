#include <iostream>
#include <vector>
#include <string>
using namespace std;


int subtractProductAndSum(int n) {
  int sum=0,pro=1;
  std::vector<int> v;
  while(n!=0){
    v.emplace_back(n%10);
    n /=10;
  }
  for(int i=0;i<v.size();i++){
    sum +=v[i];
    pro *=v[i];
  }
  return pro-sum;
}


int main(){
  int i = 234;
  int result = subtractProductAndSum(i);
  cout << result << endl;
}
