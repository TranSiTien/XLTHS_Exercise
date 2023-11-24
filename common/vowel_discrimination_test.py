import tkinter as tk
from tkinter import filedialog
from scipy.io import wavfile

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

plt.plot(vowel_data)
plt.show()

