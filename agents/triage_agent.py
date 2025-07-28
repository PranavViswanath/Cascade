# agents/triage_agent.py

def triage_contradictions(severity_scores):
    """
    Sorts contradicted papers by severity (highest to lowest).
    Returns a sorted list of tuples: (paper_title, severity_score)
    """
    sorted_triage = sorted(severity_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_triage
