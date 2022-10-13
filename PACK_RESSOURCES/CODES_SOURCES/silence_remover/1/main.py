from wave_file_manager import *

wav_samples = wave_file_read_samples("test1.wav")
if wav_samples == None:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)






