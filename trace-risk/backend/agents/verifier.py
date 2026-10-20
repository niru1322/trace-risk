# Verifier Agent - Judge (Anti-Hallucination)
def verifier_agent(fact, search_results):
    # Simple verifier: needs 2 sources
    if len(search_results) >= 2:
        confidence = 0.88
        print(f"[Verifier] Fact '{fact}' VERIFIED with {len(search_results)} sources. Confidence: {confidence}")
        return True, confidence
    else:
        confidence = 0.45
        print(f"[Verifier] Fact '{fact}' NOT VERIFIED. Only 1 source. Confidence: {confidence}")
        return False, confidence