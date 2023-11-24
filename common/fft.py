import numpy as np
from matplotlib import pyplot as plt

from src.common.vowel_discrimination import get_stable_vowel


def pad_data(data, preferred_size):
    return_data = []
    pad_count = preferred_size - len(data)
    pad_left = pad_count // 2
    pad_right = pad_count - pad_left

    for i in range(pad_left):
        return_data.append(0)
    for i in range(len(data)):
        return_data.append(data[i])
    for i in range(pad_right):
        return_data.append(0)

    # plt.plot(return_data)
    return return_data


def trim_data(data, preferred_size):
    return_data = []
    pad_count = len(data) - preferred_size
    pad_left = pad_count // 2
    pad_right = pad_count - pad_left

    for i in range(pad_left, len(data) - pad_right):
        return_data.append(data[i])

    return return_data


def windowing(data, window):
    window_size = len(window)
    if len(data) < window_size:
        data = pad_data(data, window_size)
    elif len(data) > window_size:
        data = trim_data(data, window_size)

    return_data = []
    return data * window


def calculate_fft(data, n_fft):
    window = np.hamming(n_fft)
    windowed_data = windowing(data, window)
    return_data = np.fft.fft(windowed_data, n_fft)
    # print(return_data)

    return return_data


def calculate_fft_freqs(n_fft, samplerate):
    freqs = np.fft.fftfreq(n_fft, 1 / samplerate)
    positive_freqs = freqs[:len(freqs) // 2]
    return positive_freqs


def get_positive_fft_data(fft_data):
    fft_abs = np.abs(fft_data)
    positive_fft_data = fft_abs[:len(fft_abs) // 2]
    return positive_fft_data


def extract_magnitude_fft_data(data, n_fft, frame):
    vowel_data = get_stable_vowel(data, frame)
    positive_fft_data = get_positive_fft_data(calculate_fft(vowel_data, n_fft))
    return positive_fft_data

