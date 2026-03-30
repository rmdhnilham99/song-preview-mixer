import os
import librosa
import numpy as np
from pydub import AudioSegment

# === CONFIGURATION ===
INPUT_FOLDER = "input"            # Folder with original MP3s
OUTPUT_FOLDER = "output"          # Folder for final output
OUTPUT_FILE = "final_output.mp3"
PRE_OFFSET = 2                    # Seconds before peak
MIN_CLIP = 7                      # Minimum clip length in seconds
MAX_CLIP = 26                     # Maximum clip length per clip
DROP_THRESHOLD = 0.3              # Stop when intensity drops below this fraction
FADE_IN_MS = 200                   # Fade-in per clip (ms)
FADE_OUT_MS = 300                  # Fade-out per clip (ms)
CROSSFADE_MS = 500                 # Crossfade between clips (ms)
FINAL_MAX_DURATION = 26 * 1000     # Max final output length in milliseconds

# === GLOBAL COMBINED AUDIO ===
combined = AudioSegment.empty()

# === FUNCTIONS ===
def get_rms(y):
    return librosa.feature.rms(y=y)[0]

def find_peak_index(rms):
    return np.argmax(rms)

def find_dynamic_end(rms, peak_idx):
    peak_value = rms[peak_idx]
    for i in range(peak_idx, len(rms)):
        if rms[i] < peak_value * DROP_THRESHOLD:
            return i
    return len(rms) - 1

def process_file(filepath):
    global combined
    print(f"Processing: {filepath}")

    # Load audio with librosa for analysis
    y, sr = librosa.load(filepath, sr=None)
    rms = get_rms(y)
    peak_idx = find_peak_index(rms)
    end_idx = find_dynamic_end(rms, peak_idx)

    # Convert frame index to time in seconds
    total_duration = len(y) / sr
    frame_time = total_duration / len(rms)
    peak_time = peak_idx * frame_time
    end_time = end_idx * frame_time
    start_time = max(0, peak_time - PRE_OFFSET)

    # Enforce min/max clip durations
    duration = end_time - start_time
    if duration < MIN_CLIP:
        end_time = start_time + MIN_CLIP
    elif duration > MAX_CLIP:
        end_time = start_time + MAX_CLIP

    # Load audio with pydub for slicing
    audio = AudioSegment.from_mp3(filepath)
    clip = audio[int(start_time*1000):int(end_time*1000)]
    clip = clip.fade_in(FADE_IN_MS).fade_out(FADE_OUT_MS)

    # Combine with previous clips using crossfade
    if len(combined) == 0:
        combined = clip
    else:
        combined = combined.append(clip, crossfade=CROSSFADE_MS)

def batch_process():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith(".mp3"):
            process_file(os.path.join(INPUT_FOLDER, file))

    # If combined exceeds FINAL_MAX_DURATION, trim it
    if len(combined) > FINAL_MAX_DURATION:
        combined_trimmed = combined[:FINAL_MAX_DURATION].fade_out(1000)
    else:
        combined_trimmed = combined

    output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILE)
    combined_trimmed.export(output_path, format="mp3")
    print(f"\nFinal combined file saved as: {output_path}")
    print(f"Final duration: {len(combined_trimmed)/1000:.2f} seconds")

# === RUN ===
if __name__ == "__main__":
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    batch_process()