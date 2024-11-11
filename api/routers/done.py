from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()


@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
    pass


@router.delete("/tasks/{task_id}/done")
async def unmark_task_as_done():
    pass
