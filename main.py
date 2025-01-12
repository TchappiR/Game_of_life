import numpy as np 

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):
    number_neighbors = np.sum(paded_frame[index_line-1:index_line+2, index_column-1:index_column+2])-\
							paded_frame[index_line, index_column]
    
    return number_neighbors

def compute_next_frame(frame):
    
    paded_frame = np.pad(frame, 1, mode='constant')
    
    return frame

while True:
    
    print(frame)
    frame = compute_next_frame(frame)