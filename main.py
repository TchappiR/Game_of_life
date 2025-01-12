import numpy as np 

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):
    number_neighbors = np.sum(paded_frame[index_line-1:index_line+2, index_column-1:index_column+2])-paded_frame[index_line, index_column]
    
    return number_neighbors

def compute_next_frame(frame):
    
    paded_frame = np.pad(frame, 1, mode='constant')
    number_of_lines, number_of_columns = frame.shape
    
    for index_row in range(1, number_of_lines+1):
        for index_column in range(1, number_of_columns+1):
            if paded_frame[index_row, index_column] == 0 and compute_number_neighbors(paded_frame, index_row, index_column) == 3:
                frame[index_row-1, index_column-1] = 1
            elif paded_frame[index_row, index_column] == 1 and compute_number_neighbors(paded_frame, index_row, index_column) not in [2, 3]:
                frame[index_row-1, index_column-1] = 0
    
    return frame


counter = 0

while True:
    print(counter)
    print(frame)
    counter += 1
    compute_next_frame(frame)