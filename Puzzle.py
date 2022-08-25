import queue


def solve_puzzle(board, source, destination):
    """
    Uses BFS to find and return the shortest path in a puzzle. Uses two separate queues to track the row and column of
    neighboring cells to current position in the maze
    """
    rows = len(board)
    columns = len(board[0])
    starting_row, starting_column = source[0], source[1]
    visited = [[False for _ in range(columns)] for _ in range(rows)]
    row_dir = [-1, 1, 0, 0]
    col_dir = [0, 0, 1, -1]
    row_q = queue.Queue()
    col_q = queue.Queue()
    row_q.put(starting_row)
    col_q.put(starting_column)
    visited[starting_row][starting_column] = source

    def check_neighbors(r, c):
        """
        check neighboring cells from current position for available spaces to move to
        """
        for i in range(4):
            row_neighbor = r + row_dir[i]
            col_neighbor = c + col_dir[i]
            if row_neighbor < 0 or col_neighbor < 0:            # out of bounds
                continue
            if row_neighbor >= rows or col_neighbor >= columns: # out of bounds
                continue
            if visited[row_neighbor][col_neighbor]:         # already checked cell
                continue
            if board[row_neighbor][col_neighbor] == '#':    # blocked
                continue
            row_q.put(row_neighbor)
            col_q.put(col_neighbor)
            visited[row_neighbor][col_neighbor] = (r, c)

    def get_path(board, f_row, f_col):
        """
        Uses backtracking following along the Visited Matrix to return a list of tuples
        for the path taken from the source position to the destination position
        """
        curr_pos = (f_row, f_col)
        next_pos = (f_row, f_col)
        path = []
        while curr_pos != source:
            curr_pos = next_pos
            next_pos = board[curr_pos[0]][curr_pos[1]]
            path.append(curr_pos)
        path.reverse()
        return path

    while col_q.qsize() > 0:    # empty queue means no more paths to check
        row = row_q.get()
        column = col_q.get()
        if row == destination[0] and column == destination[1]:
            path = get_path(visited, row, column)
            if len(path) == 0 or path is None:
                return None
            return path
        check_neighbors(row, column)
