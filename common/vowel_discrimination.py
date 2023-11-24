from src.common.normalize import normalize_vector
from src.common.ste_calculator import calculate_ste


def get_ste_data(data, frame_size):
    frame_data = []
    ste_data = []
    for i in range(len(data)):
        frame_data.append(data[i])
        if len(frame_data) == frame_size:
            ste_data.append(calculate_ste(frame_data))
            frame_data = []

    return ste_data


def extract_vowel(data, frame_size):
    threshold = 0.2

    ste_data = get_ste_data(data, frame_size)
    normalized_ste_data = normalize_vector(ste_data)
    left = 0
    right = len(normalized_ste_data) - 1
    while (normalized_ste_data[left] < threshold) and (left < len(normalized_ste_data)):
        left += 1
    while normalized_ste_data[right] < threshold and right >= 0:
        right -= 1

    if left >= right:
        raise Exception("No vowel found")

    start_vowel = left * frame_size
    end_vowel = right * (frame_size + 1)
    vowel_data = data[start_vowel:end_vowel]

    return vowel_data


def get_stable_vowel(data, frame_size):
    vowel_data = extract_vowel(data, frame_size)
    data_length = len(vowel_data)
    return vowel_data[data_length // 3:data_length * 2 // 3]

