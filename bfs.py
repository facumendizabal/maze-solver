#recives an start node, an end node and a graph adj list, applies breadth first search and returns
# a directed graph with the shortest path from s to e
def bfs(s, e, adj):
    solution_path = {}
    
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]

    while frontier:
        next_frontier = []

        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_frontier.append(v)

        frontier = next_frontier
        i += 1


    frontier = [e]

    while frontier:    
        for u in frontier:
            if u == s:
                break

            solution_path[u] = parent[u]
            frontier.append(parent[u])

        frontier = []

    return solution_path            
