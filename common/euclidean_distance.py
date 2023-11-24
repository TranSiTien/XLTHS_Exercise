import numpy as np


def euclidean_distance(fft_result1, fft_result2):
    # Ensure both FFT results are NumPy arrays
    fft_result1 = np.array(fft_result1)
    fft_result2 = np.array(fft_result2)

    # Calculate the Euclidean distance between the two FFT results
    distance = np.linalg.norm(fft_result1 - fft_result2)

    return distance


# def euclidean_distance(fft_result1, fft_result2):
#     # Check if the FFT results have the same length
#     if len(fft_result1) != len(fft_result2):
#         raise ValueError("FFT results must have the same length")
#
#     # Calculate the Euclidean distance
#     distance = 0.0
#     for i in range(len(fft_result1)):
#         distance += (fft_result1[i] - fft_result2[i]) ** 2
#
#     distance = distance ** 0.5  # Take the square root to get the Euclidean distance
#
#     return distance

