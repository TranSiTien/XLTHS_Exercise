import numpy as np


def calculate_ste(frame):
    frame = np.array(frame, np.float64)
    ste = 0
    for i in range(len(frame)):
        ste += frame[i] ** 2
    return ste

