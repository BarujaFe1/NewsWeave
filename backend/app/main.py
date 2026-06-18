from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import profile, ingest, briefing

Base.metadata.create_all(bind=engine)

app = FastAPI(title="NewsWeave API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router, prefix="/api", tags=["profile"])
app.include_router(ingest.router, prefix="/api", tags=["ingest"])
app.include_router(briefing.router, prefix="/api", tags=["briefing"])


@app.get("/api/health")
def health():
    return {"status": "ok"}
