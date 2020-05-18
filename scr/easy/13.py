import numpy as np
def romanToInt(s):
    num=0
        for i in range(len(s)):
            if s[i]=='M':
                if i>0 and s[i-1]=='C':
                    num+=900-100
                else:
                    num+=1000
            if s[i]=='D':
                if i>0 and s[i-1]=='C':
                    num+=400-100
                else:
                    num+=500
            if s[i]=='L':
                if i>0 and s[i-1]=='X':
                    num+=40-10
                else:
                    num+=50

            if s[i]=='C':
                if i>0 and s[i-1]=='X':
                    num+=90-10
                else:
                    num+=100
            if s[i]=='V':
                if i>0 and s[i-1]=='I':
                    num+=4-1
                else:
                    num+=5
            if s[i]=='X':
                if i>0 and s[i-1]=='I':
                    num+=9-1
                else:
                    num+=10
            if s[i]=='I':
                num+=1


        return num

print(intToRoman("III"))
