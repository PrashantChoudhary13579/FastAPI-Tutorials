from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile):

    print("Step 1: File received")

    # Read the uploaded file
    contents = await file.read()

    print("Step 2: File has been read")

    return {
        "filename": file.filename,
        "size": len(contents),
        "message": "File uploaded successfully!"
    }