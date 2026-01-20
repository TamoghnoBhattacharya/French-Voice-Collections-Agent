FORBIDDEN = ["menace", "pénalité", "huissier"]

def is_safe(text: str) -> bool:
    lowered = text.lower()
    return not any(word in lowered for word in FORBIDDEN)

def is_french_only(text: str) -> bool:
    # Extremely naive check, good enough for demo
    return not any(word in text.lower() for word in ["pay now", "debt", "call center"])
