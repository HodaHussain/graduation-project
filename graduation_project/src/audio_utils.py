import sounddevice as sd
import wave


def record_audio(duration: int = 10, filename: str = "mic_input.wav", samplerate: int = 16000) -> str:
    print("🎙️ Recording from microphone...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
    sd.wait()

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(samplerate)
        wf.writeframes(recording.tobytes())

    print(f"✅ Recording saved to: {filename}")
    return filename
