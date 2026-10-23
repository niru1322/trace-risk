
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="TRACE-RISK API")

# CORS for real website
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- YOUR RISK DATA ---
RISK_DATA = {
    "TCS": {"company": "TCS", "risk_score": 23, "level": "LOW", "color": "green", "directors": ["N. Chandrasekaran", "Rajesh Gopinathan"], "reason": "Stable governance, no overlap"},
    "IL&FS": {"company": "IL&FS", "risk_score": 81, "level": "HIGH", "color": "red", "directors": ["Shared Director A", "Shared Director B", "Shared Director C"], "reason": "High director overlap - 3 shared directors across group companies - Classic IL&FS pattern"},
    "INFOSYS": {"company": "INFOSYS", "risk_score": 18, "level": "LOW", "color": "green", "directors": ["Nandan Nilekani", "Salil Parekh"], "reason": "Good governance"},
    "IGAP": {"company": "IGAP", "risk_score": 0, "level": "NOT_FOUND", "color": "gray", "directors": [], "reason": "Company not found in MCA database"}
}

@app.get("/api/risk")
def get_risk(company: str):
    key = company.strip().upper()
    data = RISK_DATA.get(key)
    if not data:
        # try partial match
        for k,v in RISK_DATA.items():
            if key in k or k in key:
                return v
        return {"company": company, "risk_score": 0, "level": "NOT_FOUND", "color": "gray", "directors": [], "reason": "Company not found"}
    return data

@app.get("/api/health")
def health():
    return {"status": "ok", "message": "TRACE-RISK API Live"}

# --- FRONTEND SERVING FOR VERCEL ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # backend/
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

@app.get("/")
def serve_root():
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "TRACE-RISK API running. Visit /docs for API docs, or /api/risk?company=TCS"}

# Mount frontend static
if os.path.exists(FRONTEND_DIR):
    try:
        app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
    except:
        pass
