#include<string>
#include <iostream>
#include<vector>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    
    vector<char> check;
    if (s[0] == ')')
        return false;
    
    check.push_back(s[0]);
    for (int i = 1; i < s.size(); i++)
    {
        if (s[i] == ')')
        {
            if (check.size() > 0)
            {
                if (check.back() == '(')
                    check.pop_back();
                else
                    return false;
            }
            else
                return false;
        }
        else if (s[i] == '(')
            check.push_back(s[i]);
    }
    if (check.size() > 0)
        return false;

    return answer;
}