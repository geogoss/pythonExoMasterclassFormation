import wave

# test1.wav
# https://docs.python.org/3/library/wave.html 

# byteLS -> [i] (Octet poids faible "Least significant")
# byteMS -> [i+1] (Octet poids fort "Most significant")
def get_16bits_sample_from_bytes(byteLS, byteMS):
    unsigned = byteLS + byteMS*256
    signed = unsigned
    if unsigned > 32767:
        signed = unsigned-65536
    return signed

def get_16bits_samples_from_bytes(bytes):
    samples = []
    for i in range(0,len(bytes)-1, 2):
        sample = get_16bits_sample_from_bytes(bytes[i], bytes[i+1])
        samples.append(sample)
    return samples


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

    # convertir les samples
    samples_16bits = get_16bits_samples_from_bytes(frames_as_bytes)

    wr.close()
    return samples_16bits
