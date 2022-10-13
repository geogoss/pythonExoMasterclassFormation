from wave_file_manager import *
import matplotlib.pyplot as plt

wav_samples = wave_file_read_samples("test1.wav")
if wav_samples == None:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)


# matplotlib
'''a = [1, 10, 5, 2]
b = [0, 5, 3, 4]
plt.plot(a, label="Graphe A")
plt.plot(b, label="Graphe B")
plt.axhline(y = 4, color='r')
plt.axvline(x = 2, color='y')
plt.legend()
plt.show()  # bloquante'''

plt.plot(wav_samples)
plt.show()

