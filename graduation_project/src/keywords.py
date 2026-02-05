# ========= ACTIONS =========
ACTION_KEYWORDS = {
    "open": {
        "turn on", "switch on", "activate", "enable", "open", "unlock", "start",
        "شغل", "أشغل", "شغّل", "قم بتشغيل", "افتح", "أفتح", "ابدأ", "قم بتمكين"
    },
    "close": {
        "turn off", "switch off", "deactivate", "disable", "close", "lock", "stop", "pause",
        "أطفئ", "اطفي", "إطفاء", "أوقف", "اوقف", "إيقاف", "اغلق", "أغلق", "اقفل", "قفل", "عطل"
    },
    "increase": {
        "increase", "raise", "brighten", "make brighter", "up",
        "زود", "زوّد", "ارفع", "زيد", "سطع", "علّي", "أعلى"
    },
    "decrease": {
        "decrease", "lower", "dim", "make dimmer", "down",
        "قلل", "قلّل", "خفض", "اخفض", "وطي", "خفف"
    },
}

# ========= DEVICES =========
DEVICE_KEYWORDS = {
    "light": {
        "light", "lights", "lamp", "bulb", "led", "leds", "ceiling light", "strip lights",
        "النور", "نور", "الضوء", "الاضواء", "الأضواء", "الإضاءة", "لمبة", "اللمبة", "مصباح", "المصباح", "ليد"
    },
    "fan": {
        "fan", "ceiling fan", "exhaust fan", "desk fan",
        "مروحة", "المروحة", "مراوح", "المراوح", "شفاط", "المرواحة"
    },
    "door": {
        "door", "front door", "main door", "back door", "garage door",
        "باب", "الباب", "أبواب", "الأبواب", "باب الجراج", "الباب الرئيسي"
    },
    "curtain": {
        "curtain", "curtains", "blinds", "shades",
        "ستارة", "الستارة", "ستائر", "الستائر", "شيش", "برادي", "الغالق", "السطور"
    },
    "camera": {
        "camera", "security camera", "cctv", "surveillance",
        "كاميرا", "الكاميرا", "كاميرات", "الكاميرات", "مراقبة", "كاميرا مراقبة"
    }
}

# ========= LOCATIONS / ROOMS =========
LOCATION_KEYWORDS = {
    "kitchen": {"kitchen", "المطبخ", "مطبخ"},
    "bathroom": {"bathroom", "restroom", "toilet", "الحمام", "حمام", "التواليت", "دورة المياه"},
    "bedroom": {"bedroom", "غرفة النوم", "غرفه النوم", "اوضة النوم", "حجرة النوم"},
    "living room": {"living room", "hall", "lounge", "reception", "الصالة", "الصالون", "الريسيبشن", "الريسبشن"},
    "garage": {"garage", "carport", "الجراج", "كراج"},
    "outdoor": {"balcony", "terrace", "patio", "الشرفة", "البلكونة", "تراس", "الفناء"},
    # common typo from whisper sometimes
    "room": {"غرفة", "غرفتي", "اوضة", "الأوضة", "الأوضى"},
}
