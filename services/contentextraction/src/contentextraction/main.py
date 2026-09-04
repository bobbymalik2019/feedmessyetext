from fastapi import FastAPI
from contentextraction.api.extractions import router as extraction_router

app = FastAPI(
    title="Structured Extraction API",
    description="API for converting unstructured content into structured, validated output.",
    version="1.0.0",
)

app.include_router(extraction_router)

@app.get("/health")
def health():
    return {"status": "UP"}