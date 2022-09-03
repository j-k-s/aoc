from collections import deque

## read file
with open('input') as f:
    lines = f.readlines()

upper = set()
lower = set()
nodes = set()

## import edges + create upper and lower sets.
def import_edges():
    edges = []
    for l in lines:
        edge = (l.split("-")[0],l.split("-")[1].strip())
        edges.append(edge)
        for e in edge:
            nodes.add(e)
            if e != "start" and e != "end":
                if e.isupper() is True: upper.add(e)
                if e.islower() is True:
                    lower.add(e)
    print("edges:")
    for e in edges: print(e)
    print(f"Upper set contains: {upper}")
    print(f"Lower set contains: {lower}")
    return edges

## function to take a node and find adjacent nodes
def find_adjacent(node):
    results = []
    for e in edges:
        if e[0] == node: results.append(e[1])
        if e[1] == node: results.append(e[0])
    return results

def build_dict_of_adjacents(nodes):
    graph = {}
    for n in nodes: graph[n] = find_adjacent(n)
    return graph

def find_paths():
    my_queue = deque()
    results = []
    start = ["start"] ## starting path is the first node
    my_queue.append(start)
    while len(my_queue) > 0:
        thispath = my_queue.popleft()   ## path to analyse
        currentnode = thispath[-1]      ## end node of this path
        nused = set()
        small_cave_visited = {}
        for low in lower: small_cave_visited[low] = 0        ## initialise counter for small cave
        small_cave_twice = False                            ## Flag is true if any small cave = twice
        for p in thispath:
            nused.add(p)  ## set of used nodes
            if p in lower: small_cave_visited[p] += 1
            if p in lower and small_cave_visited[p] == 2: small_cave_twice = True
        if currentnode == "end":
            results.append(thispath)
        else:
            for c in graph[currentnode]:   ## for all adjacents to last node in this path
                nextpath = []
                ## Warning to the reader - not very readable condition statement
                if ((c != "start" and (c in upper or (c in lower and ((small_cave_visited[c] < 2 and small_cave_twice == False) or (small_cave_visited[c] < 1 and small_cave_twice == True)))))
                    or c == "end"):
                    for p in thispath: nextpath.append(p) ## create new working path
                    nextpath.append(c)
                    my_queue.append(nextpath)
                    if c in lower:
                        small_cave_visited[c] += 1
                        if small_cave_visited[c] == 2: small_cave_twice == True


    for r in results: print(*r)
    print(f"Total paths = {len(results)}")

## main program
a = "start"
b = "end"
edges = import_edges()
graph = build_dict_of_adjacents(nodes)

print("===============\nnodes:",nodes)
print("===============\nedges:",edges)
print("===============\ngraph:",graph)

paths = find_paths()
