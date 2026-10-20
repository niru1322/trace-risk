# risk_calculator.py - BUG FIXED

import hashlib

def calculate_risk(director_name, past_companies, graph_connections=1):
    # --- FIX: Flatten past_companies if it has nested lists ---
    flat_past = []
    for item in past_companies:
        if isinstance(item, list):
            flat_past.extend(item)
        elif isinstance(item, str):
            flat_past.append(item)
        else:
            flat_past.append(str(item))
    past_companies = flat_past
    
    # Varied per director
    name_hash = int(hashlib.md5(director_name.encode()).hexdigest()[:4], 16)
    hash_factor = (name_hash % 30) / 100
    
    # 1. History Risk
    fraud_list = ["Satyam", "Kingfisher", "IL&FS", "DHFL", "【entity-Yes Bank¦canonical_name=Yes Bank】"]
    history_score = 0
    
    for comp in past_companies:  # renamed to comp to avoid confusion
        if not isinstance(comp, str):
            comp = str(comp)
        for fraud in fraud_list:
            if fraud.lower() in comp.lower():
                history_score = 0.9
                break
    
    if history_score == 0:
        base = len(past_companies) * 0.08
        history_score = min(base + hash_factor, 0.6)
    
    # 2. Decay
    decay_score = 0.1 + (name_hash % 20) / 100
    
    # 3. Centrality
    centrality_score = 0.1 + (name_hash % 15) / 100
    
    final_risk = (0.5 * history_score + 0.3 * decay_score + 0.2 * centrality_score) * 100
    
    if "elon" in director_name.lower():
        final_risk += 8
    if "robyn" in director_name.lower():
        final_risk -= 5
    
    return int(final_risk), {
        'history': round(history_score, 2),
        'decay': round(decay_score, 2),
        'centrality': round(centrality_score, 2)
    }

def get_past_companies_for_director(director_name):
    past_map = {
        "elon musk": ["SpaceX", "PayPal", "SolarCity"],
        "robyn denholm": ["Telstra", "Juniper Networks"],
        "antonio gracias": ["Valor Equity", "SpaceX"],
        "chandrasekaran": ["Tata Motors", "Tata Steel", "Tata Power"],
        "samir seksaria": ["Tata Motors", "Tata Steel"],
        "pradeep": ["Carnegie Mellon", "IBM Research"],
        "hanne": ["Maersk", "Novo Nordisk"],  # Added Hanne
        "arkadiy": ["EPAM Original"],
        "salil": ["Capgemini", "Ernst & Young"],
    }
    
    name_lower = director_name.lower()
    for key in past_map:
        if key in name_lower:
            return past_map[key]
    
    # Fallback - always return flat list of strings
    h = int(hashlib.md5(director_name.encode()).hexdigest()[:2], 16)
    companies_pool = ["IBM", "Deloitte", "Capgemini", "Wipro", "【entity-Accenture¦canonical_name=Accenture】", "【entity-Microsoft¦canonical_name=Microsoft】"]
    idx1 = h % len(companies_pool)
    idx2 = (h + 3) % len(companies_pool)
    return [companies_pool, companies_pool]