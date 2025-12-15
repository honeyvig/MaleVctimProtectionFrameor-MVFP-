def detect_coercion(behavioral_signals: dict) -> bool:
    indicators = [
        behavioral_signals.get("isolation"),
        behavioral_signals.get("forced_ingestion"),
        behavioral_signals.get("threat_language"),
    ]
    return sum(bool(i) for i in indicators) >= 2
