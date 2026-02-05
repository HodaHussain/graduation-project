
# import re
# from typing import Tuple
# import whisper
# import os
# import tempfile
# import sounddevice as sd
# import wave
# from nltk.tokenize import word_tokenize
# from autocorrect import Speller
# from spellchecker import SpellChecker
# from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
# import nltk
# # ✅ Define Expanded Command Lists
# actions_list_en = [
#     "turn on", "turn off", "switch on", "switch off", "activate", "deactivate",
#     "open", "close", "lock", "unlock", "increase", "decrease", "raise", "lower",
#     "set", "adjust", "change", "dim", "brighten", "make brighter", "make dimmer",
#     "change color to", "set brightness to", "set fan speed to", "start", "stop",
#     "pause", "resume", "schedule", "set timer for", "turn on at", "turn off at",
#     "enable", "disable", "sync", "connect", "show status", "check status",
#     "is it on", "is it off", "good morning", "good night", "movie mode", "night mode"
# ]

# devices_list_en = [
#     "lights", "light", "leds", "lamp", "bulb", "ceiling light", "strip lights",
#     "fan", "ceiling fan", "exhaust fan", "desk fan", "door", "front door",
#     "main door", "back door", "garage door", "camera", "security camera", "cctv",
#     "surveillance", "curtains", "blinds", "shades", "window covers"
# ]

# rooms_list_en = [
#     "living room", "hall", "lounge", "main room", "reception", "bedroom",
#     "master bedroom", "guest room", "my room", "kitchen", "cooking area",
#     "dining area", "bathroom", "restroom", "toilet", "washroom", "balcony",
#     "terrace", "patio", "porch", "garage", "carport"
# ]

# actions_list_ar = [
#     "شغل", "أشغل", "افتح", "أفتح", "شغّل", "قم بتشغيل", "قم بإضاءة", "أطفئ",
#     "اغلق", "إيقاف", "أوقف", "أغلق", "إطفاء", "وقف التشغيل", "ارفع", "خفض",
#     "زود", "قلل", "زيد", "نقص", "غير", "اضبط", "عدل", "بدل", "قم بضبط",
#     "قم بتعديل", "خفف", "سطع", "اجعل الإضاءة أقوى", "اجعل الإضاءة أضعف",
#     "غير اللون إلى", "اضبط السطوع إلى", "اجعل السطوع", "اضبط سرعة المروحة إلى",
#     "ابدأ", "أوقف", "استأنف", "استمرار", "وقف مؤقت", "اضبط مؤقت", "حدد وقت التشغيل",
#     "شغل عند", "أطفئ عند", "قم بتمكين", "عطل", "اربط", "وصل", "اعرض الحالة",
#     "تحقق من الحالة", "هل هو يعمل", "هل هو مغلق", "وضع النوم", "وضع السينما",
#     "صباح الخير", "تصبح على خير"
# ]

# devices_list_ar = [
#     "الأضواء", "الضوء", "المصابيح", "المصباح", "اللمبات", "اللمبة", "الليدات", "نور",
#     "النور", "الإضاءة", "اللمبة الذكية", "مصباح السقف", "إضاءة الشريط", "المروحة",
#     "المراوح", "مروحة السقف", "المروحة الذكية", "شفاط الهواء", "مروحة الطاولة", "الباب",
#     "الأبواب", "الباب الرئيسي", "باب المدخل", "الباب الأمامي", "الباب الخلفي", "باب الجراج",
#     "الكاميرا", "الكاميرات", "كاميرا المراقبة", "كاميرا الأمن", "كاميرا CCTV", "المراقبة",
#     "الستائر", "الستارة", "البرادي", "الشيش", "الستائر الذكية", "الغالق", "مظلة النافذة"
# ]

# locations_list_ar = [
#     "غرفة المعيشة", "الصالة", "الصالون", "الريسيبشن", "الريسبشن", "الغرفة الرئيسية",
#     "غرفة النوم", "غرفة النوم الرئيسية", "غرفة الضيوف", "غرفتي", "حجرتي", "المطبخ",
#     "المطبخ الرئيسي", "منطقة الطهي", "مكان الأكل", "غرفة الطعام", "الحمام", "دورة المياه",
#     "التواليت", "المرحاض", "الحمام الرئيسي", "الشرفة", "البلكونة", "التراس", "الفناء",
#     "الباحة", "المساحة الخارجية", "الكراج", "الجراج", "مكان السيارة", "الموقف"
# ]

# nltk.download('punkt', quiet=True)

# # Load Whisper
# print("🔄 Loading Whisper model...")
# model = whisper.load_model("medium")
# print("✅ Whisper model loaded.")

# # Arabic NER with MARBERT
# bert_model = "UBC-NLP/MARBERTv2"
# tokenizer = AutoTokenizer.from_pretrained(bert_model)
# model_bert = AutoModelForTokenClassification.from_pretrained(bert_model)
# ner_pipeline = pipeline("ner", model=model_bert, tokenizer=tokenizer)

# spell_en = Speller(lang='en')
# spell_checker_ar = SpellChecker(language='ar')

# ACTION_KEYWORDS = {
#     "open": {
#         "open", "unlock", "activate", "enable", "turn on", "switch on", "start",
#         "schedule", "set timer for", "turn on at", "sync", "connect", "good morning",
#         "movie mode", "night mode", "شغل", "أشغل", "افتح", "أفتح", "شغّل", "قم بتشغيل",
#         "قم بإضاءة", "ابدأ", "استأنف", "استمرار", "حدد وقت التشغيل", "شغل عند",
#         "قم بتمكين", "اربط", "وصل", "صباح الخير", "وضع السينما", "وضع النوم"
#     },
#     "close": {
#         "close", "lock", "deactivate", "disable", "turn off", "switch off", "stop",
#         "pause", "turn off at", "أطفئ", "اغلق", "إيقاف", "أوقف", "أغلق", "إطفاء",
#         "وقف التشغيل", "وقف مؤقت", "أوقف", "أطفئ عند", "عطل", "تصبح على خير"
#     },
#     "increase": {
#         "increase", "raise", "brighten", "make brighter", "set brightness to",
#         "set fan speed to", "زود", "ارفع", "زيد", "اضبط السطوع إلى", "اجعل السطوع",
#         "سطع", "اجعل الإضاءة أقوى", "اضبط سرعة المروحة إلى"
#     },
#     "decrease": {
#         "decrease", "lower", "dim", "make dimmer", "قلل", "نقص", "خفض", "اخفض",
#         "خفف", "اجعل الإضاءة أضعف"
#     },
# }

# DEVICE_KEYWORDS = {
#     "light": {
#         "light", "lights", "lamp", "bulb", "leds", "ceiling light", "strip lights",
#         "الأضواء", "الضوء", "المصابيح", "المصباح", "اللمبات", "اللمبة", "الليدات",
#         "نور", "النور", "الإضاءة", "اللمبة الذكية", "مصباح السقف", "إضاءة الشريط"
#     },
#     "fan": {
#         "fan", "ceiling fan", "exhaust fan", "desk fan", "المروحة", "المراوح", "مروحة السقف",
#         "المروحة الذكية", "شفاط الهواء", "مروحة الطاولة"
#     },
#     "door": {
#         "door", "front door", "main door", "back door", "garage door", "الباب", "الأبواب",
#         "الباب الرئيسي", "باب المدخل", "الباب الأمامي", "الباب الخلفي", "باب الجراج"
#     },
#     "curtain": {
#         "curtain", "curtains", "blinds", "shades", "window covers", "الستارة", "الستائر",
#         "البرادي", "الشيش", "الستائر الذكية", "الغالق", "مظلة النافذة"
#     },
#     "camera": {
#         "camera", "security camera", "cctv", "surveillance", "الكاميرا", "الكاميرات",
#         "كاميرا المراقبة", "كاميرا الأمن", "كاميرا cctv", "المراقبة"
#     }
# }

# LOCATION_KEYWORDS = {
#     "kitchen": {
#         "kitchen", "cooking area", "منطقة الطهي", "المطبخ", "المطبخ الرئيسي"
#     },
#     "bathroom": {
#         "bathroom", "restroom", "toilet", "washroom", "الحمام", "دورة المياه",
#         "التواليت", "المرحاض", "الحمام الرئيسي"
#     },
#     "room": {
#         "room", "my room", "غرفة", "غرفه", "غرفتي", "حجرتي", "guest room",
#         "غرفة الضيوف", "bedroom", "غرفة النوم", "master bedroom", "غرفة النوم الرئيسية"
#     },
#     "living room": {
#         "living room", "hall", "lounge", "main room", "reception", "صالة", "الصالون",
#         "الريسيبشن", "الريسبشن", "الغرفة الرئيسية"
#     },
#     "outdoor": {
#         "balcony", "الشرفة", "البلكونة", "terrace", "التراس", "patio", "الفناء",
#         "الباحة", "porch", "المساحة الخارجية"
#     },
#     "garage": {
#         "garage", "carport", "الكراج", "الجراج", "مكان السيارة", "الموقف"
#     }
# }


# # ====== Normalization Helpers ======
# def match_all_from_dict(text: str, keyword_dict: dict) -> list[str]:
#     matches = []
#     for key, variations in keyword_dict.items():
#         for v in variations:
#             if v in text:
#                 matches.append(key)
#                 break  # Avoid duplicates if multiple synonyms match
#     return matches

# # ====== Command Processors ======
# def process_english_command(command: str) -> tuple[list[str], list[str], list[str]]:
#     command = re.sub(r'[^\w\s]', '', command.lower())
#     print("process_english_command is : " , command)
#     actions = match_all_from_dict(command, ACTION_KEYWORDS)
#     devices = match_all_from_dict(command, DEVICE_KEYWORDS)
#     locations = match_all_from_dict(command, LOCATION_KEYWORDS)
#     print("actions is : " , actions ,"devices is : " , devices ,"locations is : " , locations )
#     return actions, devices, locations

# def process_arabic_command(command: str) -> tuple[list[str], list[str], list[str]]:
#     command = re.sub(r'[^\w\s\u0600-\u06FF]', '', command.lower())

#     actions = match_all_from_dict(command, ACTION_KEYWORDS)
#     devices = match_all_from_dict(command, DEVICE_KEYWORDS)
#     locations = match_all_from_dict(command, LOCATION_KEYWORDS)

#     return actions, devices, locations


# # Record mic input
# def record_audio(duration=15, filename='mic_input.wav', samplerate=16000):
#     print("🎙️ Recording from microphone...")
#     recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
#     sd.wait()
#     with wave.open(filename, 'w') as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(2)
#         wf.setframerate(samplerate)
#         wf.writeframes(recording.tobytes())
#     print(f"✅ Recording saved to: {filename}")
#     return filename

# # NLP Processing
# # ✅ Process English Commands (Updated)

# # Arabic pipeline
# def process_audio_en(file_path):
#     print(f"🔍 Processing file: {file_path}")

#     if not os.path.exists(file_path):
#         print("❌ Error: File not found!")
#         return {'error': 'File not found'}

#     try:
#         # ✅ Transcribe audio using Whisper
#         result = model.transcribe(file_path, language="en")
#         transcribed_text = result.get('text', '').strip()

#         if not transcribed_text:
#             print("⚠ Warning: Whisper did not return any text!")
#             return {'error': 'No speech detected'}

#         print(f"📝 Transcribed Text: {transcribed_text}")

#         # ✅ Split the transcribed text into multiple commands (assuming ',' or 'and' separate commands)
#         commands = transcribed_text.lower().replace(" and ", ",").split(",")

#         sent_commands = []

#         for command in commands:
#             command = command.strip()
#             tokens = word_tokenize(command)
#             corrected_tokens = [spell_en(t) for t in tokens]
#             print("the send to process_english_command : ",corrected_tokens)
#             print("the type is : ",type(corrected_tokens))
#             actions, rooms ,devices  = process_english_command(" ".join(corrected_tokens))

#             if not actions or not devices:
#                 print(f"⚠ Warning: Invalid command detected - {command}")
#                 continue  # Skip invalid commands

#             location = rooms[0] if rooms else ""
#             command_to_esp = f"{actions[0]} {devices[0]} {location}".strip()
#             print(f"🚀 Sending to ESP32: {command_to_esp}")

#         return {
#             'text': transcribed_text,
#             'sent_commands': sent_commands,
#         }

#     except Exception as e:
#         return {'error': str(e)}

# # Arabic NER with MBERT
# bert_model = "bert-base-multilingual-cased"
# tokenizer = AutoTokenizer.from_pretrained(bert_model)
# model_bert = AutoModelForTokenClassification.from_pretrained(bert_model)
# ner_pipeline = pipeline("ner", model=model_bert, tokenizer=tokenizer)

# def process_audio_ar(file_path):
#     print(f"🔍 Processing file: {file_path}")

#     if not os.path.exists(file_path):
#         print("❌ Error: File not found!")
#         return {'error': 'File not found'}

#     try:
#         # ✅ Transcribe audio using Whisper (Dummy transcription)
#         result = model.transcribe(file_path, language="ar")
#         transcribed_text = result.get('text', '').strip()

#         if not transcribed_text:
#             print("⚠ Warning: Whisper did not return any text!")
#             return {'error': 'No speech detected'}

#         print(f"📝 Transcribed Text: {transcribed_text}")

#         # mBERT Named Entity Recognition
#         ner_results = ner_pipeline(transcribed_text)
#         print("🔍 mBERT NER Results:", ner_results)

#         # Extract tokens and labels
#         entities = [entity['word'] for entity in ner_results if entity['score'] > 0.95]
#         print(f"✨ Detected Entities: {entities}")

#         tokens = word_tokenize(transcribed_text)
#         corrected_tokens = [spell_checker_ar.correction(t) for t in tokens]

#         actions, rooms, devices = process_arabic_command(transcribed_text)  # Use original Arabic text without translation

#         # ✅ Print extracted command
#         print(f"🔹 Actions: {actions}")
#         print(f"🔹 Rooms: {rooms}")
#         print(f"🔹 Devices: {devices}")

#         return {
#             'text': transcribed_text,
#             'entities': entities,
#             'corrected_tokens': corrected_tokens,
#             'actions': actions,
#             'rooms': rooms,
#             'devices': devices
#         }
#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return {'error': str(e)}

# # Main loop
# if __name__ == "__main__":
#     lang_choice = input("🌐 Choose language (en/ar): ").strip().lower()

#     audio_path = record_audio()

#     if lang_choice == "ar":
#         process_audio_ar(audio_path)
#     else:
#         process_audio_en(audio_path)

#     os.remove(audio_path)

# from langdetect import detect, DetectorFactory
# DetectorFactory.seed = 0  # لضمان نفس النتائج في كل مرة


# text = input("Write the sentence that you want to know its language: ")


# language = detect(text)

# print(f"Expected language: {language}")

# import fasttext

# # Load pre-trained language identification model
# model = fasttext.load_model("lid.176.bin")

# # Input from user
# text = input("Enter a sentence to detect its language: ")

# # Predict the language
# prediction = model.predict(text)
# language_label = prediction[0][0].replace("__label__", "")
# # confidence = prediction[1][0]

# # Output result
# print(f"Detected language: {language_label}")
# # print(f"Confidence: {confidence:.2f}")

# import fasttext
# import tkinter as tk
# from tkinter import messagebox

# # Load the model
# model = fasttext.load_model("lid.176.bin")

# # Function to detect language
# def detect_language():
#     text = input_field.get()
#     if not text.strip():
#         messagebox.showwarning("Input Error", "Please enter some text.")
#         return
#     prediction = model.predict(text)
#     language_label = prediction[0][0].replace("__label__", "")
#     # confidence = prediction[1][0]
#     result_label.config(text=f"Detected language: {language_label}")
#     # result_label.config(text=f"Detected language: {language_label} (Confidence: {confidence:.2f})")

# # Create GUI window-
# window = tk.Tk()
# window.title("Language Detection (fastText)")
# window.geometry("400x200")

# # Input field
# tk.Label(window, text="Enter a sentence:").pack(pady=5)
# input_field = tk.Entry(window, width=50)
# input_field.pack(pady=5)

# # Detect button
# detect_btn = tk.Button(window, text="Detect Language", command=detect_language)
# detect_btn.pack(pady=10)

# # Result label
# result_label = tk.Label(window, text="", fg="blue", font=("Arial", 12))
# result_label.pack(pady=10)

# # Run the GUI
# window.mainloop()






import os
import re

from audio_utils import record_audio
from whisper_utils import transcribe_audio
from nlp_en import process_english_command
from nlp_ar import process_arabic_command


def split_commands(text: str, lang: str) -> list[str]:
    t = text.strip()
    t = t.replace("،", " ")
    if lang == "ar":
        parts = re.split(r"\bو\b|\bثم\b|\bوبعدين\b", t)
    else:
        t = t.lower().replace(" and ", ",")
        parts = [p for p in t.split(",")]
    return [p.strip() for p in parts if p.strip()]


if __name__ == "__main__":
    lang_choice = input("🌐 Choose language (en/ar): ").strip().lower()

    audio_path = record_audio(duration=10)

    if lang_choice == "ar":
        text = transcribe_audio(audio_path, "ar")
        print("📝 Text:", text)

        commands = split_commands(text, "ar")
        for i, cmd in enumerate(commands, 1):
            actions, devices, locations = process_arabic_command(cmd)
            print(f"\n— Command #{i}: {cmd}")
            print("⚙️ Actions:", actions)
            print("📟 Devices:", devices)
            print("📍 Locations:", locations)

    else:
        text = transcribe_audio(audio_path, "en")
        print("📝 Text:", text)

        commands = split_commands(text, "en")
        for i, cmd in enumerate(commands, 1):
            actions, devices, locations = process_english_command(cmd)
            print(f"\n— Command #{i}: {cmd}")
            print("⚙️ Actions:", actions)
            print("📟 Devices:", devices)
            print("📍 Locations:", locations)

    try:
        os.remove(audio_path)
    except OSError:
        pass
