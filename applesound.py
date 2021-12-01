# Print out realtime audio volume as ascii bars

import sounddevice as sd
import numpy as np


import sys
import math
import numpy as np


class S:
    def __init__(self, record_time):
        self.totalSound = 0
        self.totalCount = 0
        self.record_time = record_time

    def print_sound(self, indata, outdata, frames, time, status):
        volume_norm = np.linalg.norm(indata)*5
        self.totalCount += 1
        self.totalSound += volume_norm
        print ("|" * int(volume_norm))



    def okay(self):
        with sd.Stream(callback=self.print_sound):
            sd.sleep(self.record_time*1000) # ms


b = S(5)
b.okay()
print(b.totalSound, b.totalCount)
noise = b.totalSound / b.totalCount
print("environment noise:", b.totalSound / b.totalCount)

#import pydub
#from pydub.playback import play

#print(sys.argv[1])

#song = AudioSegment.from_mp3("your_song.mp3")
#song =  pydub.AudioSegment.from_file(file = wavFile, format = "wav")


# boost volume by 6dB
#louder_song = song + 6

# reduce volume by 3dB
#quieter_song = song - 3

#Play song
#play(louder_song)

#save louder song
#louder_song.export("louder_song.mp3", format='mp3')



wavFile = sys.argv[1]

# import sounddevice as sd
import soundfile as sf
#
weight = noise / 10
data, fs = sf.read(wavFile)
sd.play(weight*data, fs)
sd.wait()

# (fs1, x) = read('Traffic_stereo.wav', 'rb')
# sd.play(x, fs1)
# sd.wait()