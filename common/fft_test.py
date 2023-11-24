import tkinter as tk
from tkinter import filedialog

import numpy as np
from scipy.io import wavfile

from src.common.fft import calculate_fft, pad_data, calculate_fft_freqs
from src.common.vowel_discrimination import extract_vowel, get_stable_vowel
from matplotlib import pyplot as plt

print("Please select a file to test vowel discrimination: ")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(f"Selected file: {file_path}")

samplerate, data = wavfile.read(file_path)

frame_duration = 0.03
frame_size = int(samplerate * frame_duration)

vowel_data = get_stable_vowel(data, frame_size)

fft_data = calculate_fft(vowel_data, 1024)

positive_freqs = calculate_fft_freqs(1024, samplerate)
fft_abs = np.abs(fft_data)
print(positive_freqs[0])
print(fft_data[0])
positive_fft_data = fft_abs[:len(fft_abs) // 2]

plt.plot(positive_freqs, positive_fft_data)
plt.show()


