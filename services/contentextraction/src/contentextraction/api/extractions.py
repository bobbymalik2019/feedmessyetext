from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/v1/extractions",
    tags=["Extractions"],
)


@router.post("")
async def create_extraction(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    print(f"Received File: {file.filename}, content type: {file.content_type}, size: {len(content)} bytes")
    return {
        "status": "RECEIVED",
        "file": {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(content),
        },
    }