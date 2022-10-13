import wave

# test1.wav
# https://docs.python.org/3/library/wave.html 

def wave_file_read_samples(filename):
    expected_n_channels = 1 # mono
    expected_sample_width = 2 # 16bits
    expected_framerate = 44100

    wr = wave.open(filename, mode="rb")
    if wr.getnchannels() != expected_n_channels:
        print("ERREUR: Utilisez un fichier mono")
        return None
    if wr.getsampwidth() != expected_sample_width:
        print("ERREUR: Utilisez le format 16bits")
        return None       
    if wr.getframerate() != expected_framerate:
        print("ERREUR: Utilisez 44100Hz")
        return None           

    nframes = wr.getnframes()
    print("nframes", nframes)
    frames_as_bytes = wr.readframes(nframes)

    # TO DO : convertir les samples

    wr.close()
    return frames_as_bytes
