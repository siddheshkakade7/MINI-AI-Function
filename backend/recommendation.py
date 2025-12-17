# recommendation.py

def generate_recommendation(summary: str) -> str:
    """
    Takes a summary (string) and returns a single-sentence recommendation.
    """
    if "health" in summary.lower():
        return "I recommend focusing on a balanced diet and regular exercise."
    elif "finance" in summary.lower():
        return "I recommend saving consistently and diversifying your investments."
    elif "study" in summary.lower():
        return "I recommend creating a daily study schedule and sticking to it."
    else:
        return "I recommend taking practical next steps based on your summary."
