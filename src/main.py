import whisper
import os

# vars
INTERVIEW_FILE_NAME = "interview2"
INTERVIEW_FILE_EXT = ".m4a"

# convert file to wav
print("##### Converting file to .wav #####")
command = f"ffmpeg -y -i in/{INTERVIEW_FILE_NAME + INTERVIEW_FILE_EXT} tmp/output.wav"
return_code = os.system("/bin/bash -c \"" + command + "\"")
if return_code != 0:
  print("Something went wrong, ffmpeg command failed")
  exit(1)
print()

# transcribe
print("##### Start transcribing #####")
model = whisper.load_model("base")
result = model.transcribe("tmp/output.wav", verbose = False)
#print(result["text"])
print()

# export
with open(f"out/{INTERVIEW_FILE_NAME}_transcription.txt", "w") as f:
  f.write(result["text"])

print("##### Results exported #####")
