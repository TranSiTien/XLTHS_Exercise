import tkinter as tk
from tkinter import filedialog

from matplotlib import pyplot as plt
from scipy.io import wavfile

from src.common.directory import get_subdirectories
from src.common.euclidean_distance import euclidean_distance
from src.common.fft import extract_magnitude_fft_data, calculate_fft_freqs
from src.common.vector_avg import average_fft_results

root = tk.Tk()
root.withdraw()

# training_folder_path = filedialog.askdirectory()
# print(f"Selected training folder: {training_folder_path}")
training_folder_path = "D:\Chuong Trinh Hoc\Ki5\XLTHS\BaiTapNhom\signals\\NguyenAmHuanLuyen-16k";

# test_folder_path = filedialog.askdirectory()
# print(f"Selected testing folder: {test_folder_path}")
test_folder_path = "D:\Chuong Trinh Hoc\Ki5\XLTHS\BaiTapNhom\signals\\NguyenAmKiemThu-16k"

fft_sizes = [512, 1024, 2048]
frame_duration = 0.03

training_folder_sub_folders = get_subdirectories(training_folder_path)
test_folder_sub_folders = get_subdirectories(test_folder_path)
print(f"Training folders: {training_folder_sub_folders}")
print(f"Testing folders: {test_folder_sub_folders}")


def calculate_average_vowel_vectors(fft_size, fr_duration, folder_path, folders):
    vowel_names = ["a", "e", "i", "o", "u"]
    average_vowel_vectors = {}
    for vowel in vowel_names:
        fft_results = []
        for folder_name in folders:
            samplerate, data = wavfile.read(f"{folder_path}/{folder_name}/{vowel}.wav")
            magnitude_fft_data = extract_magnitude_fft_data(data, fft_size, (int)(fr_duration * samplerate))
            # plt.plot(frequency, magnitude_fft_data)
            # plt.title(f"{folder_name} - {vowel}")
            # plt.show()
            fft_results.append(magnitude_fft_data)
        average_vowel_vectors[vowel] = average_fft_results(fft_results)
        # plt.plot(average_vowel_vectors[vowel])
        # plt.title(f"{vowel}")
        # plt.show()

    return average_vowel_vectors


def analyze_statistic(n_fft, average_vowel_training_vectors, test_folder_sub_folders, test_folder_path):
    vowel_names = ["a", "e", "i", "o", "u"]
    statistics = {}
    for vowel in vowel_names:
        statistics[vowel] = {"correct": 0, "wrong_predicted": {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}}
    for vowel in vowel_names:
        for folder in test_folder_sub_folders:
            min_distance = 1e8
            predicted_vowel = ""
            for vowel_name2 in vowel_names:
                samplerate, data = wavfile.read(f"{test_folder_path}/{folder}/{vowel_name2}.wav")
                magnitude_fft_data = extract_magnitude_fft_data(data, n_fft, (int)(frame_duration * samplerate))
                distance = euclidean_distance(average_vowel_training_vectors[vowel],
                                              magnitude_fft_data)
                if distance < min_distance:
                    min_distance = distance
                    predicted_vowel = vowel_name2
            # print(f"vowel: {vowel},distance: {min_distance}, predicted vowel: {predicted_vowel}")
            if predicted_vowel == vowel:
                statistics[vowel]["correct"] += 1
            else:
                statistics[vowel]["wrong_predicted"][predicted_vowel] += 1


    return statistics


def print_statistic(st):
    vowel_names = ["a", "e", "i", "o", "u"]
    # for vowel in vowel_names:
        # print(f"Vowel: {vowel}")
        # print(f"Correct: {st[vowel]['correct']}")
        # print(f"Wrong predicted: {st[vowel]['wrong_predicted']}")
        # print(
        #     f"Accuracy: {st[vowel]['correct'] / (st[vowel]['correct'] + sum(st[vowel]['wrong_predicted'].values()))}")
#    print average accuracy
    total_correct = 0
    total_wrong = 0
    for vowel in vowel_names:
        total_correct += st[vowel]['correct']
        total_wrong += sum(st[vowel]['wrong_predicted'].values())
    print(f"Total correct: {total_correct}")
    print(f"Total wrong: {total_wrong}")
    print(f"Total accuracy: {total_correct / (total_correct + total_wrong)}")


for n_fft in fft_sizes:
    average_vowel_training_vectors = calculate_average_vowel_vectors(n_fft, frame_duration,training_folder_path, training_folder_sub_folders)
    statistics = analyze_statistic(n_fft, average_vowel_training_vectors, test_folder_sub_folders, test_folder_path)
    print(f"FFT size: {n_fft}")
    print_statistic(statistics)
