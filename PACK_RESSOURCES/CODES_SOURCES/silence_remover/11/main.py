from wave_file_manager import wave_file_read_samples, wave_file_write_samples
from exclude_silence_processing import get_samples_without_silences


# 1 - Lecture du fichier wav et récupération des samples
#input_filename = "test1.wav"
#input_filename = "test_glitch.wav"
#input_filename = "test_phrase_informatique.wav"
input_filename = "test_anglais.wav"
wav_samples = wave_file_read_samples(input_filename)
if wav_samples == None:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)

# 2 - Processing : algorithme pour supprimer les silences
wav_samples_without_silences = get_samples_without_silences(wav_samples)

# 3 - Ecriture du fichier wav de sortie
output_filename = input_filename[:-4] + "_OUT" + input_filename[-4:]
print("OUTPUT FILENAME", output_filename)
wave_file_write_samples(output_filename, wav_samples_without_silences)

