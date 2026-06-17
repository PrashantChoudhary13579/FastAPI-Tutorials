from fastapi import FastAPI, Form, File, UploadFile
from typing import Annotated

router = FastAPI()

@router.post("/file/")
async def create_file(
    file:Annotated[ bytes|None, File()] = None
):
    if not file:
        return {"message":"no file sent"}
    else:
        return {"message": len(file)}
    
@router.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile | None = None
):
    if not file:
        return {"message":"No upload file sent"}
    else:
        return {"message":file.filename}
    

# You can make a file optional by using standard type annotations and setting a default value of None