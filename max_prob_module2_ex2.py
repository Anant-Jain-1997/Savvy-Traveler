from collections import defaultdict, deque
def solve(edges, probability, start, end):
    g = defaultdict(list)
    for i in range(len(edges)):
        src, dst = edges[i][0], edges[i][1]
        prob = probability[i]
        g[src].append((dst, prob))
        g[dst].append((src, prob))
    q = deque()
    q.append((start, 1))
    visited = defaultdict(int)
    while q:
        node, prob = q.popleft()
        if visited[node] > prob:
            continue
        else:
            visited[node] = prob

        for adj, nextProb in g[node]:
            if visited[adj] < prob * nextProb:
                q.append((adj, prob * nextProb))
    return visited[end]

# input 2
point_edges = [['A','B'],['B','C'],['C','F'],['F','E'],['E','B'],['E','D'],['D','A'],['D','G'],['G','H'],['H','E']]
probability = [0.8,0.6,0.8,0.9,0.7,0.8,0.9,0.8,0.9,0.6]
edges = [] #contains edges in terms of 0,1,2..
points = [] #contains unique Nodes in terms if its Name
nodes = [] #Contains unique Nodes in terms of 0,1,2..
count = 0 # to count unique Nodes

#looping in point_edges to get unique nodes

for i in point_edges:
    #looping in edge to get unique node
    for j in i:
        # steps performed if array is not empty
        # inserts node and its index in points and nodes respectivelyt if not already exists
        if len(points) > 0:
            flag = 0
            for k in points:
                if k == j:
                    flag = 1
            if flag == 0:
                points.append(j)
                nodes.append(count)
                count = count + 1
                # appends when array is empty (at index 0)

        else:
            points.append(j)
            nodes.append(count)
            count = count + 1


temp = []
# forms edges array in terms of 1,2,3,4..
for i in point_edges:
    for j in i:
        temp.append(points.index(j))
    edges.append(temp)
    temp = []
max = 0
maxIndex = 0
# loops into nodes and calls fuction for every node and finds max probability path.
for w in range(len(nodes)):
    result = 0
    for i in range(len(nodes)):
        if i != w:
            start = i
            end = w
            result = result + solve(edges, probability, start, end)
            if result > max:
                max = result
                maxIndex = w

print("Most reliable travel destination is ---> ",points[maxIndex])
