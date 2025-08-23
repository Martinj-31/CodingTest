#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(int i, int total, const vector<int>& numbers, int target) {
    if (i == numbers.size()) {
        if (total == target) {
            answer++;
        }
        return;
    }
    dfs(i + 1, total + numbers[i], numbers, target);
    dfs(i + 1, total - numbers[i], numbers, target);
}

int solution(vector<int> numbers, int target) {
    answer = 0;
    dfs(0, 0, numbers, target);
    return answer;
}