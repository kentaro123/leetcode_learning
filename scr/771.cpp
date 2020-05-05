#include <iostream>
#include <vector>
#include <string>
using namespace std;


int numJewelsInStones(string J, string S) {
        int sum=0;
        for(int i=0;i<J.size();i++){
            for(int j=0;j<S.size();j++){
                if(J[i]==S[j]) sum+=1;
            }
        }
        return sum;
    }


int main(){
  string J = "aA";
  string S = "aAAbbbb";
  std::cout << numJewelsInStones(J,S) << '\n';
}
