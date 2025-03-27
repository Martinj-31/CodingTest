import sys
from collections import deque

N = int(sys.stdin.readline())

tree = {}
visited = {}
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    tree[node] = deque([left, right])
    visited[node] = 0


def reset_visited():
    for node in tree.keys():
        visited[node] = 0


def front_search(node):
    global result
    result.append(node)
    left = tree[node][0]
    if left != ".":
        if visited[left] == 0:
            front_search(left)
    right = tree[node][1]
    if right != ".":
        if visited[right] == 0:
            front_search(right)


def middle_search(node):
    global result
    if tree[node][0] == "." and tree[node][1] == ".":
        result.append(node)
        return
    left = tree[node][0]
    if left != ".":
        if visited[left] == 0:
            visited[left] = 1
            middle_search(left)
    right = tree[node][1]
    if right != ".":
        if visited[right] == 0:
            visited[right] = 1
            result.append(node)
            middle_search(right)
    elif right == ".":
        result.append(node)


def back_search(node):
    global result
    if tree[node][0] == "." and tree[node][1] == ".":
        result.append(node)
        return
    left = tree[node][0]
    if left != ".":
        if visited[left] == 0:
            visited[left] = 1
            back_search(left)
    right = tree[node][1]
    if right != ".":
        if visited[right] == 0:
            visited[right] = 1
            back_search(right)
        if left == "." or visited[left] == 1:
            visited[left] = 1
            result.append(node)
    elif right == ".":
        result.append(node)


result = []
front_search('A')
for i in result:
    print(i, end="")
print("")
reset_visited()
result = []
middle_search('A')
for i in result:
    print(i, end="")
print("")
reset_visited()
result = []
back_search('A')
for i in result:
    print(i, end="")
