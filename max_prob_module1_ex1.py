from collections import defaultdict, deque
print("CPSC 535 Advanced Algorithms Project")
print("We are assuming the vertices as A --> 0, B --> 1, C --> 2, D --> 3, ..... , Z --> 25")
def solve(edges, probability, start, end):
    g = defaultdict(list)
    #make graph
    for i in range(len(edges)):
        src, dst = edges[i][0], edges[i][1]
        prob = probability[i]
        g[src].append((dst, prob))
        g[dst].append((src, prob))
    q = deque()
    #do BFS with save parents
    q.append((start, 1))
    maxProb = defaultdict(float)
    parent = defaultdict(int)
    parent[start] = start
    while q:
        node, prob = q.popleft()
        if maxProb[node] > prob:
            continue
        else :
            maxProb[node] = prob
        for adj, nextProb in g[node]:
            if maxProb[adj] < (prob * nextProb):
                parent[adj] = node;
                q.append((adj, (prob * nextProb)))

    maxAnsProb = maxProb[end]
    #print Path
    path = []
    while(end!=parent[end]):
        path.append(end)
        end = parent[end];
    path.append(end)
    path.reverse()
    
    print("This route will maximize the probability to arrive on time ---> ",*path)
    
    return maxAnsProb

edges =[[0, 1], [0, 2], [0, 3], [1, 2], [1, 4], [1, 5], [2, 5], [3, 5], [3, 6], [4, 5], [4, 7], [5, 6], [5, 7], [6, 7]]
probability =  [0.8, 0.7, 0.9, 0.8, 0.6, 0.6, 0.9, 0.6, 0.8, 0.8, 0.6, 0.7, 0.7, 0.9]
start = 5
end = 0
print("The probability of the taken path is ---> ",solve(edges, probability, start, end))
