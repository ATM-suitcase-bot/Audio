from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'E:\aseniorSemester2\RoboticsCapstone\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15')
# read the model

recognizer = KaldiRecognizer(model, 16000)

# Recognize from the microphone
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()

while True:
    data = stream.read(4096) # 4 bytes
    # if len(data) == 0:
    #     break

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())
