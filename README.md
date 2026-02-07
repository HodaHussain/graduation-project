## Voice-Controlled Smart Home (Arabic & English) – Graduation Project

This project implements a Voice-Controlled Smart Home System that allows users to control home devices using spoken commands in both English and Arabic.
The system uses OpenAI Whisper for speech-to-text, then applies an NLP-based command parser (keyword matching + optional NER/spell correction) to extract the intended action, device, and location, and finally sends the command to an ESP-based microcontroller to execute the action.

## Key Features

Real-time voice command recording from microphone

Speech-to-text transcription using Whisper (medium model)

Bilingual support: English & Arabic

Command understanding through:

Keyword matching (Actions / Devices / Locations)

Spell correction (English & Arabic)

Named Entity Recognition (NER) for Arabic (MARBERTv2 / mBERT)

Command formatting and sending to ESP (ESP32/ESP8266) for device control

Modular implementation (split into multiple files) + Flutter application integration

## System Pipeline

# 1-Voice Capture

Record audio from microphone (sounddevice, wave)

# 2-Speech Recognition (ASR)

Transcribe speech using Whisper → output text

# 3-Text Processing & NLP

Normalize text (remove punctuation, lowercase)

Tokenization (nltk)

Spell correction:

English: autocorrect.Speller

Arabic: pyspellchecker

Extract:

Action (open/close/increase/decrease…)

Device (light/fan/door/curtain/camera…)

Location (kitchen/bathroom/room/living room/garage…)

Optional Arabic NER using Transformers (MARBERTv2 or mBERT)

# 4-IoT Execution

Build a structured command (e.g., open light kitchen)

Send the command to the ESP module to control relays/devices

## Technologies Used
# 1- Software

Python

whisper, transformers, nltk, sounddevice, librosa (optional), numpy

Flutter (Mobile UI / Smart Home interface)

C++ (ESP firmware)

# 2- Hardware

ESP-based microcontroller (ESP32 / ESP8266)

Relays + connected home appliances (lights, fan, etc.)

## Supported Commands (Examples)

# English:

“Turn on the kitchen lights”

“Close the door”

“Increase fan speed in the living room”

# Arabic:

“شغل نور المطبخ”

“اقفل الباب”

“زود سرعة المروحة في الصالة”

## Future Work

Improve Arabic understanding for dialect variations

Add more devices and automation scenarios (modes, schedules)

Integrate cloud logging and user profiles

Add offline ASR option for low-resource devices
