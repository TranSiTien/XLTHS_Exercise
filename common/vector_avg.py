import numpy as np


def get_vectors_avg(vectors, vector_length):
    return_vector = []
    num_vectors = len(vectors) / vector_length
    for i in range(vector_length):
        sum = 0
        for j in range(num_vectors):
            sum += vectors[j * vector_length + i]
        return_vector.append(sum / num_vectors)

    return return_vector


def average_fft_results(fft_results):
    # Stack the FFT results along a new axis to calculate the mean across that axis
    stacked_results = np.stack(fft_results, axis=0)

    # Calculate the mean along the specified axis (axis=0 for averaging across multiple arrays)
    average_result = np.mean(stacked_results, axis=0)

    return average_result
