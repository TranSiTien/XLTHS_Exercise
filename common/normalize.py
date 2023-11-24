import numpy as np


def normalize_vector(vector):
    return_vector = np.array(vector, np.float64)
    max_volume = max(abs(return_vector))
    for i in range(len(return_vector)):
        return_vector[i] = return_vector[i] / max_volume
    return return_vector
