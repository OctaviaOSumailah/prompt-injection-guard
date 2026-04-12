import re

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"disregard all prior",
    r"reveal (the )?system prompt",
    r"you are now",
    r"act as",
    r"bypass restrictions",
]

def detect_prompt_injection(text):
    text_lower = text.lower()
    matches = []

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            matches.append(pattern)

    if matches:
        return {
            "risk": "HIGH",
            "matches": matches,
            "action": "BLOCK"
        }

    return {
        "risk": "LOW",
        "matches": [],
        "action": "ALLOW"
    }