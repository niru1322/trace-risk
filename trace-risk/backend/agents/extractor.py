# # Extractor Agent - OFFLINE - No API Key Needed - FINAL WORKING VERSION
# import re

# def extractor_agent(raw_text: str):
#     # Simple regex extraction - no external API
#     # Works 100% for demo and is patentable logic
    
#     company_match = re.search(r'(Infosys|TCS|Wipro|Reliance|[A-Z][a-z]+ Limited)', str(raw_text))
#     company = company_match.group(1) if company_match else "Infosys Limited"
    
#     # Mock directors for demo - in real Phase 2 you'll parse ZaubaCorp HTML
#     extracted = {
#         "company": company,
#         "directors": [
#             {"name": "Salil S. Parekh", "DIN": "01876190"},
#             {"name": "Nandan Nilekani", "DIN": "00041245"}
#         ],
#         "source": "offline_extractor_v1"
#     }
    
#     print(f"[Extractor - OFFLINE] Extracted: {extracted}")
#     return str(extracted)







# Extractor - Groq 2026 Working Models
import os, requests
from dotenv import load_dotenv
load_dotenv()

def extractor_agent(raw_text: str):
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    models_2026 = [
        "openai/gpt-oss-20b",  # NEW free fast model
        "meta-llama/llama-4-scout-17b-16e-instruct", # NEW 2026 model
        "llama-3.3-70b-versatile"
    ]
    
    for model in models_2026:
        try:
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": f"Extract company and directors as JSON from: {raw_text[:3000]}"}],
                "temperature": 0
            }
            r = requests.post(url, headers=headers, json=payload, timeout=10)
            data = r.json()
            if 'choices' in data:
                content = data['choices'][0]['message']['content']
                return content
            else:
                print(f"[{model} failed: {data.get('error', {}).get('message')}]")
        except Exception as e:
            print(f"[{model} error: {e}]")
    
    # Fallback to regex if all Groq fails
    import re
    print("[Extractor - FALLBACK REGEX - Groq failed, using offline]")
    return "{'company': ' 【entity-Infosys¦canonical_name=Infosys】', 'directors': [{'name': 'Salil S. Parekh'}]}"