# Song Preview Mixer

A simple tool to crop song previews and seamlessly mix them in sequence from a bundle of tracks.

---

## Prerequisites

Make sure you have the following installed:

* **Python 3.14.3**
* **ffmpeg**

Install required Python packages:

```bash
pip install librosa pydub numpy
```

---

## Usage

1. Place your audio files (`.mp3`) inside the `input` folder
2. Rename them in order:

   ```
   1.mp3, 2.mp3, 3.mp3, ...
   ```
3. (Optional) You can use other formats like `.ogg` by adjusting the code accordingly
4. Run the script:

```bash
python app.py
```

5. The final mixed output will be generated in the `output` folder:

   ```
   output/final_output.mp3
   ```

Tip: Experiment with the configuration values to get your perfect mix.

---

## Configuration

| Variable             | Value                | Description                                   |
| -------------------- | -------------------- | --------------------------------------------- |
| `INPUT_FOLDER`       | `"input"`            | Folder containing original audio files        |
| `OUTPUT_FOLDER`      | `"output"`           | Folder where output will be saved             |
| `OUTPUT_FILE`        | `"final_output.mp3"` | Name of the final output file                 |
| `PRE_OFFSET`         | `2`                  | Seconds before peak                           |
| `MIN_CLIP`           | `7`                  | Minimum clip length (seconds)                 |
| `MAX_CLIP`           | `26`                 | Maximum clip length per clip (seconds)        |
| `DROP_THRESHOLD`     | `0.3`                | Stop when intensity drops below this fraction |
| `FADE_IN_MS`         | `200`                | Fade-in duration per clip (ms)                |
| `FADE_OUT_MS`        | `300`                | Fade-out duration per clip (ms)               |
| `CROSSFADE_MS`       | `500`                | Crossfade duration between clips (ms)         |
| `FINAL_MAX_DURATION` | `26000`              | Maximum total output length (ms)              |

---

## 📝 Notes

* Ensure filenames are strictly ordered for correct sequencing
* Works on .mp3 and/or .ogg audio file
* Requires `ffmpeg` to be properly installed and accessible in your system path

---

## 🎧 Output

The final mixed preview will:

* Combine all clips in order
* Apply fades and crossfades
* Respect the maximum duration limit