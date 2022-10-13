from wave_file_manager import *
import matplotlib.pyplot as plt

SILENCE_THRESHOLD = 50
GLITCH_MAX_LEN = int(441*0.6) # 6 ms
SILENCE_MIN_LEN = 4410 * 4 # 400ms
MARGIN_START = 4410 * 1 # 100ms
MARGIN_END = 4410 * 1 # 100ms

def normalize_samples(samples, max_value):
    # ...
    # détecter la valeur du min / max.
    # 10000 / -9500
    # 1000
    # x 1000 / 10000

    max_sample = max(abs(max(samples)), abs(min(samples)))
    f = max_value / max_sample

    return [s * f for s in samples]

def get_silences_points(samples, threshold, glitch_max_len, silence_min_len, margin_start, margin_end):
    points = []
    in_silence_zone = False
    chunk_count = 0
    chunk_len = 441 # 10ms
    start = 0

    if (MARGIN_START+MARGIN_END) > SILENCE_MIN_LEN:
        print("ERREUR: MARGIN_START + MARGIN_END supérieur à SILENCE_MIN_LEN")
        return None

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

    points = [(p[0]+margin_start, p[1]-margin_end) for p in points if p[1]-p[0] >= silence_min_len]

    return points

def get_samples_without_silences(samples, silences_points):
    out_samples = []

    # 0.....50----80.....100----120.....200
    # points = [(50, 80), (100, 120)]
    # out_samples = samples[0:50]+samples[80:100]+samples[120:200]
    # - le silence démarre dès le début (0)
    # - à la fin : ne pas oublier le son du dernièr bloc

    start = 0
    for p in silences_points:
        if p[0] > start:
            out_samples += samples[start:p[0]]
            start = p[1]

    if start < len(samples)-1:
        out_samples += samples[start:]

    return out_samples

# Lecture du fichier wav et récupération des samples
#input_filename = "test1.wav"
#input_filename = "test_glitch.wav"
#input_filename = "test_phrase_informatique.wav"
input_filename = "test_anglais.wav"
wav_samples = wave_file_read_samples(input_filename)
if wav_samples == None:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)

# normaliser les samples
wav_samples_norm = normalize_samples(wav_samples, 1000)

silences_points = get_silences_points(wav_samples_norm, SILENCE_THRESHOLD, GLITCH_MAX_LEN, SILENCE_MIN_LEN, MARGIN_START, MARGIN_END)

wav_samples_without_silences = get_samples_without_silences(wav_samples, silences_points)


# matplotlib
'''a = [1, 10, 5, 2]
b = [0, 5, 3, 4]
plt.plot(a, label="Graphe A")
plt.plot(b, label="Graphe B")
plt.axhline(y = 4, color='r')
plt.axvline(x = 2, color='y')
plt.legend()
plt.show()  # bloquante'''

'''plt.plot(wav_samples_norm)
plt.axhline(y = SILENCE_THRESHOLD, color='r')
plt.axhline(y = -SILENCE_THRESHOLD, color='r')

for p in silences_points:
    plt.axvline(x = p[0], color='r')
    plt.axvline(x = p[1], color='y')

plt.show()'''

# input_filename
# "test1.wav" -> "test1_OUT.wav"
output_filename = input_filename[:-4] + "_OUT" + input_filename[-4:]
print("OUTPUT FILENAME", output_filename)
wave_file_write_samples(output_filename, wav_samples_without_silences)

