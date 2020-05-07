#include <iostream>
#include <vector>
using namespace std;


int numberOfSteps (int num) {
        int sum = 0;
        while(num!=0){
            if(num%2==0)num = num/2;
            else num-=1;
            sum+=1;
        }
        return sum;
    }


int main(){
  int num = 14;
  std::cout << numberOfSteps(num) << '\n';
}
