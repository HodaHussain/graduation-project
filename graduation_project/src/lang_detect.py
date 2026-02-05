from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

def detect_language(text):
    return detect(text)
