#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <iterator>
using namespace std;


ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
  for_each(l1.rbegin(),l1.rend());
  for_each(l2.rbegin(),l2.rend());
  list<int>::iterator itr;
  int sum1 = 0;
  int sum2 = 0;
  for(itr= l1.begin();itr!=l1.end();itr++){
    sum1+=*itr;
  }
  for(itr= l2.begin();itr!=l2.end();itr++){
    sum2+=*itr;
  }
  int sum = sum1+sum2;
  list<string> result;
  while(sum!=0){
    result.push_back(sum%10);
    sum /=10;
  }

  return result;

}


int main(){
  list<string> l1{2,4,3};
  list<string> l2{5,6,4};
  list<string> result = addTwoNumbers(l1,l2);
  std::list<std::string>::iterator itr;

  for (itr = result.begin(); itr != result.end(); itr++) {
    std::cout << *itr << std::endl;
  }
}
