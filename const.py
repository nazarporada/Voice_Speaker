import pyaudio

WAVE_OUTPUT_FILENAME = "voice.wav"
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5