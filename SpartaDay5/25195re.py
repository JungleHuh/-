import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, w = map(int,input().split())
  graph[u].append(w)

fan_count = int(input())
fan_N = list(map(int,input().split()))
exist = 0
answer = []
def DFS(graph, v, exist):
  #노드 끝까지 도달했을 때 팬클럽 곰곰이를 만나지 않았다면 answer리스트에 0추가
  if not graph[v] and exist == 0:
    answer.append(0)
  
  for i in graph[v]:
    exist = 0
    #지나가는 경로 팬클럽 존재 -> exist를 -1로 바꿔주고 다음 경로탐색
    if i in fan_N:
      exist = -1
      continue
    #경로탐색
    DFS(graph, i, exist)


if 1 in fan_N:
  print("Yes")
else:
  DFS(graph, 1, exist)
  if len(answer) == 0:
    print("Yes")
  else:
    print("yes")