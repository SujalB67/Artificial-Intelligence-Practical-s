import heapq

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # down, up, right, left
    
    def heuristic(a, b):
        # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {start: None}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, g_score[goal]

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            
            # Check bounds
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 'X':  # skip obstacles
                    continue
                
                # Ensure the cell is numeric (e.g. cost = 1)
                cost = grid[nx][ny] if isinstance(grid[nx][ny], (int, float)) else 1
                new_cost = g_score[current] + cost
                
                if (nx, ny) not in g_score or new_cost < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = new_cost
                    f_score = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f_score, (nx, ny)))
                    came_from[(nx, ny)] = current
                    
    return None, float('inf')
    
grid = [
    [1, 1, 1, 1],
    [1, 'X', 1, 1],
    [1, 1, 1, 1]
]

start = (0, 0)
goal = (2, 3)

path, cost = a_star_search(grid, start, goal)

print("Shortest Path:", path)
print("Total Cost:", cost)