def is_valid(state):
    missioanries_left,cannibals_left,boat = state
    missioanries_right = 3 - missioanries_left
    cannibals_right = 3 - cannibals_left

    if (missioanries_left < cannibals_left and missioanries_left > 0) or(missioanries_right< cannibals_right and missioanries_right > 0):
        return False
    return True 

def get_successor(state):
    missioanries_left,cannibals_left,boat = state
    moves = []
    possible_moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    if boat == 1:
        for move in possible_moves:
            missioanries_new = missioanries_left - move[0]
            cannibals_new = cannibals_left - move[1]
            if 0 <= missioanries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missioanries_new,cannibals_new,0)):
                moves.append((missioanries_new,cannibals_new,0))
    else:
        for move in possible_moves:
            missioanries_new = missioanries_left - move[0]
            cannibals_new = cannibals_left - move[1]
            if 0 <= missioanries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missioanries_new,cannibals_new,0)):
                moves.append((missioanries_new,cannibals_new,1))
    return moves

def dfs(current_state,visited,goal_state,path):

    if current_state == goal_state:
        return path
    
    visited.add(current_state)
   
    for successor in get_successor(current_state):
        if successor not in visited:
            new_path = dfs(successor,visited,goal_state,path + [successor])
            if new_path:
                return new_path
    return None
def is_valid(state):
    missioanries_left,cannibals_left,boat = state
    missioanries_right = 3 - missioanries_left
    cannibals_right = 3 - cannibals_left

    if (missioanries_left < cannibals_left and missioanries_left > 0) or(missioanries_right< cannibals_right and missioanries_right > 0):
        return False
    return True 

def get_successor(state):
    missioanries_left,cannibals_left,boat = state
    moves = []
    possible_moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    if boat == 1:
        for move in possible_moves:
            missioanries_new = missioanries_left - move[0]
            cannibals_new = cannibals_left - move[1]
            if 0 <= missioanries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missioanries_new,cannibals_new,0)):
                moves.append((missioanries_new,cannibals_new,0))
    else:
        for move in possible_moves:
            missioanries_new = missioanries_left - move[0]
            cannibals_new = cannibals_left - move[1]
            if 0 <= missioanries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missioanries_new,cannibals_new,0)):
                moves.append((missioanries_new,cannibals_new,1))
    return moves

def dfs(current_state,visited,goal_state,path):

    if current_state == goal_state:
        return path
    
    visited.add(current_state)
   
    for successor in get_successor(current_state):
        if successor not in visited:
            new_path = dfs(successor,visited,goal_state,path + [successor])
            if new_path:
                return new_path
    return None

initial_state = (3,3,1)
goal_state = (0,0,0)
visited = set()
solution  = dfs(initial_state,visited,goal_state,[])

if solution:
    print("Solutionm found")
    for i,state in enumerate(solution):
        print(f"State {i+1}:{state}")
else:
    print(" Solution not found")
initial_state = (3,3,1)
goal_state = (0,0,0)
visited = set()
solution  = dfs(initial_state,visited,goal_state,[])

if solution:
    print("Solutionm found")
    for i,state in enumerate(solution):
        print(f"State {i+1}:{state}")
else:
    print(" Solution not found")
