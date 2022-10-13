from wave_file_manager import *
import matplotlib.pyplot as plt

SILENCE_THRESHOLD = 50
GLITCH_MAX_LEN = int(441*0.6) # 6 ms


def normalize_samples(samples, max_value):
    # ...
    # détecter la valeur du min / max.
    # 10000 / -9500
    # 1000
    # x 1000 / 10000

    max_sample = max(abs(max(samples)), abs(min(samples)))
    f = max_value / max_sample

    return [s * f for s in samples]

def get_silences_points(samples, threshold, glitch_max_len):
    points = []
    in_silence_zone = False
    chunk_count = 0
    chunk_len = 441 # 10ms
    start = 0

    for i in range(len(samples)):
        s = abs(samples[i])
        if not in_silence_zone:
            if s <= threshold:
                if chunk_count == 0:
                    start = i
                chunk_count += 1
                if chunk_count >= chunk_len:
                    in_silence_zone = True
            else:
                chunk_count = 0
        else:
            if s > threshold:
                chunk_count = 0
                in_silence_zone = False
                if len(points) > 0 and start-points[-1][1] <= glitch_max_len:
                        points[-1] = (points[-1][0], i)
                else:
                    points.append((start, i))

    return points

# Lecture du fichier wav et récupération des samples
input_filename = "test_glitch.wav"
wav_samples = wave_file_read_samples(input_filename)
if wav_samples == None:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)

# normaliser les samples
wav_samples_norm = normalize_samples(wav_samples, 1000)

silences_points = get_silences_points(wav_samples_norm, SILENCE_THRESHOLD, GLITCH_MAX_LEN)

# matplotlib
'''a = [1, 10, 5, 2]
b = [0, 5, 3, 4]
plt.plot(a, label="Graphe A")
plt.plot(b, label="Graphe B")
plt.axhline(y = 4, color='r')
plt.axvline(x = 2, color='y')
plt.legend()
plt.show()  # bloquante'''

plt.plot(wav_samples_norm)
plt.axhline(y = SILENCE_THRESHOLD, color='r')
plt.axhline(y = -SILENCE_THRESHOLD, color='r')

for p in silences_points:
    plt.axvline(x = p[0], color='r')
    plt.axvline(x = p[1], color='y')

plt.show()

