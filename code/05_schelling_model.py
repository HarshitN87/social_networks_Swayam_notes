import random
import matplotlib.pyplot as plt
import copy

class Schelling:
    def __init__(self, size, empty_ratio, similarity_threshold, n_iterations):
        self.size = size 
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_iterations = n_iterations
        self.grid = []
        self.empty_cells = []
        
        # Populate grid
        # 1 = Type A, 2 = Type B, 0 = Empty
        p = [(1 - empty_ratio)/2, (1 - empty_ratio)/2, empty_ratio]
        choices = [1, 2, 0]
        
        for i in range(size):
            row = []
            for j in range(size):
                val = random.choices(choices, weights=p)[0]
                row.append(val)
                if val == 0:
                    self.empty_cells.append((i, j))
            self.grid.append(row)

    def is_unsatisfied(self, x, y):
        agent_type = self.grid[x][y]
        if agent_type == 0:
            return False

        same_type_count = 0
        total_neighbors = 0
        
        # 8 possible directions
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),           (0,1),
                      (1,-1),  (1,0),  (1,1)]
                      
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                neighbor = self.grid[nx][ny]
                if neighbor != 0:
                    total_neighbors += 1
                    if neighbor == agent_type:
                        same_type_count += 1
                        
        if total_neighbors == 0: 
            return False # Isolated node
            
        # Is the threshold met? (Using absolute count as requested in the case study)
        # Often it's a percentage, but Case Study 1 explicitly uses an absolute t=3 or t=4
        if same_type_count < self.similarity_threshold:
            return True
            
        return False

    def play(self):
        for i in range(self.n_iterations):
            unsatisfied_agents = []
            for r in range(self.size):
                for c in range(self.size):
                    if self.is_unsatisfied(r, c):
                        unsatisfied_agents.append((r, c))
                        
            if len(unsatisfied_agents) == 0:
                print(f"100% Satisfaction reached at iteration {i}.")
                break
                
            # Move unsatisfied agents
            for agent in unsatisfied_agents:
                # Agent might have moved if we process immediately, but typically 
                # we pick one unsatisfied agent randomly per turn (as per case study)
                pass
                
            # Randomly select ONE agent and move it to ONE random empty cell 
            # (Following the strictly sequential prompt from Case Study 1)
            mover = random.choice(unsatisfied_agents)
            new_home = random.choice(self.empty_cells)
            
            # Swap
            this_type = self.grid[mover[0]][mover[1]]
            self.grid[mover[0]][mover[1]] = 0
            self.grid[new_home[0]][new_home[1]] = this_type
            
            # Update empty cells tracker
            self.empty_cells.remove(new_home)
            self.empty_cells.append(mover)

    def draw(self, title):
        plt.figure(figsize=(6,6))
        # Map colors
        color_grid = []
        for r in range(self.size):
            row = []
            for c in range(self.size):
                if self.grid[r][c] == 1:
                    row.append([1.0, 0.0, 0.0]) # Red for Type A
                elif self.grid[r][c] == 2:
                    row.append([0.0, 0.0, 1.0]) # Blue for Type B
                else:
                    row.append([1.0, 1.0, 1.0]) # White for Empty
            color_grid.append(row)
            
        plt.imshow(color_grid)
        plt.title(title)
        plt.grid(False)
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    # Case study example: 10x10 grid, threshold t=3
    print("Initializing Schelling Model with threshold t=3...")
    model = Schelling(size=10, empty_ratio=0.1, similarity_threshold=3, n_iterations=5000)
    
    # Optional: draw initial state
    # model.draw("Initial Random State")
    
    model.play()
    print("Simulation finished. Visualizing Final State...")
    # Optional: draw final state
    # model.draw("Final Cluster State")
