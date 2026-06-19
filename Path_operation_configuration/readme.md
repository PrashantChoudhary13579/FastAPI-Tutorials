### 1. @app.post("/items/")

Notice there is no path parameter.
This endpoint works with the entire collection of items.

### 2. @app.post("/items/{item_id}")

is a path parameter.

#### You can configure and add metadata for your path operations easily by passing parameters to the path operation decorators.