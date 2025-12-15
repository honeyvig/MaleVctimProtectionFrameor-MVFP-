from safety_layer.danger_detection import detect_coercion
from medical_layer.anomaly_detection import detect_possible_drugging

signals = {
    "isolation": True,
    "forced_ingestion": True,
    "threat_language": False,
}

vitals = {
    "heart_rate": 130,
    "oxygen": 90,
    "tremors": True,
}

print("Coercion Detected:", detect_coercion(signals))
print("Possible Drugging:", detect_possible_drugging(vitals))
