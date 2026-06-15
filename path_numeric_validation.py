from fastapi import FastAPI, Query, Path
from typing import Annotated

router = FastAPI()

@router.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[
        int, 
        Path(
            title="Item id" ,
            description="Write down the item id in integer",ge=1, 
            lt=1000
            )
        ],
    q: str | None = None,
    size: Annotated[
        float | None,
        Query(gt=0.5, lt=10.5)
        ] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    if size:
        results.update({"size":size})
    return results