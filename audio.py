import pyaudio
import struct



pa = pyaudio.PyAudio()
SAMPLING_RATE = int(pa.get_device_info_by_index(0)['defaultSampleRate'])
NUM_SAMPLES = 1000
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)

string_audio_data = stream.read(NUM_SAMPLES)
k = max(struct.unpack('1000h', string_audio_data))
print(k)
                
