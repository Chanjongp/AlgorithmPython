from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)

    for from_country, to_country in tickets:
        graph[from_country].append(to_country)

    for country in graph.keys():
        graph[country].sort(reverse=True)

    stack = []
    stack.append("ICN")

    while stack:
        top = stack.pop()

        if top not in graph or not graph[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    return answer[::-1]
