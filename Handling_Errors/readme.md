## Handling Errors

### Override the default exception handlers

- FastAPI has some default exception handlers.

- These handlers are in charge of returning the default JSON responses when you raise an HTTPException and when the request has invalid data.

- You can override these exception handlers with your own.

### Override request validation exception
- When a request contains invalid data, FastAPI internally raises a RequestValidationError.

- And it also includes a default exception handler for it.

- To override it, import the RequestValidationError and use it with @app.exception_handler(RequestValidationError) to decorate the exception handler.

- The exception handler will receive a Request and the exception.