import whisper
import numpy as np
import wave


print("🔄 Loading Whisper model...")
model = whisper.load_model("small")  # you can switch to "base" if you want faster
print("✅ Whisper model loaded.")


def _load_wav_mono_16k(path: str, target_sr: int = 16000) -> np.ndarray:
    # Read wav via Python (no ffmpeg)
    with wave.open(path, "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        audio_bytes = wf.readframes(n_frames)

    if sampwidth != 2:
        raise ValueError(f"Expected 16-bit WAV (sampwidth=2), got sampwidth={sampwidth}")

    audio = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0

    # stereo -> mono
    if n_channels == 2:
        audio = audio.reshape(-1, 2).mean(axis=1)

    # resample if needed (your recorder is already 16k)
    if framerate != target_sr:
        x_old = np.linspace(0, 1, num=len(audio), endpoint=False)
        new_len = int(len(audio) * target_sr / framerate)
        x_new = np.linspace(0, 1, num=new_len, endpoint=False)
        audio = np.interp(x_new, x_old, audio).astype(np.float32)

    return audio


def transcribe_audio(file_path: str, language: str) -> str:
    audio = _load_wav_mono_16k(file_path)

    result = model.transcribe(
        audio,
        language=language,
        task="transcribe",
        temperature=0.0,
        condition_on_previous_text=False,
    )
    return result.get("text", "").strip()
