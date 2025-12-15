def assess_exit_risk(environment: dict) -> str:
    if environment.get("surveillance") and environment.get("violence_history"):
        return "HIGH RISK – Delay exit, seek external help"
    return "MODERATE RISK – Exit possible with planning"
