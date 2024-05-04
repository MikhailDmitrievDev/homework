from fastapi import APIRouter, Depends

from storage import Storage
from depends import get_storage
from service import TaskManager

router = APIRouter(prefix='/tasks')


@router.get('/')
async def tasks(storage: Storage = Depends(get_storage)):
    """
    Route returned all tasks in storage

    :param storage: returned actual storage instance
    """
    task_manager = TaskManager(storage)
    return await task_manager.get_tasks()


@router.post('/')
async def create(task):
    """
    Route create new task in storage

    :param task: Task entity
    """
    ...
