N = int(input())

first = [i for i in range(N + 1)]
second = [0]
[second.append(int(input())) for _ in range(N)]

visited = [False] * (N + 1)
same_arr = [first[j] for j in range(1, N + 1) if first[j] == second[j]]

all_result = []


def dfs(first, second, v, visited, result):
    visited[v] = True

    # second -> first -> first's second
    temp = second[v]
    if visited[temp]:
        global all_result
        if len(result) >= len(all_result):
            all_result = result

        return

    result.append(temp)
    dfs(first, second, temp, visited, result)
    visited[v] = False


for i in range(1, N + 1):
    dfs(first, second, i, visited, [i])
all_result.extend(same_arr)

final_result = list(set(all_result))
final_result.sort()

print(len(final_result))
[print(r) for r in final_result]
