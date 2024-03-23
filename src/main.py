import whisper
import os

# convert file to wav
print("Converting file to .wav")
command = "ffmpeg -i in/interview2.m4a tmp/output.wav"
return_code = os.system("/bin/bash -c \"" + command + "\"")
if return_code != 0:
  print("Something went wrong, ffmpeg command failed")
  exit(1)
print()

# transcribe
print("Start transcribing")
model = whisper.load_model("base")
result = model.transcribe("tmp/output.wav", verbose = True)
#print(result["text"])
print()

# export
with open("out/interview2-transcription.txt", "w") as f:
  f.write(result["text"])

print("Results exported")