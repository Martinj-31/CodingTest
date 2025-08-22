#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> done;
    
    for (int i = 0; i < progresses.size(); i++)
        done.push_back(static_cast<int>(ceil((100.0 - progresses[i]) / speeds[i])));
    
    int d = 1;
    int cur = done[0];
    for (int i = 1; i < done.size(); i++)
    {
        if (done[i] <= cur)
        {
            d += 1;
            if (i == done.size() - 1)
                answer.push_back(d);
        }
        else if (done[i] > cur)
        {
            answer.push_back(d);
            d = 1;
            cur = done[i];
            if (i == done.size() - 1)
                answer.push_back(d);
        }
        
    }
    return answer;
}