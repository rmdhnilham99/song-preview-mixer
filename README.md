# Song Preview Mixer
For cropping song preview and mix it in order with other songs in bundle


# Prerequisites
Python 3.14.3
ffmpeg

- before starting run this command

> pip install librosa pydub numpy

- put the desired audio (.mp3) into `input` folder
- name it 1, 2, 3, 4 ... .mp3
- other format like (.ogg) is possible with change on the code which currently using mp3
- run this command

> python app.py

- the result will be generated in `output` folder under the name final_output.mp3
- play with the config to results your best version of the mix


# Configuration
| Variable             | Value       | Description                                      |
|----------------------|-------------|--------------------------------------------------|
| INPUT_FOLDER         | "input"     | Folder with original MP3s                        |
| OUTPUT_FOLDER        | "output"    | Folder for final output                          |
| OUTPUT_FILE          | "final_output.mp3" | Final output file name                    |
| PRE_OFFSET           | 2           | Seconds before peak                              |
| MIN_CLIP             | 7           | Minimum clip length in seconds                   |
| MAX_CLIP             | 26          | Maximum clip length per clip                     |
| DROP_THRESHOLD       | 0.3         | Stop when intensity drops below this fraction    |
| FADE_IN_MS           | 200         | Fade-in per clip (milliseconds)                  |
| FADE_OUT_MS          | 300         | Fade-out per clip (milliseconds)                 |
| CROSSFADE_MS         | 500         | Crossfade between clips (milliseconds)           |
| FINAL_MAX_DURATION   | 26000       | Max final output length (milliseconds)           |