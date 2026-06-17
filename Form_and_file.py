# Use File and Form together when you need to receive data and files in the same request

from fastapi import FastAPI, File, Form, UploadFile
from typing import Annotated

app = FastAPI()

@app.post("/file/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()], 
    token: Annotated[str, File()]
):
    return {
        "file_size":len(file),
        "tokens": token,
        "fileb_content_type":fileb.content_type
    }

# You can define files and form fields at the same time using File and Form.
# Create file and form parameters the same way you would for Body or Query.