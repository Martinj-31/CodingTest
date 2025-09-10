#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

void dfs(int i, vector<vector<int>> &computers, vector<int> &visited) {
    visited[i] = 1;
    for (int x = 0; x < visited.size(); ++x) {
        if (visited[x] == 0 && computers[i][x] == 1) {
            dfs(x, computers, visited);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<int> visited(n, 0);
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            answer++;
            dfs(i, computers, visited);
        }
    }
    return answer;
}