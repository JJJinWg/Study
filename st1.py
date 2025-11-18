# import time
#
# from pyrepl.commands import end
#
# start_time = time.time()
#
# for i in range(1000000):
#     result=i**2
#
# end_time=time.time()
#
# execution_time = end_time - start_time
# print(f'Execution time: {execution_time} seconds')
# ///////////////////////////////////////////////////////////
# import timeit
#
# def test_function():
#     for i in range(1000000):
#         result = i**2
#
# execution_time = timeit.timeit(test_function, number=1)
# print(f'코드 실행시간: {execution_time:.6f}초')
#///////////////////////////////////////////////////////////
# # LIST 구현
# list_ex = [3,7,6,10,38]
#
# print(len(list_ex))
# print(list_ex[3])
# list_ex.append(1000)
# print(list_ex)
#
# for i,v in enumerate(list_ex):
#     print(i,v)
#
# for i in range(len(list_ex)):
#     print(i,list_ex[i])
# for v in list_ex:
#     print(v)
#
# list_ex.sort(reverse= True)
# ///////////////////////////////
# 큐(Queue)

# from _collections import deque
#
# q = deque()
# q.append(10)
# q.append(20)
# q.append(30)
#
# print(q)
# while q:
#     print(q.popleft())
#     print(q)
# //////////////////////////////////
# # 스택(Stack(
# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
#
# # stack.pop()
# # stack.pop()
# # stack.pop()
# #
# # print(stack[-1])
#
# while stack:
#     print(stack.pop())
#///////////////////////////////////////
# # Hash table = Dictionary
#
# dic_ex = {}
# dic_ex[23516] = "장현민"
# dic_ex[23515] = "남궁호"
# dic_ex[23514] = "박기훈"
# print(dic_ex)
#
# for k, v in dic_ex.items():
#     if v == "장현민":
#         print("찾았다")
#
# if 23516 in dic_ex:
#     print("찾았다")
# else:
#     print("없다")
#////////////////////////////
# 해시 셋 (Hash set)
# hash_set = set()
# hash_set.add(2025001)
# hash_set.add(2025002)
# hash_set.add(2025003)
# hash_set.add(2025004)
# hash_set.add(2025005)
# hash_set.add(2025006)
# print(hash_set)
#
# print(2025001 in hash_set)
#//////////////////////////////
#재쉬함수 팩토리어

# def factorial(n):
#     answer = 1
#     for i in range(1,n+1):
#         answer *= i
#         print(answer)
#     return answer
# factorial(5)
#
# def factorial(n):
#     if n == 1:
#         return 1
#     answer = n * factorial(n-1)
#     return answer
# print(factorial(5))
# factorial(5)
#////////////////////////
# # 피보나치 수열
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#
#     prev = 1
#     cur = 1
#     for _ in range(2, n):
#         next = cur + prev
#         prev = cur
#         cur = next
#     return next
#
# print(fibo(10))
#
#
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)
#
# print(fibo(10))
#/////////////////////////////////////
# 완전 함수 탐색
# 2개 더해서 14되는 값 찾기
# nums = [4,9,7,5,1]
# target = 14
#
# def solution(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             print(nums[i], nums[j], nums[i] + nums[j])
#             if nums[i] + nums[j] == target:
#                 print("valid solution")
#
# solution(nums, target)
#
# # 3개 더 해서 15 찾기 자기 자신은 제외
# nums = [4,9,7,5,1]
# target = 15
#
# def solution(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if i != j and i != k and j != k:
#                     print(nums[i], nums[j], nums[k], nums[i]+nums[j]+nums[k])
#                     if nums[i]+nums[j]+nums[k] == target:
#                         print("valid solution")
#
# solution(nums, target)
#//////////////////////////////////////////
# # 동적 계획법 (Dynamic Programming, DP)
# def fibo(n):
#   memo = {}
#   # basecase
#   if n == 1 or n == 2:
#     return 1
#   if n not in memo:
#     memo[n] = fibo(n-1) + fibo(n-2)
#   return memo[n]
#   #return fibo(n-1) + fibo(n-2)
#
#
# print(fibo(7))
#/////////////////////////////////////////////
## 연결 리시트
# graph = {
#     0: [1, 3, 6],
#     1: [0, 3],
#     2: [3],
#     3: [0, 1, 2, 7],
#     4: [5],
#     5: [4, 6, 7],
#     6: [0, 5],
#     7: [3, 5]
# }
#
# for next_v in graph[0]:
#     print(next_v)
#//////////////////////////////////////////
# # 인접 행렬
# graph = [
#   [0, 1, 0, 1, 0, 0, 1, 0],
#   [1, 0, 0, 1, 0, 0, 0, 0],
#   [0, 0, 0, 1, 0, 0, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0, 1],
#   [0, 0, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 1, 1],
#   [1, 0, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 1, 0, 1, 0, 0]
# ]
#
# for i, v in enumerate(graph[0]):
#     if v == 1:
#         print(i, "번째랑 연결되어 있다!")
#///////////////////////////////////////////
# #BFS 구현
#
# from collections import deque
#
# graph = {
#   0: [1, 3, 6],
#   1: [0, 3],
#   2: [3],
#   3: [0, 1, 2, 7],
#   4: [5],
#   5: [4, 6, 7],
#   6: [0, 5],
#   7: [3, 5]
# }
#
# start_v = 0
#
# def bfs(graph, start_v):
#     q = deque()
#     visited = {}
#     q.append(start_v)
#     visited[start_v] = True
#
#     while q:
#         cur_v = q.popleft()
#         print(cur_v)
#         for next_v in graph[cur_v]:
#             if next_v not in visited:
#                 q.append(next_v)
#                 visited[next_v] = True
#
# bfs(graph, start_v)
#/////////////////////////////////////////
#DFS
#from collections import deque
#
# graph = {
#   0: [1, 3, 6],
#   1: [0, 3],
#   2: [3],
#   3: [0, 1, 2, 7],
#   4: [5],
#   5: [4, 6, 7],
#   6: [0, 5],
#   7: [3, 5]
# }
#
# visited = {}
#
# def dfs(cur_v):
#     visited[cur_v] = True
#     print(cur_v)
#     for next_v in graph[cur_v]:
#         if next_v not in visited:
#             dfs(next_v)
# dfs(0)
#
#//////////////
# depth = 0
# def dfs(cur_v):
#     global depth
#     visited[cur_v] = True
#     print('ㄴ' * depth, f"s{cur_v}")
#     depth += 1
#     for next_v in graph[cur_v]:
#         if next_v not in visited:
#             dfs(next_v)
#
# dfs(0)
#///////////////
# visited = [False] * len(graph)
# depth = 0
#
# def dfs(graph, cur_v):
#     global depth
#     visited[cur_v] = True
#     for next_v in graph[cur_v]:
#         if not visited[next_v]:
#             dfs(graph, next_v)
# dfs(graph, 3)
# print(visited)
#////////////////////////////////////
#DFS 직접 구현하기
# 1은 길이고, 0은 벽이다.
# 동서남북 4가지 방향으로 이동할 수 있다.
# 0,0 좌표에서 dfs()
# grid = [
#     [1, 1, 1, 1],
#     [0, 1, 0, 1],
#     [0, 1, 0, 1],
#     [1, 0, 1, 1]
# ]
#
#
# def dfs(r, c):
#     visited[r][c] = True
#     print(f"{r},{c}")
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < row_len and 0 <= nc< col_len and grid[nr][nc] == 1:
#             if not visited[nr][nc]:
#                 dfs(nr, nc)
#     return
#
# col_len = len(grid[0])
# row_len = len(grid)
# visited = [[False] * col_len for _ in range(row_len)]
# dr = [1, -1, 0 ,0]
# dc = [0, 0, 1, -1]
# dfs(0,0)
#////////////////////////////////////
#
# 1은 길이고, 0은 벽이다.
# 동서남북 4가지 방향으로 1칸 이동할 수 있다.
# 0,0 좌표에서 bfs()
#
# from collections import deque
#
# grid = [
#     [1, 1, 1, 1],
#     [0, 1, 0, 1],
#     [0, 1, 0, 1],
#     [1, 0, 1, 1]
# ]
#
# col_len = len(grid[0])
# row_len = len(grid)
# visited = [[False] * col_len for _ in range(row_len)]
#
# dr = [1,-1, 0, 0]
# dc = [0, 0, 1, -1]
#
# def bfs(sr, sc):
#     #초기 설정
#     q = deque()
#
#     #시작점 예약
#     q.append((sr, sc))
#     visited[sr][sc] = True
#
#     while q:
#         #방문
#         r,c = q.popleft()
#         print(r,c)
#         #예약
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1:
#                 if not visited[nr][nc]:
#                     q.append((nr,nc))
#                     visited[nr][nc] = True
#     return
#
# bfs(0,0)
#////////////////////////////////////////////////////////////
# #트리 인접 리시트
# tree = {
#     0: [1,2],
#     1: [],
#     2: [3,4],
#     3: [],
#     4: []
# }
#
# edges = [
#     [0,1],[0,2],[2,3],[2,4]
# ]
#
# for edge in edges:
#     u, v = edge
#     print(f"u:{u}, v:{v}")

#비어있는 트리 활용하기
#첫번 째 방법
# tree = {
#     0: [],
#     1: [],
#     2: [],
#     3: [],
#     4: []
# }
#
# for u,v in edges:
#     tree[u].append(v)
#     tree[v].append(u)
#
# print(tree)
#
# # 두 번째 방법
# tree = {}
# for u, v in edges:
#     print(tree)
#     if u not in tree:
#         tree[u] = []
#         print("비어있는 리스트 추가:", tree)
#     tree[u].append(v)
#     print("노드 추가:", tree)
#
# # 세 번째 방법
# tree = {}
# for u, v in edges:
#     if u not in tree:
#         tree[u] = []
#     tree[u].append(v)
# print(tree)
#
# # 네 번째 방법
# from collections import defaultdict
#
# tree =  defaultdict(list)
# for u, v in edges:
#     tree[u].append(v)
# print(tree)
#//////////////////////////////////////////////
# 트리 BFS
# tree = {
#     0: [1, 2],
#     1: [],
#     2: [3, 4],
#     3: [],
#     4: []
# }
#
# from collections import deque
#
# def bfs(root):
#     visited = []
#     q = deque()
#     q.append(root)
#     visited.append(root)
#
#     while q:
#         cur_v = q.popleft()
#         print(cur_v)
#
#         for next_v in tree[cur_v]:
#             q.appendleft(next_v)
#             visited.append(next_v)
#
#     return visited
#
# print(bfs(0))
#////////////////////////////////////////
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# root = TreeNode(0)
# root.left = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(4)
#
# def bfs(root):
#     visited = []
#     q = deque()
#     q.append(root)
#     visited.append(root.value)
#
#     while q:
#         cur_v = q.popleft()
#         print(cur_v.value)
#
#         if cur_v.left:
#             q.append(cur_v.left)
#             visited.append(cur_v.left.value)
#         if cur_v.right:
#             q.append(cur_v.right)
#             visited.append(cur_v.right.value)
#
#     return visited
#
# print(bfs(root))
#//////////////////////////////////
#트리 DFS
tree = {
    0: [1, 2],
    1: [],
    2: [3, 4],
    3: [],
    4: []
}
#
# def dfs(cur_v):
#     for child in tree[cur_v]:
#         dfs(child)
#     print(cur_v)
#     return
#
# dfs(0)

def dfs(cur_v, level):
    print(' '*level, 'ㄴ', cur_v)
    for child in tree[cur_v]:
        dfs(child, level+1)
    return
dfs(0,0)