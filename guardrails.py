def check_input(user_input):

    # Check empty input
    if not user_input or not user_input.strip():
        return False, "Please enter a valid question."

    # Check very long input
    if len(user_input) > 2000:
        return False, "Your message is too long. Please keep it under 2000 characters."

    # Basic prompt injection checks
    blocked_phrases = [
        "ignore previous instructions",
        "ignore all instructions",
        "reveal system prompt",
        "show system prompt",
        "forget your instructions",
        "act as a different ai",
        "ignore unneseray questions",
    ]

    user_input_lower = user_input.lower()

    for phrase in blocked_phrases:
        if phrase in user_input_lower:
            return False, "Sorry, I can't process that type of request."

    # Input is allowed
    return True, None