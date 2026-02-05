import re
from keywords import ACTION_KEYWORDS, DEVICE_KEYWORDS, LOCATION_KEYWORDS


def _normalize_ar(text: str) -> str:
    # Quick normalizations for common Whisper mistakes
    t = text.strip().lower()
    t = t.replace("الأوضى", "الأوضة")
    t = t.replace("المرواحة", "المروحة")
    t = t.replace("مرواحة", "مروحة")
    t = t.replace("السطور", "الستائر")
    return t


def _match_all(text: str, keyword_dict: dict) -> list[str]:
    matches = []
    for key, variations in keyword_dict.items():
        for v in variations:
            if v in text:
                matches.append(key)
                break
    return matches


def process_arabic_command(command: str) -> tuple[list[str], list[str], list[str]]:
    command = _normalize_ar(command)
    command = re.sub(r"[^\w\s\u0600-\u06FF]", " ", command)  # keep Arabic
    command = re.sub(r"\s+", " ", command).strip()

    actions = _match_all(command, ACTION_KEYWORDS)
    devices = _match_all(command, DEVICE_KEYWORDS)
    locations = _match_all(command, LOCATION_KEYWORDS)
    return actions, devices, locations
