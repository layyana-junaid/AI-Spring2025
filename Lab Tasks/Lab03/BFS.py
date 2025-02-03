'''Layyana Junaid 23k-0056 BSAI-4A '''
'''Breadth First Search'''
'''Breath first search is basically our Goal Based Agent!'''

tree = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': ['H'],
  'E': [],
  'F': ['I'],
  'G': [],
  'H': [],
  'I': []
}

                                 #  A
                              #  /     \
                          #    B       C
                      #       / \     / \
                    #        D   E   F   G
                        #   /       /
                        #  H       I
def bfs(tree, start, goal):
  visited = []  # List for visited nodes
  queue = []  # Initialize a queue
  visited.append(start)
  queue.append(start)

  while queue:
    node = queue.pop(0)  # Dequeue
    print(node, end=" ")

    if node == goal:  # Stop if goal is found
      print("\nGoal found!")
      return  # End the function when goal is found

    for neighbour in tree[node]:  # Iterate over neighbors
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


start_node = 'A'
goal_node = 'I'
# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(tree, start_node, goal_node)
