from wave_file_manager import *
import matplotlib.pyplot as plt


def normalize_samples(samples, max_value):
    # ...
    # détecter la valeur du min / max.
    # 10000 / -9500
    # 1000
    # x 1000 / 10000

    max_sample = max(abs(max(samples)), abs(min(samples)))
    f = max_value / max_sample

    return [s * f for s in samples]

# Lecture du fichier wav et récupération des samples
wav_samples = wave_file_read_samples("test1.wav")
if wav_samples == None:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)

# normaliser les samples
wav_samples_norm = normalize_samples(wav_samples, 1000)

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
plt.show()

