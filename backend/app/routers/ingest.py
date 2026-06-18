from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.ingestor import ingest_all_sources

router = APIRouter()


@router.post("/ingest")
def trigger_ingest(db: Session = Depends(get_db)):
    count = ingest_all_sources(db)
    return {"message": f"Ingestão concluída", "articles": count}
