import re

BLOCKED_PATTERNS = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"bypass security",
    r"drop\s+table",
    r"or\s+1=1",
    r"<script.*?>"
]

def sanitize_input(user_input):

    # Empty input check
    if not user_input or not user_input.strip():
        return False, "Input cannot be empty"

    # HTML detection (strip/block)
    if re.search(r"<[^>]+>", user_input):
        return False, "HTML content is not allowed"

    # Prompt injection detection
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return False, "Potential malicious input detected"

    return True, "Valid input"