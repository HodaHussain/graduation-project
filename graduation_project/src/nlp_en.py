import re
from keywords import ACTION_KEYWORDS, DEVICE_KEYWORDS, LOCATION_KEYWORDS


def _match_all(text: str, keyword_dict: dict) -> list[str]:
    matches = []
    for key, variations in keyword_dict.items():
        for v in variations:
            if v in text:
                matches.append(key)
                break
    return matches


def process_english_command(command: str) -> tuple[list[str], list[str], list[str]]:
    command = re.sub(r"[^\w\s]", " ", command.lower())
    command = re.sub(r"\s+", " ", command).strip()

    actions = _match_all(command, ACTION_KEYWORDS)
    devices = _match_all(command, DEVICE_KEYWORDS)
    locations = _match_all(command, LOCATION_KEYWORDS)
    return actions, devices, locations
