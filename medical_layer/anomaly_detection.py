def detect_possible_drugging(vitals: dict) -> bool:
    abnormal = 0
    if vitals.get("heart_rate", 0) > 120:
        abnormal += 1
    if vitals.get("oxygen", 100) < 92:
        abnormal += 1
    if vitals.get("tremors"):
        abnormal += 1

    return abnormal >= 2
