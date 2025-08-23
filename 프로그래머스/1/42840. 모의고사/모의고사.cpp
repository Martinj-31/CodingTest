#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> man1 = {1, 2, 3, 4, 5};
    vector<int> man2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> man3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    int man1_pt = 0;
    int man2_pt = 0;
    int man3_pt = 0;
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == man1[i % man1.size()]) {
            man1_pt++;
        }
        if (answers[i] == man2[i % man2.size()]) {
            man2_pt++;
        }
        if (answers[i] == man3[i % man3.size()]) {
            man3_pt++;
        }
    }
    vector<int> pts = {man1_pt, man2_pt, man3_pt};
    int best = *max_element(pts.begin(), pts.end());
    for (int i = 0; i < pts.size(); i++) {
        if (best <= pts[i]) {
            answer.push_back(i + 1);
        }
    }
    return answer;
}