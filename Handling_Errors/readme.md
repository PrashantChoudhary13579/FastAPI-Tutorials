## Handling Errors

### Raise an HTTPException in your code
- HTTPException is a normal Python exception with additional data relevant for APIs.

### Add custom headers
- There are some situations in where it's useful to be able to add custom headers to the HTTP error. For example, for some types of security.

### Install custom exception handlers
- You can add custom exception handlers with the same exception utilities from Starlette

### Override the default exception handlers

- FastAPI has some default exception handlers.

- These handlers are in charge of returning the default JSON responses when you raise an HTTPException and when the request has invalid data.

- You can override these exception handlers with your own.

#### 1. Override request validation exception
- When a request contains invalid data, FastAPI internally raises a RequestValidationError.

- And it also includes a default exception handler for it.

- To override it, import the RequestValidationError and use it with @app.exception_handler(RequestValidationError) to decorate the exception handler.

- The exception handler will receive a Request and the exception.

#### 2. Override the HTTPException error handler
- The same way, you can override the HTTPException handler.

#### 3. Use the RequestValidationError body
- The RequestValidationError contains the body it received with invalid data.

### Reuse FastAPI's exception handlers

- If you want to use the exception along with the same default exception handlers from FastAPI, you can import and reuse the default exception handlers from fastapi.exception_handlers