def trauma_informed_response(user_text: str) -> str:
    if "confused" in user_text.lower():
        return (
            "You are not weak or broken. Confusion can result from prolonged stress "
            "or manipulation. Let us slow things down and focus on your safety."
        )
    return "I am here to support you without judgment."
