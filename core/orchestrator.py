class MVPFOrchestrator:
    def __init__(self, consent_manager):
        self.consent = consent_manager

    def run(self, signals):
        if not self.consent.is_allowed():
            return "Consent not granted"

        if signals.get("danger"):
            return "Trigger Safety Layer"

        if signals.get("confusion"):
            return "Trigger Cognitive Support"

        if signals.get("medical"):
            return "Trigger Medical Support"

        return "Monitoring"
