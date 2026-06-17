## Use File, bytes, and UploadFile to declare files to be uploaded in the request, sent as form data. 

### UploadFile has the following async methods. 
They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).

- write(data): Writes data (str or bytes) to the file.
- read(size): Reads size (int) bytes/characters of the file.
- seek(offset): Goes to the byte position offset (int) in the file.
    - E.g., await myfile.seek(0) would go to the start of the file.
    - This is especially useful if you run await myfile.read() once and then need to read the contents again.
- close(): Closes the file.

### await- 

Instead of making the whole server wait, FastAPI lets other requests run while this file is being read.

That's what await means.

It tells Python:

- "Pause this function until the file has been read. Meanwhile, go do other work."