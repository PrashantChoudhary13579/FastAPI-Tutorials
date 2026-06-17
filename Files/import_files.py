from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import Annotated

router = FastAPI()

@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size":len(file)}

# using the uploadfile has much more advantages over File() 
@router.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    return {"file_content":file.content_type,"filename":file.filename,}

# File() - 
# FastAPI reads the entire uploaded file into memory.
# The variable file is of type bytes.

# UploadFile
# does not load the whole file into memory immediately. 

